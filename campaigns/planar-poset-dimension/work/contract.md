# Prepared contract

Source: `{"num_vars":n,"clauses":[[signed_literal,...],...]}` with at most three literals per clause. Output a satisfying Boolean `{"assignment":[...]}` or `{"status":"NO-SOLUTION"}`.

Target input is `{"vertices":n,"covers":[[lower,upper],...],"points":[point_by_element,...],"routes":[polyline_by_cover,...],"dimension":d}`. A point is `[[x_numerator,x_denominator],[y_numerator,y_denominator]]` with positive denominators. Each cover route starts and ends at its element points and has strictly increasing y on every segment. Covers must be exactly the Hasse edges of an acyclic relation; distinct vertices have distinct points; edges neither cross nor pass through unrelated vertices. A positive output `{"orders":[[element,...],...]}` contains exactly `d` linear extensions whose intersection is the poset. `NO-SOLUTION` means no such realizer exists.

`algorithm.py` reads source JSON from stdin and emits legal target JSON. `algorithm.py --extract` reads `{"source":source,"target_solution":output}` and emits a valid source output. Both commands are deterministic, polynomial time, independent subprocesses. Errors exit nonzero; diagnostics go to stderr. Recovery must handle every valid target output.
