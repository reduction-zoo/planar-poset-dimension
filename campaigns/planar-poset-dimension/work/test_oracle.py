from check import legal_target,solve_target,valid_target


def point(x,y):
    return [[x,1],[y,1]]


def test_hand_cases():
    chain = {"vertices":2,"covers":[[0,1]],"points":[point(0,0),point(0,1)],"routes":[[point(0,0),point(0,1)]],"dimension":1}
    assert valid_target(chain,{"orders":[[0,1]]})
    antichain = {"vertices":2,"covers":[],"points":[point(0,0),point(1,0)],"routes":[],"dimension":1}
    assert solve_target(antichain) == {"status":"NO-SOLUTION"}
    assert valid_target({**antichain,"dimension":2},{"orders":[[0,1],[1,0]]})
    assert not legal_target({**chain,"points":[point(0,1),point(0,0)]})
    assert not valid_target(chain,{"orders":[[1,0]]})
    bent = {**chain,"points":[point(0,0),point(0,2)],
            "routes":[[point(0,0),point(1,1),point(0,2)]]}
    assert legal_target(bent)
    crossing = {"vertices":4,"covers":[[0,2],[1,3]],
                "points":[point(0,0),point(1,0),point(1,1),point(0,1)],
                "routes":[[point(0,0),point(1,1)],[point(1,0),point(0,1)]],
                "dimension":2}
    assert not legal_target(crossing)
    transitive = {"vertices":3,"covers":[[0,1],[1,2],[0,2]],
                  "points":[point(0,0),point(0,1),point(0,2)],
                  "routes":[[point(0,0),point(0,1)],[point(0,1),point(0,2)],
                            [point(0,0),point(0,2)]],"dimension":1}
    assert not legal_target(transitive)


if __name__ == "__main__":
    test_hand_cases()
