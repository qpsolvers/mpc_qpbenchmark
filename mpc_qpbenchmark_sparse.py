#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Sparse MPC test set."""

import os.path
from typing import Iterator

from qpbenchmark import Problem
from qpbenchmark.benchmark import main

from mpc_qpbenchmark import MpcQpbenchmark

SPARSE_PREFIXES = ("QUADCMPC",)


class MpcQpbenchmarkSparse(MpcQpbenchmark):
    """MPC test set restricted to problems with sparse Hessians."""

    @property
    def description(self) -> str:
        return (
            "Problems arising from model predictive control in robotics, "
            "restricted to instances with sparse cost matrices (QUADCMPC)."
        )

    @property
    def title(self) -> str:
        return "Model predictive control test set (sparse)"

    @property
    def sparse_only(self) -> bool:
        return True

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over sparse test set problems."""
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".npz") and fname.startswith(SPARSE_PREFIXES):
                yield Problem.load(os.path.join(self.data_dir, fname))


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results_sparse.csv",
    )
