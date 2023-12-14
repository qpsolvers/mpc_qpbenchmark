---
name: Submit a new problem
about: Propose a new problem for the MPC test set
title: ''
labels: ''
assignees: ''
---

### Problem

I propose to add the following problems to the MPC test set. The problems can be generated as follows:

<!--
    Make sure you fill out the <FIELDS>:

    - COPYRIGHT_HOLDER: you or your employer
    - DESCRIPTION: Describe your problem for interested readers.
    - PROBLEM_CODE: Name your problem in up to eight capital letters.
-->

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 <COPYRIGHT_HOLDER>
# SPDX-License-Identifier: Apache-2.0

"""<DESCRIPTION>"""

from os import path

from qpbenchmark.problem import Problem

if __name__ == "__main__":
    problem = Problem(
        P=...,
        q=...,
        G=..,
        h=..,
        A=...,
        b=...,
        lb=...,
        ub=...,
        name="<PROBLEM_CODE>",
    )
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    problem.save(f"{data_dir}/{problem.name}.npz")
```

### Context

<!--
    Context around this problem: how did it arise? Why is it interesting to add
    it to the benchmark?
-->

These problems arose from model predictive control of...

### References

<!--
    If the problem arose in a specific context, such as an engineering problem
    or a research paper, put the relevant references here.
-->

1. Foo Bar *et al.*, "...", 2022.
