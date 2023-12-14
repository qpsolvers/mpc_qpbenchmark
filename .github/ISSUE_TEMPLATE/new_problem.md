---
name: Submit a new problem
about: Propose a new problem for the GitHub-FFA test set
title: ''
labels: ''
assignees: ''
---

### Problem

I propose to add the following problem to the MPC test set. The problem can be built and tested as follows:

```python
import numpy as np
import qpsolvers

def build_problem():
    # Cost: x^T P x + q^T x
    P = ...
    q = ...
    # Inequality constraints: G x <= h
    G = ...
    h = ...
    # Equality constraints: A x == b
    A = ...
    b = ...
    # Box constraints: lb <= x <= ub
    lb = ...
    ub = ...
    return qpsolvers.Problem(P, q, G, h, A, b, lb, ub)

if __name__ == "__main__":
    solver = "proxqp"  # your favorite solver here
    x = qpsolvers.solve_problem(build_problem(), solver=solver)
```

### Context

<!--
    Context around this problem: how did it arise? Why is it interesting to add
    it to the benchmark?
-->

This problem is interesting because...

### References

<!--
    If the problem arose in a specific context, such as an engineering problem
    or a research paper, put the relevant references here.
-->

1. Foo Bar *et al.*, "...", 2022.
