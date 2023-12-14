#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
# SPDX-License-Identifier: Apache-2.0

"""Model predictive control test set."""

import os.path
from typing import Iterator

from qpbenchmark.problem import Problem
from qpbenchmark.test_set import TestSet
from qpbenchmark.tolerance import Tolerance


class MpcQpbenchmark(TestSet):
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

    def define_tolerances(self, runtime: float = 10.0) -> None:
        """Define test set tolerances.

        Args:
            runtime: Maximum QP solver runtime in seconds.
        """
        self.tolerances = {
            "default": Tolerance(
                primal=1.0,
                dual=1.0,
                gap=1.0,
                runtime=runtime,
            ),
            "high_accuracy": Tolerance(
                primal=1e-9,
                dual=1e-9,
                gap=1e-9,
                runtime=runtime,
            ),
            "low_accuracy": Tolerance(
                primal=1e-3,
                dual=1e-3,
                gap=1e-3,
                runtime=runtime,
            ),
            "mid_accuracy": Tolerance(
                primal=1e-6,
                dual=1e-6,
                gap=1e-6,
                runtime=runtime,
            ),
        }

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
                yield Problem.load(
                    os.path.join(self.data_dir, fname),
                    name=os.path.basename(fname)[:-4],
                )
