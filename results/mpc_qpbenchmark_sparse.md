# Model predictive control test set (sparse)

| Number of problems | 4 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2026-04-07 18:05:51.078798+00:00 |
| CPU                | [AMD Ryzen 7 8845HS w/ Radeon 780M Graphics](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
    * [Mid accuracy](#mid-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)

## Description

Problems arising from model predictive control in robotics, restricted to instances with sparse cost matrices (QUADCMPC).

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.11.1                |
| cvxopt   | 1.3.3                 |
| gurobi   | 13.0.1 (size-limited) |
| highs    | 1.14.0                |
| kvxopt   | 1.3.3.1               |
| osqp     | 1.1.1                 |
| piqp     | 0.6.2                 |
| proxqp   | 0.7.2                 |
| qpalm    | 1.2.6                 |
| scs      | 3.2.11                |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.10.0.

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
| `python_version` | 3.14.3.final.0 (64 bit) |
| `stepping` | 2 |
| `vendor_id_raw` | AuthenticAMD |

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

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                 0.0 |                               2529.9 |                           562949953421313.0 |                           58451869320.0 |                         571082742.8 |
| gurobi   |                                 0.0 |                               2529.9 |                           562949953421313.0 |                           58451869320.0 |                         571082742.8 |
| highs    |                                75.0 |                                522.9 |                           135748005151019.0 |                           14094966907.1 |                         137927645.4 |
| kvxopt   |                                 0.0 |                               2529.9 |                           562949953421313.0 |                           58451869320.0 |                         571082742.8 |
| osqp     |                               100.0 |                                  1.0 |                             1716385612685.0 |                                271327.8 |                            174044.8 |
| piqp     |                               100.0 |                                 20.0 |                                         6.0 |                                    83.7 |                                 1.2 |
| proxqp   |                               100.0 |                                 14.4 |                                1552581870.0 |                                213908.8 |                            710141.3 |
| qpalm    |                               100.0 |                                  1.0 |                              273576056623.0 |                                849112.5 |                            541560.6 |
| scs      |                               100.0 |                                  5.3 |                              152239032446.0 |                                120963.8 |                             17772.8 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    27.2 |                              4841.9 |
| cvxopt   |                                 0.0 |                               1888.6 |                                    562951.0 |                                 14434.6 |                             51177.4 |
| gurobi   |                                 0.0 |                               1888.6 |                                    562951.0 |                                 14434.6 |                             51177.4 |
| highs    |                                 0.0 |                               1888.6 |                                    562951.0 |                                 14434.6 |                             51177.4 |
| kvxopt   |                                 0.0 |                               1888.6 |                                    562951.0 |                                 14434.6 |                             51177.4 |
| osqp     |                                 0.0 |                               1888.6 |                                    562951.0 |                                 14434.6 |                             51177.4 |
| piqp     |                               100.0 |                                 28.1 |                                         1.0 |                                  1417.1 |                              6028.1 |
| proxqp   |                                75.0 |                                390.3 |                                    168866.0 |                                  3692.7 |                             23916.7 |
| qpalm    |                               100.0 |                                  2.0 |                                    247489.0 |                                     1.0 |                                 1.0 |
| scs      |                               100.0 |                                 18.3 |                                    502236.0 |                                     3.4 |                             24181.5 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.3 |                                     81241.9 |                                     1.0 |                                 5.6 |
| cvxopt   |                                 0.0 |                               3512.7 |                               35184372088.8 |                                  6197.2 |                                21.8 |
| gurobi   |                                 0.0 |                               3512.7 |                               35184372088.8 |                                  6197.2 |                                21.8 |
| highs    |                                 0.0 |                                 45.7 |                                         1.0 |                                    18.6 |                              7036.3 |
| kvxopt   |                                 0.0 |                               3512.7 |                               35184372088.8 |                                  6197.2 |                                21.8 |
| osqp     |                               100.0 |                                  1.5 |                               14080910258.8 |                                    14.3 |                                 7.8 |
| piqp     |                               100.0 |                                113.5 |                                     61751.2 |                                   636.4 |                                 4.0 |
| proxqp   |                               100.0 |                                 22.1 |                                  97028399.7 |                                     4.2 |                                 1.0 |
| qpalm    |                                75.0 |                                  1.0 |                               17098503538.9 |                                    90.0 |                                20.7 |
| scs      |                               100.0 |                                  1.7 |                                9267168387.2 |                                  1191.8 |                                18.6 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.3 |
| cvxopt   |                                 0.0 |                               2467.9 |                                   8529544.7 |                                 19240.2 |                                 6.1 |
| gurobi   |                                 0.0 |                               2467.9 |                                   8529544.7 |                                 19240.2 |                                 6.1 |
| highs    |                                 0.0 |                                502.1 |                                   2167368.4 |                                 26658.9 |                              2453.2 |
| kvxopt   |                                 0.0 |                               2467.9 |                                   8529544.7 |                                 19240.2 |                                 6.1 |
| osqp     |                                25.0 |                               1683.1 |                                   8523196.7 |                                 14430.2 |                                 4.6 |
| piqp     |                               100.0 |                                 37.3 |                                         1.0 |                                  2017.0 |                                 1.0 |
| proxqp   |                                75.0 |                                476.2 |                                   2217327.4 |                                  5209.3 |                                 3.1 |
| qpalm    |                               100.0 |                                  1.0 |                                   1761193.8 |                                  2288.2 |                                 1.4 |
| scs      |                               100.0 |                                  9.0 |                                   4426330.1 |                                     5.8 |                                 1.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |         0 |               0 |              0 |              0 |
| gurobi   |         0 |               0 |              0 |              0 |
| highs    |        75 |               0 |              0 |              0 |
| kvxopt   |         0 |               0 |              0 |              0 |
| osqp     |       100 |               0 |            100 |             25 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |              75 |            100 |             75 |
| qpalm    |       100 |             100 |             75 |            100 |
| scs      |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |             100 |            100 |            100 |
| gurobi   |       100 |             100 |            100 |            100 |
| highs    |       100 |             100 |              0 |             25 |
| kvxopt   |       100 |             100 |            100 |            100 |
| osqp     |       100 |             100 |            100 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |             100 |             75 |            100 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.4 |             1.0 |            1.3 |            1.2 |
| cvxopt   |    2529.9 |          1888.6 |         3512.7 |         2467.9 |
| gurobi   |    2529.9 |          1888.6 |         3512.7 |         2467.9 |
| highs    |     522.9 |          1888.6 |           45.7 |          502.1 |
| kvxopt   |    2529.9 |          1888.6 |         3512.7 |         2467.9 |
| osqp     |       1.0 |          1888.6 |            1.5 |         1683.1 |
| piqp     |      20.0 |            28.1 |          113.5 |           37.3 |
| proxqp   |      14.4 |           390.3 |           22.1 |          476.2 |
| qpalm    |       1.0 |             2.0 |            1.0 |            1.0 |
| scs      |       5.3 |            18.3 |            1.7 |            9.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |           default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|------------------:|----------------:|---------------:|---------------:|
| clarabel |               1.0 |             1.0 |        81241.9 |            1.0 |
| cvxopt   | 562949953421313.0 |        562951.0 |  35184372088.8 |      8529544.7 |
| gurobi   | 562949953421313.0 |        562951.0 |  35184372088.8 |      8529544.7 |
| highs    | 135748005151019.0 |        562951.0 |            1.0 |      2167368.4 |
| kvxopt   | 562949953421313.0 |        562951.0 |  35184372088.8 |      8529544.7 |
| osqp     |   1716385612685.0 |        562951.0 |  14080910258.8 |      8523196.7 |
| piqp     |               6.0 |             1.0 |        61751.2 |            1.0 |
| proxqp   |      1552581870.0 |        168866.0 |     97028399.7 |      2217327.4 |
| qpalm    |    273576056623.0 |        247489.0 |  17098503538.9 |      1761193.8 |
| scs      |    152239032446.0 |        502236.0 |   9267168387.2 |      4426330.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel |           1.0 |            27.2 |            1.0 |            1.0 |
| cvxopt   | 58451869320.0 |         14434.6 |         6197.2 |        19240.2 |
| gurobi   | 58451869320.0 |         14434.6 |         6197.2 |        19240.2 |
| highs    | 14094966907.1 |         14434.6 |           18.6 |        26658.9 |
| kvxopt   | 58451869320.0 |         14434.6 |         6197.2 |        19240.2 |
| osqp     |      271327.8 |         14434.6 |           14.3 |        14430.2 |
| piqp     |          83.7 |          1417.1 |          636.4 |         2017.0 |
| proxqp   |      213908.8 |          3692.7 |            4.2 |         5209.3 |
| qpalm    |      849112.5 |             1.0 |           90.0 |         2288.2 |
| scs      |      120963.8 |             3.4 |         1191.8 |            5.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |     default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|------------:|----------------:|---------------:|---------------:|
| clarabel |         1.0 |          4841.9 |            5.6 |            1.3 |
| cvxopt   | 571082742.8 |         51177.4 |           21.8 |            6.1 |
| gurobi   | 571082742.8 |         51177.4 |           21.8 |            6.1 |
| highs    | 137927645.4 |         51177.4 |         7036.3 |         2453.2 |
| kvxopt   | 571082742.8 |         51177.4 |           21.8 |            6.1 |
| osqp     |    174044.8 |         51177.4 |            7.8 |            4.6 |
| piqp     |         1.2 |          6028.1 |            4.0 |            1.0 |
| proxqp   |    710141.3 |         23916.7 |            1.0 |            3.1 |
| qpalm    |    541560.6 |             1.0 |           20.7 |            1.4 |
| scs      |     17772.8 |         24181.5 |           18.6 |            1.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
