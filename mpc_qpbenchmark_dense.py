#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Dense MPC test set"""

import os.path
from typing import Iterator

from qpbenchmark import Problem
from qpbenchmark.benchmark import main

from mpc_qpbenchmark import MpcQpbenchmark

DENSE_PREFIXES = ("LIPMWALK", "WHLIPBAL")


class MpcQpbenchmarkDense(MpcQpbenchmark):
    """MPC test set restricted to problems with dense Hessians."""

    @property
    def description(self) -> str:
        return (
            "Problems arising from model predictive control in robotics, "
            "restricted to instances with dense cost matrices "
            "(LIPMWALK and WHLIPBAL)."
        )

    @property
    def title(self) -> str:
        return "Model predictive control test set (dense)"

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over dense test set problems."""
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".npz") and fname.startswith(DENSE_PREFIXES):
                yield Problem.load(os.path.join(self.data_dir, fname))


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results_dense.csv",
    )
