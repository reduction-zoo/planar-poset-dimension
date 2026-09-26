"""Independent 3-SAT and split-graph star-coloring oracles."""

import argparse
import json
import subprocess
import sys
from itertools import combinations, permutations, product
from pathlib import Path

import z3


def legal_source(source):
    if not isinstance(source, dict):
        return False
    n = source.get("num_vars")
    clauses = source.get("clauses")
    return (type(n) is int and n >= 0 and isinstance(clauses, list)
            and all(isinstance(clause, list) and len(clause) <= 3
                    and all(type(literal) is int and 1 <= abs(literal) <= n for literal in clause)
                    for clause in clauses))


def solve_source(source):
    if not legal_source(source):
        raise ValueError("Illegal source formula")
    variables = [z3.Bool(f"x{i}") for i in range(source["num_vars"])]
    solver = z3.Solver()
    for clause in source["clauses"]:
        solver.add(z3.Or(*(variables[abs(literal) - 1] if literal > 0
                           else z3.Not(variables[-literal - 1]) for literal in clause)))
    result = solver.check()
    if result == z3.unsat:
        return {"status": "NO-SOLUTION"}
    if result != z3.sat:
        raise RuntimeError(f"Inconclusive source solver: {result}")
    model = solver.model()
    return {"assignment": [z3.is_true(model.eval(variable, model_completion=True)) for variable in variables]}


def valid_source(source, output):
    if not legal_source(source) or not isinstance(output, dict):
        return False
    if output == {"status": "NO-SOLUTION"}:
        return solve_source(source) == output
    assignment = output.get("assignment")
    if set(output) != {"assignment"} or not isinstance(assignment, list) or len(assignment) != source["num_vars"] or any(type(value) is not bool for value in assignment):
        return False
    return all(any(assignment[abs(literal) - 1] == (literal > 0) for literal in clause)
               for clause in source["clauses"])


from fractions import Fraction


def rational(pair):
    return (isinstance(pair,list) and len(pair) == 2
            and all(type(v) is int for v in pair) and pair[1] > 0)


def point(raw):
    return Fraction(*raw[0]),Fraction(*raw[1])


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on_segment(a,b,c):
    return (cross(a,b,c) == 0 and min(a[0],b[0]) <= c[0] <= max(a[0],b[0])
            and min(a[1],b[1]) <= c[1] <= max(a[1],b[1]))


def intersects(a,b,c,d):
    ab_c,ab_d = cross(a,b,c),cross(a,b,d)
    cd_a,cd_b = cross(c,d,a),cross(c,d,b)
    if ab_c == ab_d == cd_a == cd_b == 0:
        return max(a[1],c[1]) <= min(b[1],d[1])
    return ((ab_c <= 0 <= ab_d or ab_d <= 0 <= ab_c)
            and (cd_a <= 0 <= cd_b or cd_b <= 0 <= cd_a))


def closure(n,covers):
    reach = [[False]*n for _ in range(n)]
    for u,v in covers:
        reach[u][v] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    return reach


def legal_target(target):
    if not isinstance(target,dict) or set(target) != {"vertices","covers","points","routes","dimension"}:
        return False
    n,covers,points,routes,d = (target[key] for key in ("vertices","covers","points","routes","dimension"))
    if (type(n) is not int or n < 0 or type(d) is not int or d < 1
            or not isinstance(covers,list) or not isinstance(points,list) or len(points) != n
            or not isinstance(routes,list) or len(routes) != len(covers)
            or any(not isinstance(edge,list) or len(edge) != 2
                   or any(type(v) is not int or not 0 <= v < n for v in edge)
                   or edge[0] == edge[1] for edge in covers)
            or len({tuple(edge) for edge in covers}) != len(covers)
            or any(not isinstance(raw,list) or len(raw) != 2
                   or not all(rational(coord) for coord in raw) for raw in points)
            or any(not isinstance(route,list) or len(route) < 2
                   or any(not isinstance(raw,list) or len(raw) != 2
                          or not all(rational(coord) for coord in raw) for raw in route)
                   for route in routes)):
        return False
    locations = [point(raw) for raw in points]
    if len(set(locations)) != n:
        return False
    polylines = [[point(raw) for raw in route] for route in routes]
    for (u,v),line in zip(covers,polylines):
        if line[0] != locations[u] or line[-1] != locations[v]:
            return False
        if any(a[1] >= b[1] for a,b in zip(line,line[1:])):
            return False
        for w,location in enumerate(locations):
            if w not in (u,v) and any(on_segment(a,b,location) for a,b in zip(line,line[1:])):
                return False
    reach = closure(n,covers)
    if any(reach[v][v] for v in range(n)):
        return False
    if any(any(w not in (u,v) and reach[u][w] and reach[w][v] for w in range(n))
           for u,v in covers):
        return False
    for i,j in combinations(range(len(covers)),2):
        allowed = {locations[v] for v in set(covers[i]) & set(covers[j])}
        left,right = polylines[i],polylines[j]
        for a,b in zip(left,left[1:]):
            for c,e in zip(right,right[1:]):
                if not intersects(a,b,c,e):
                    continue
                shared = {a,b} & {c,e} & allowed
                if len(shared) != 1:
                    return False
                common = next(iter(shared))
                if cross(a,b,c) == cross(a,b,e) == 0:
                    if max(a[1],c[1]) != min(b[1],e[1]) or common[1] != max(a[1],c[1]):
                        return False
    return True


def direct_realizer(target,orders):
    n,d = target["vertices"],target["dimension"]
    if (not isinstance(orders,list) or len(orders) != d
            or any(not isinstance(order,list) or len(order) != n
                   or any(type(v) is not int for v in order)
                   or sorted(order) != list(range(n)) for order in orders)):
        return False
    reach = closure(n,target["covers"])
    positions = [{v:i for i,v in enumerate(order)} for order in orders]
    return all(all(position[u] < position[v] for position in positions) == reach[u][v]
               for u in range(n) for v in range(n) if u != v)


