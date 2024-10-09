#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""
Generate QUADCMPC problems of the test set.

Make sure you clone submodules in order to run this script.
"""

from os import path

import numpy as np
from qpsolvers import Problem
from quadruped_qp_problems.centroidalMPC import CentroidalQuadruped

DATA_DIR = path.realpath(
    path.join(path.dirname(path.abspath(__file__)), "../data")
)


def generate_problem(name: str, gait: np.ndarray, v_ref: np.ndarray):
    centroidal_problem = CentroidalQuadruped(gait, v_ref)
    problem = Problem(
        P=centroidal_problem.get_P(),
        q=centroidal_problem.get_q(),
        G=centroidal_problem.get_G(),
        h=centroidal_problem.get_h(),
        A=centroidal_problem.get_A(),
        b=centroidal_problem.get_b(),
        lb=centroidal_problem.get_lb(),
        ub=centroidal_problem.get_ub(),
    )
    save_path = f"{DATA_DIR}/{name}.npz"
    print(f"Writing {name} problem to {save_path}...")
    problem.save(save_path)


if __name__ == "__main__":
    generate_problem(
        "QUADCMPC1",
        gait=np.array(
            [
                [8, 1, 0, 0, 1],
                [8, 0, 1, 1, 0],
                [8, 1, 0, 0, 1],
                [8, 0, 1, 1, 0],
            ]
        ),
        v_ref=np.array([0.1, 0.0, 0.0]).reshape((-1, 1)),
    )
    generate_problem(
        "QUADCMPC2",
        gait=np.array(
            [
                [12, 1, 0, 0, 1],
                [12, 0, 1, 1, 0],
            ]
        ),
        v_ref=np.array([0.1, 0.0, 0.0]).reshape((-1, 1)),
    )
    generate_problem(
        "QUADCMPC3",
        gait=np.array([[16, 1, 1, 1, 1]]),
        v_ref=np.zeros((3, 1)),
    )
    generate_problem(
        "QUADCMPC4",
        gait=np.array([[8, 1, 0, 0, 1], [8, 0, 1, 1, 0]]),
        v_ref=np.zeros((3, 1)),
    )
