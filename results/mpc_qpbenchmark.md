# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.7.0 |
| Date               | 2026-07-23 10:03:40.297011+00:00 |
| CPU                | [AMD Ryzen 7 8845HS w/ Radeon 780M Graphics](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |
| Results file       | mpc_qpbenchmark.parquet |
| Results checksum   | sha256:45fbb96de03a9ebc2426fa662c596dd98fd86bd5306cc8efe6fe37daeb496c03 |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Results by settings](#results-by-settings)
    * [Default settings](#default-settings)
    * [High accuracy settings](#high-accuracy-settings)
    * [Low accuracy settings](#low-accuracy-settings)
    * [Mid accuracy settings](#mid-accuracy-settings)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
* [Settings](#settings)
* [Known limitations](#known-limitations)
* [CPU info](#cpu-info)

## Description

Problems arising from model predictive control in robotics.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.11.1                |
| cvxopt   | 1.3.3                 |
| daqp     | 0.8.7                 |
| ecos     | 2.0.14                |
| gurobi   | 13.0.2 (size-limited) |
| highs    | 1.15.1                |
| kvxopt   | 1.3.3.1               |
| osqp     | 1.1.3                 |
| piqp     | 0.6.3                 |
| proxqp   | 0.7.3                 |
| qpalm    | 1.2.6                 |
| quadprog | 0.1.13                |
| scs      | 3.2.11                |
| sip      | 0.0.2                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.13.0.

## Results by settings

### Default settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                93.8 |                                611.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp     |                               100.0 |                                  1.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos     |                                56.2 |                               4869.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| gurobi   |                                93.8 |                                611.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| highs    |                                96.9 |                                304.7 |                                         1.0 |                                     1.0 |                                 1.0 |
| kvxopt   |                                93.8 |                                612.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp     |                               100.0 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                               100.0 |                                  7.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                               100.0 |                                  4.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| quadprog |                                93.8 |                                608.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                               100.0 |                                  2.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                               100.0 |                                  2.4 |                                         1.0 |                                     1.0 |                                 1.0 |

### High accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                 0.0 |                                471.5 |                                         1.0 |                                     1.0 |                            170994.5 |
| daqp     |                                93.8 |                                  1.0 |                                         1.0 |                                    34.3 |                              1363.2 |
| ecos     |                                 0.0 |                               3769.0 |                                         1.0 |                                508639.7 |                          18771596.7 |
| gurobi   |                                39.1 |                                472.6 |                                         1.0 |                                     7.7 |                               103.9 |
| highs    |                                 0.0 |                                235.7 |                                         1.0 |                                   520.5 |                             43288.9 |
| kvxopt   |                                 0.0 |                                471.6 |                                         1.0 |                                     1.0 |                            170994.5 |
| osqp     |                                92.2 |                                592.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                               100.0 |                                  5.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                96.9 |                                233.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                96.9 |                                116.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| quadprog |                                93.8 |                                470.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                               100.0 |                                  7.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                               100.0 |                                  1.8 |                                         1.0 |                                     1.0 |                                 1.0 |

### Low accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                90.6 |                                909.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp     |                               100.0 |                                  1.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos     |                                23.4 |                               7267.3 |                                         1.0 |                                     1.3 |                                19.4 |
| gurobi   |                                93.8 |                                911.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| highs    |                                93.8 |                                  4.1 |                                         1.0 |                                     1.0 |                                20.8 |
| kvxopt   |                                90.6 |                                909.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp     |                               100.0 |                                  1.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                               100.0 |                                  6.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                               100.0 |                                  6.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                59.4 |                                  1.0 |                                         1.0 |                                     1.0 |                                 5.0 |
| quadprog |                                93.8 |                                908.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                               100.0 |                                  1.7 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                               100.0 |                                  2.7 |                                         1.0 |                                     1.0 |                                 1.0 |

### Mid accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                46.9 |                                711.2 |                                         1.0 |                                     1.0 |                               171.4 |
| daqp     |                                93.8 |                                  1.4 |                                         1.0 |                                     1.0 |                                 2.3 |
| ecos     |                                 6.2 |                               5683.5 |                                         1.0 |                                   509.1 |                             18772.0 |
| gurobi   |                                90.6 |                                712.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| highs    |                                 0.0 |                                355.4 |                                         1.0 |                                     1.0 |                                43.4 |
| kvxopt   |                                46.9 |                                711.0 |                                         1.0 |                                     1.0 |                               171.4 |
| osqp     |                                93.8 |                                711.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                               100.0 |                                  7.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                98.4 |                                177.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                98.4 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| quadprog |                                93.8 |                                710.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                               100.0 |                                  4.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                               100.0 |                                  2.4 |                                         1.0 |                                     1.0 |                                 1.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |        94 |               0 |             91 |             47 |
| daqp     |       100 |              94 |            100 |             94 |
| ecos     |        56 |               0 |             23 |              6 |
| gurobi   |        94 |              39 |             94 |             91 |
| highs    |        97 |               0 |             94 |              0 |
| kvxopt   |        94 |               0 |             91 |             47 |
| osqp     |       100 |              92 |            100 |             94 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |              97 |            100 |             98 |
| qpalm    |       100 |              97 |             59 |             98 |
| quadprog |        94 |              94 |             94 |             94 |
| scs      |       100 |             100 |            100 |            100 |
| sip      |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |               6 |             97 |             53 |
| daqp     |       100 |              94 |            100 |             94 |
| ecos     |       100 |              44 |             67 |             50 |
| gurobi   |       100 |              45 |            100 |             97 |
| highs    |       100 |               3 |             94 |              3 |
| kvxopt   |       100 |               6 |             97 |             53 |
| osqp     |       100 |             100 |            100 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              98 |             59 |             98 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |       100 |             100 |            100 |            100 |
| sip      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.4 |             1.0 |            1.6 |            1.4 |
| cvxopt   |     611.1 |           471.5 |          909.1 |          711.2 |
| daqp     |       1.3 |             1.0 |            1.8 |            1.4 |
| ecos     |    4869.1 |          3769.0 |         7267.3 |         5683.5 |
| gurobi   |     611.0 |           472.6 |          911.2 |          712.5 |
| highs    |     304.7 |           235.7 |            4.1 |          355.4 |
| kvxopt   |     612.8 |           471.6 |          909.6 |          711.0 |
| osqp     |       1.2 |           592.6 |            1.8 |          711.3 |
| piqp     |       7.1 |             5.6 |            6.4 |            7.2 |
| proxqp   |       4.8 |           233.5 |            6.9 |          177.5 |
| qpalm    |       1.0 |           116.9 |            1.0 |            1.0 |
| quadprog |     608.4 |           470.9 |          908.0 |          710.1 |
| scs      |       2.3 |             7.2 |            1.7 |            4.5 |
| sip      |       2.4 |             1.8 |            2.7 |            2.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| daqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| ecos     |       1.0 |             1.0 |            1.0 |            1.0 |
| gurobi   |       1.0 |             1.0 |            1.0 |            1.0 |
| highs    |       1.0 |             1.0 |            1.0 |            1.0 |
| kvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| osqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| daqp     |       1.0 |            34.3 |            1.0 |            1.0 |
| ecos     |       1.0 |        508639.7 |            1.3 |          509.1 |
| gurobi   |       1.0 |             7.7 |            1.0 |            1.0 |
| highs    |       1.0 |           520.5 |            1.0 |            1.0 |
| kvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| osqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |        170994.5 |            1.0 |          171.4 |
| daqp     |       1.0 |          1363.2 |            1.0 |            2.3 |
| ecos     |       1.0 |      18771596.7 |           19.4 |        18772.0 |
| gurobi   |       1.0 |           103.9 |            1.0 |            1.0 |
| highs    |       1.0 |         43288.9 |           20.8 |           43.4 |
| kvxopt   |       1.0 |        170994.5 |            1.0 |          171.4 |
| osqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            5.0 |            1.1 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |        10 |          10     |         10     |         10     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| daqp     | ``dual_tol``                     | -         |           1e-09 |          0.001 |          1e-06 |
| daqp     | ``primal_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| ecos     | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``TimeLimit``                    | 10.0      |          10     |         10     |         10     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| kvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| osqp     | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| piqp     | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| qpalm    | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs      | ``time_limit_secs``              | 10.0      |          10     |         10     |         10     |
| sip      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| sip      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| sip      | ``time_limit``                   | 10.0      |          10     |         10     |         10     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | AMD Ryzen 7 8845HS w/ Radeon 780M Graphics |
| `count` | 16 |
| `family` | 25 |
| `flags` | `3dnowext`, `3dnowprefetch`, `abm`, `adx`, `aes`, `amd_lbr_v2`, `aperfmperf`, `apic`, `arat`, `avx`, `avx2`, `avx512_bf16`, `avx512_bitalg`, `avx512_vbmi2`, `avx512_vnni`, `avx512_vpopcntdq`, `avx512bitalg`, `avx512bw`, `avx512cd`, `avx512dq`, `avx512f`, `avx512ifma`, `avx512vbmi`, `avx512vbmi2`, `avx512vl`, `avx512vnni`, `avx512vpopcntdq`, `bmi1`, `bmi2`, `bpext`, `cat_l3`, `cdp_l3`, `clflush`, `clflushopt`, `clwb`, `clzero`, `cmov`, `cmp_legacy`, `constant_tsc`, `cpb`, `cppc`, `cpuid`, `cpuid_fault`, `cqm`, `cqm_llc`, `cqm_mbm_local`, `cqm_mbm_total`, `cqm_occup_llc`, `cr8_legacy`, `cx16`, `cx8`, `dbx`, `de`, `decodeassists`, `erms`, `extapic`, `extd_apicid`, `f16c`, `flush_l1d`, `flushbyasid`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `fxsr_opt`, `gfni`, `ht`, `hw_pstate`, `ibpb`, `ibrs`, `ibrs_enhanced`, `ibs`, `invpcid`, `irperf`, `lahf_lm`, `lbrv`, `lm`, `mba`, `mca`, `mce`, `misalignsse`, `mmx`, `mmxext`, `monitor`, `movbe`, `msr`, `mtrr`, `mwaitx`, `nonstop_tsc`, `nopl`, `npt`, `nrip_save`, `nx`, `ospke`, `osvw`, `osxsave`, `overflow_recov`, `pae`, `pat`, `pausefilter`, `pci_l2i`, `pclmulqdq`, `pdpe1gb`, `perfctr_core`, `perfctr_llc`, `perfctr_nb`, `perfmon_v2`, `pfthreshold`, `pge`, `pku`, `pni`, `popcnt`, `pqe`, `pqm`, `pse`, `pse36`, `rapl`, `rdpid`, `rdpru`, `rdrand`, `rdrnd`, `rdseed`, `rdt_a`, `rdtscp`, `rep_good`, `sep`, `sha`, `sha_ni`, `skinit`, `smap`, `smca`, `smep`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `sse4a`, `ssse3`, `stibp`, `succor`, `svm`, `svm_lock`, `syscall`, `tce`, `topoext`, `tsc`, `tsc_scale`, `umip`, `user_shstk`, `v_spec_ctrl`, `vaes`, `vgif`, `vmcb_clean`, `vme`, `vmmcall`, `vnmi`, `vpclmulqdq`, `wbnoinvd`, `wdt`, `x2apic`, `x2avic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveerptr`, `xsaveopt`, `xsaves`, `xtopology` |
| `l1_data_cache_size` | 262144 |
| `l1_instruction_cache_size` | 262144 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 1024 |
| `l2_cache_size` | 8388608 |
| `l3_cache_size` | 1048576 |
| `model` | 117 |
| `python_version` | 3.14.6.final.0 (64 bit) |
| `stepping` | 2 |
| `vendor_id_raw` | AuthenticAMD |