def target_solutions(target,limit=3):
    if not legal_target(target):
        raise ValueError("Illegal upward planar poset diagram")
    n,d = target["vertices"],target["dimension"]
    reach = closure(n,target["covers"])
    pos = [[z3.Int(f"p_{r}_{v}") for v in range(n)] for r in range(d)]
    solver = z3.Solver()
    for row in pos:
        if n:
            solver.add(z3.Distinct(row))
        for variable in row:
            solver.add(variable >= 0,variable < n)
    for u in range(n):
        for v in range(u+1,n):
            if reach[u][v]:
                solver.add(*[row[u] < row[v] for row in pos])
            elif reach[v][u]:
                solver.add(*[row[v] < row[u] for row in pos])
            else:
                solver.add(z3.Or(*[row[u] < row[v] for row in pos]))
                solver.add(z3.Or(*[row[v] < row[u] for row in pos]))
    outputs = []
    while len(outputs) < limit:
        result = solver.check()
        if result == z3.unsat:
            break
        if result != z3.sat:
            raise RuntimeError(f"Inconclusive dimension solver: {result}")
        model = solver.model()
        values = [[model.eval(variable).as_long() for variable in row] for row in pos]
        orders = [sorted(range(n),key=lambda v:row[v]) for row in values]
        assert direct_realizer(target,orders)
        outputs.append({"orders":orders})
        block = [variable != values[r][v] for r,row in enumerate(pos)
                 for v,variable in enumerate(row)]
        if not block:
            break
        solver.add(z3.Or(*block))
    return outputs or [{"status":"NO-SOLUTION"}]


def solve_target(target):
    return target_solutions(target,1)[0]


def valid_target(target,output):
    if not legal_target(target) or not isinstance(output,dict):
        return False
    if output == {"status":"NO-SOLUTION"}:
        return solve_target(target) == output
    return set(output) == {"orders"} and direct_realizer(target,output["orders"])


def exhaustive_target(target):
    n,d = target["vertices"],target["dimension"]
    reach = closure(n,target["covers"])
    extensions = [order for order in permutations(range(n))
                  if all(order.index(u) < order.index(v) for u in range(n) for v in range(n)
                         if reach[u][v])]
    for orders in product(extensions,repeat=d):
        if direct_realizer(target,[list(order) for order in orders]):
            return {"orders":[list(order) for order in orders]}
    return {"status":"NO-SOLUTION"}


def self_test():
    from generate_cases import EDGE_CASES,random_source
    from test_oracle import test_hand_cases
    root = Path(__file__).resolve().parents[3]
    path = Path(__file__).with_name("cases.json")
    subprocess.run([sys.executable,str(root/"research/validate_preparation.py"),str(path)],check=True,cwd=root)
    cases = json.loads(path.read_text())
    for n,clauses,answer in EDGE_CASES:
        assert ("assignment" in solve_source({"num_vars":n,"clauses":clauses})) == answer
    for case in cases:
        source = case["source"]
        if case["kind"] == "random":
            assert random_source(case["seed"]) == source
        current = solve_source(source)
        exists = any(all(any(bits[abs(lit)-1] == (lit > 0) for lit in clause)
                             for clause in source["clauses"])
                     for bits in product((False,True),repeat=source["num_vars"]))
        assert ("assignment" in current) == exists == ("assignment" in case["expected"])
        assert valid_source(source,current) and valid_source(source,case["expected"])
    test_hand_cases()
    import random
    yes,no = 0,0
    def raw(x,y):
        return [[x,1],[y,1]]
    for seed in range(100):
        rng = random.Random(seed)
        sizes = [rng.randint(1,3) for _ in range(rng.randint(1,3))]
        while sum(sizes) > 5:
            sizes[-1] -= 1
            if sizes[-1] == 0:
                sizes.pop()
        points,covers = [],[]
        for chain,size in enumerate(sizes):
            start = len(points)
            points += [raw(2*chain,i) for i in range(size)]
            covers += [[start+i,start+i+1] for i in range(size-1)]
        target = {"vertices":len(points),"covers":covers,"points":points,
                  "routes":[[points[u],points[v]] for u,v in covers],
                  "dimension":rng.randint(1,2)}
        assert legal_target(target)
        answer = solve_target(target)
        assert ("orders" in answer) == ("orders" in exhaustive_target(target))
        yes += "orders" in answer
        no += "orders" not in answer
    print(f"Self-test passed: {len(cases)} source formulas and {yes} YES/{no} NO planar-poset targets")


def candidate_check(path):
    self_test()
    cases = json.loads(Path(__file__).with_name("cases.json").read_text())
    recovered = 0
    for case in cases:
        source = case["source"]
        forward = subprocess.run([sys.executable,str(path)],input=json.dumps(source),text=True,capture_output=True,check=True)
        target = json.loads(forward.stdout)
        if not legal_target(target):
            raise AssertionError(f"Illegal target: {target}")
        for output in target_solutions(target):
            assert valid_target(target,output)
            payload = {"source":source,"target_solution":output}
            extraction = subprocess.run([sys.executable,str(path),"--extract"],input=json.dumps(payload),text=True,capture_output=True,check=True)
            recovered_output = json.loads(extraction.stdout)
            if not valid_source(source,recovered_output):
                raise AssertionError(f"Invalid recovery from {output}: {recovered_output}")
            recovered += 1
    print(f"Candidate check passed: {len(cases)} source cases, {recovered} target outputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test",action="store_true")
    group.add_argument("--candidate",type=Path)
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        candidate_check(args.candidate)
