# 3-SAT → Dimension of a poset with a planar diagram

Category: Complexity open

## Source

A source instance is an explicitly encoded Boolean formula with at most three literals per clause. Its outputs are satisfying Boolean assignments, or NO-SOLUTION when the formula is unsatisfiable.

## Target

The target supplies a finite poset, an upward planar Hasse diagram with rational polyline coordinates, and a dimension bound d. Find at most d linear orders whose intersection is the poset, or report NO-SOLUTION.

## Required result

Construct deterministic polynomial-time maps F and G: F sends every legal source instance to a legal target instance, and G(x,y) is a valid source output for every valid output y of F(x). Preserve the stated threshold, domain and promises. The requested complexity conclusion is NP-hardness for the stated target problem.

## Acceptance

Give explicit construction and recovery algorithms, a general proof for every legal input and every valid target output, and polynomial runtime and encoding-size bounds. Specify finite output encodings and handle NO-SOLUTION outputs when applicable. Tests compare recovered source outputs with independent source solutions.

## Why it matters

This separates the complexity of order dimension from the complexity of obtaining a planar drawing.

## Difficulty

The reduction must construct a valid upward planar diagram while enforcing every order constraint.

## Literature context

Supplying a planar diagram does not fix a realizer. The proposed result concerns dimension despite that additional geometric information.

Literature checked 2026-09-16. This summarizes the archived literature search on the date above. Unpublished, unindexed and overlooked work remains outside coverage; no new novelty assessment was performed.

## References

- [Planarity and dimension II](https://arxiv.org/html/2607.09294v1): Blake, Hodor, Micek, Seweryn and Trotter, Planarity and dimension II, Section 1, explicitly leave exact dimension complexity for planar diagrams open. Their polynomial-time approximation outputs dimension at most 96 dim(P)+672. This does not decide a given exact threshold. Their diagram representation discussion also distinguishes diagram recognition hardness from dimension computation with a diagram supplied. Neither general-poset hardness nor height-two hardness establishes this restricted target.
- [version history](https://arxiv.org/abs/2607.09294): On 2026-09-16 searched "2026" "remains open" "NP-hard" scheduling strings, then "planar posets" "dimension" "NP-hard" 2026, "planar diagram" "dimension" complexity open, and "poset dimension" planarization crossing reduction. Inspected the introduction, definitions and version history, which lists v1 dated July 10. No later classification was identified within this search. This is evidence of present openness, not exhaustive coverage of all literature.

Fixed from board record `website/questions/planar-poset-dimension.json` in board checkout at 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17; the record was copied from the current working tree.
