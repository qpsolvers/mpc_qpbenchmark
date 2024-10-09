#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Model predictive control test set."""

import os.path
from typing import Iterator

import qpbenchmark
from qpbenchmark import Problem
from qpbenchmark.benchmark import main


class MpcQpbenchmark(qpbenchmark.TestSet):
    """Model predictive control test set."""

    data_dir: str

    @property
    def description(self) -> str:
        return "Problems arising from model predictive control in robotics."

    @property
    def title(self) -> str:
        return "Model predictive control test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def __init__(self):
        """Initialize test set."""
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        self.data_dir = data_dir
        self.__add_known_solver_issues()
        self.__add_known_solver_timeouts()

    def __add_known_solver_issues(self):
        """See how this is done in the maros_meszaros_qpbenchmark."""

    def __add_known_solver_timeouts(self):
        """See how this is done in the maros_meszaros_qpbenchmark."""

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over test set problems."""
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".npz"):
                yield Problem.load(os.path.join(self.data_dir, fname))


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
