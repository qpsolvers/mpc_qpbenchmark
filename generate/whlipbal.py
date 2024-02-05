#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
# Copyright 2023 Inria
# SPDX-License-Identifier: Apache-2.0

"""Model predictive control of a wheeled inverted pendulum.

This is one locomotion mode for Upkie: https://github.com/upkie/upkie
"""

import os

import numpy as np
import qpsolvers

try:
    import qpmpc
    from loop_rate_limiters import RateLimiter
    from qpmpc.live_plots import WheeledInvertedPendulumPlot
    from qpmpc.systems import WheeledInvertedPendulum

    if tuple(map(int, (qpmpc.__version__.split(".")))) < (3, 0, 1):
        raise ImportError("Version {qpmpc.__version__} < 3.0.1")
except ImportError as exn:
    raise ImportError(
        "This example requires qpmpc >= 3.0.1 (with extras): "
        "you can install it by `pip install qpmpc[extras]`"
    ) from exn


NB_SUBSTEPS: int = 15  # number of integration substeps


def get_target_states(
    pendulum: WheeledInvertedPendulum, state: np.ndarray, target_vel: float
):
    """Define the reference state trajectory over the receding horizon.

    Args:
        state: Cart-pole state at the beginning of the horizon.
        target_vel: Target ground velocity in m/s.

    Returns:
        Goal state at the end of the horizon.
    """
    nx = pendulum.STATE_DIM
    T = pendulum.sampling_period
    target_states = np.zeros((pendulum.nb_timesteps + 1) * nx)
    for k in range(pendulum.nb_timesteps + 1):
        target_states[k * nx] = state[0] + (k * T) * target_vel
        target_states[k * nx + 2] = target_vel
    return target_states


def save_problem(problem: qpsolvers.Problem, name: str) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.realpath(os.path.join(script_dir, "../data"))
    save_path = f"{data_dir}/{name}.npz"
    print(f"Writing {name} problem to {save_path}...")
    problem.save(save_path)


if __name__ == "__main__":
    pendulum = WheeledInvertedPendulum(
        length=0.58,
        max_ground_accel=10.0,
        nb_timesteps=50,
        sampling_period=0.02,
    )
    live_plot = WheeledInvertedPendulumPlot(pendulum, order="velocities")
    mpc_problem = WheeledInvertedPendulum.build_mpc_problem(
        pendulum,
        terminal_cost_weight=10.0,
        stage_state_cost_weight=1.0,
        stage_input_cost_weight=1e-3,
    )

    dt = pendulum.sampling_period / NB_SUBSTEPS
    rate = RateLimiter(frequency=1.0 / dt, warn=False)
    state = np.zeros(pendulum.STATE_DIM)
    for i in range(30):
        t = i * pendulum.sampling_period
        target_vel = 0.5 + (np.cos(t / 2.0) if True else 0.0)
        target_states = get_target_states(pendulum, state, target_vel)
        mpc_problem.update_initial_state(state)
        mpc_problem.update_goal_state(
            target_states[-WheeledInvertedPendulum.STATE_DIM :]
        )
        mpc_problem.update_target_states(
            target_states[: -WheeledInvertedPendulum.STATE_DIM]
        )
        mpc_qp = qpmpc.MPCQP(mpc_problem, sparse=False)
        save_problem(mpc_qp.problem, f"WHLIPBAL{i}")
        qpsol = qpsolvers.solve_problem(mpc_qp.problem, solver="proxqp")
        plan = qpmpc.Plan(mpc_problem, qpsol)
        for step in range(NB_SUBSTEPS):
            state = pendulum.integrate(state, plan.first_input, dt)
            live_plot.update(
                plan=plan,
                plan_time=t,
                state=state,
                state_time=t + step * dt,
            )
            rate.sleep()
