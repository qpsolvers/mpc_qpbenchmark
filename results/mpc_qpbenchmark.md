# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2026-04-07 17:50:32.554994+00:00 |
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

Problems arising from model predictive control in robotics.

## Solvers

| solver      | version               |
|:------------|:----------------------|
| clarabel    | 0.11.1                |
| cvxopt      | 1.3.3                 |
| daqp        | 0.8.5                 |
| ecos        | 2.0.14                |
| gurobi      | 13.0.1 (size-limited) |
| highs       | 1.14.0                |
| jaxopt_osqp | 0.8.4                 |
| kvxopt      | 1.3.3.1               |
| osqp        | 1.1.1                 |
| piqp        | 0.6.2                 |
| proxqp      | 0.7.2                 |
| qpalm       | 1.2.6                 |
| qpax        | 0.0.10                |
| quadprog    | 0.1.13                |
| scs         | 3.2.11                |

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

| solver      | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel    | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel    | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel    | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt      | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| daqp        | ``dual_tol``                     | -         |           1e-09 |          0.001 |          1e-06 |
| daqp        | ``primal_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| ecos        | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``TimeLimit``                    | 10.0      |          10     |         10     |         10     |
| highs       | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs       | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs       | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| jaxopt_osqp | ``tol``                          | -         |           1e-09 |          0.001 |          1e-06 |
| kvxopt      | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp        | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp        | ``eps_rel``                      | -         |           0     |          0     |          0     |
| osqp        | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| piqp        | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp        | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp        | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp        | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp        | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp      | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp      | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp      | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm       | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| qpalm       | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm       | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| qpax        | ``solver_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| scs         | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs         | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs         | ``time_limit_secs``              | 10.0      |          10     |         10     |         10     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  2.1 |                                         1.0 |                                     1.0 |                                 7.5 |
| cvxopt      |                                93.8 |                                956.4 |                             8408591722842.2 |                             699782933.0 |                             52554.1 |
| daqp        |                               100.0 |                                  1.9 |                                        13.5 |                                   391.2 |                                 1.2 |
| ecos        |                                56.2 |                               7640.7 |                            59925719263422.8 |                            4993371488.4 |                            390629.0 |
| gurobi      |                                93.8 |                                959.1 |                             8408591725724.5 |                             699783015.4 |                             52403.3 |
| highs       |                                 4.7 |                              20219.6 |                           133836468654614.5 |                           11138189000.7 |                            834105.9 |
| jaxopt_osqp |                                93.8 |                               1530.2 |                             8435862724245.5 |                             703823932.1 |                             57504.2 |
| kvxopt      |                                93.8 |                                957.2 |                             8408591722842.2 |                             699782933.0 |                             52554.1 |
| osqp        |                               100.0 |                                  1.7 |                               45725077120.8 |                             513333531.3 |                             27464.9 |
| piqp        |                               100.0 |                                 10.9 |                                         1.0 |                                    12.6 |                                 1.0 |
| proxqp      |                               100.0 |                                  8.3 |                                 137185053.2 |                                  3472.6 |                               137.9 |
| qpalm       |                               100.0 |                                  1.0 |                                5139775881.2 |                               1059439.5 |                              3927.6 |
| qpax        |                                93.8 |                               1223.5 |                             8408591722842.2 |                             699993605.5 |                             53224.2 |
| quadprog    |                                93.8 |                                954.7 |                             8408591722842.2 |                             699782933.0 |                             52403.3 |
| scs         |                               100.0 |                                  4.2 |                                6896944773.5 |                             123672647.5 |                             33821.2 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 2.7 |
| cvxopt      |                                 0.0 |                                501.6 |                                      8796.5 |                                   191.4 |                           2691416.3 |
| daqp        |                                93.8 |                                  1.0 |                                        13.5 |                                102190.6 |                             21442.1 |
| ecos        |                                 0.0 |                               4009.7 |                                     61572.8 |                            1556185883.8 |                         295460817.2 |
| gurobi      |                                39.1 |                                502.7 |                                     11661.5 |                                 21588.9 |                              1632.2 |
| highs       |                                 0.0 |                              11315.1 |                                    140737.2 |                                  3059.5 |                                15.7 |
| jaxopt_osqp |                                 0.0 |                              11315.1 |                                    140737.2 |                                  3059.5 |                                15.7 |
| kvxopt      |                                 0.0 |                                501.6 |                                      8796.5 |                                   191.4 |                           2691416.3 |
| osqp        |                                92.2 |                                630.3 |                                     13264.8 |                                   621.5 |                                 3.1 |
| piqp        |                               100.0 |                                  5.7 |                                         1.0 |                                    43.6 |                                 3.6 |
| proxqp      |                                98.4 |                                133.4 |                                      8280.2 |                                   387.5 |                                 3.8 |
| qpalm       |                                96.9 |                                124.3 |                                      6119.8 |                                    69.4 |                                 1.2 |
| qpax        |                                 0.0 |                              11315.1 |                                    140737.2 |                                  3059.5 |                                15.7 |
| quadprog    |                                93.8 |                                501.0 |                                      8796.5 |                                   191.4 |                                 1.0 |
| scs         |                               100.0 |                                  8.1 |                                      8603.5 |                                    68.2 |                                 1.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.8 |                                         1.3 |                                     1.0 |                               221.6 |
| cvxopt      |                                90.6 |                               1016.7 |                                    569705.3 |                                  6168.8 |                               171.9 |
| daqp        |                               100.0 |                                  2.0 |                                     82042.9 |                                     3.3 |                                 1.0 |
| ecos        |                                23.4 |                               8126.2 |                                   3988012.1 |                                 93390.5 |                             14139.8 |
| gurobi      |                                93.8 |                               1018.5 |                                    569705.5 |                                  6169.5 |                                46.1 |
| highs       |                                 0.0 |                              21022.5 |                                   8545953.9 |                                 92555.1 |                             15295.8 |
| jaxopt_osqp |                                29.7 |                               1561.6 |                                   2325596.5 |                                 40021.9 |                              4301.4 |
| kvxopt      |                                90.6 |                               1016.6 |                                    569705.3 |                                  6168.8 |                               171.9 |
| osqp        |                               100.0 |                                  1.7 |                                    781304.4 |                                  6186.6 |                               118.9 |
| piqp        |                               100.0 |                                  7.0 |                                         1.0 |                                  1111.7 |                               164.8 |
| proxqp      |                               100.0 |                                  8.2 |                                   1245784.5 |                                  1121.7 |                               207.5 |
| qpalm       |                                59.4 |                                  1.0 |                                    351663.6 |                                  9166.5 |                              3308.9 |
| qpax        |                                70.3 |                               1264.9 |                                    569705.3 |                                  7933.7 |                               730.9 |
| quadprog    |                                93.8 |                               1015.4 |                                    569705.3 |                                  6168.8 |                                46.0 |
| scs         |                               100.0 |                                  1.9 |                                    873129.5 |                                  3374.9 |                               119.4 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.9 |                                         1.0 |                                     nan |                                 nan |
| cvxopt      |                                46.9 |                                928.0 |                                   5864062.3 |                                     nan |                                 nan |
| daqp        |                                93.8 |                                  1.9 |                                         9.0 |                                     nan |                                 nan |
| ecos        |                                 6.2 |                               7416.9 |                                  41048433.2 |                                     nan |                                 nan |
| gurobi      |                                90.6 |                                929.7 |                                   5865972.3 |                                     nan |                                 nan |
| highs       |                                 0.0 |                              19621.9 |                                  89450995.3 |                                     nan |                                 nan |
| jaxopt_osqp |                                20.3 |                               9627.6 |                                  67831505.2 |                                     nan |                                 nan |
| kvxopt      |                                46.9 |                                927.9 |                                   5864062.3 |                                     nan |                                 nan |
| osqp        |                                93.8 |                                927.9 |                                  12490646.2 |                                     nan |                                 nan |
| piqp        |                               100.0 |                                  9.2 |                                         1.0 |                                     nan |                                 nan |
| proxqp      |                                98.4 |                                232.3 |                                   5541021.0 |                                     nan |                                 nan |
| qpalm       |                                98.4 |                                  1.0 |                                   2187061.0 |                                     nan |                                 nan |
| qpax        |                                 9.4 |                              13612.2 |                                  67578952.7 |                                     nan |                                 nan |
| quadprog    |                                93.8 |                                926.7 |                                   5864062.3 |                                     nan |                                 nan |
| scs         |                               100.0 |                                  6.0 |                                   8126097.3 |                                     nan |                                 nan |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |        94 |               0 |             91 |             47 |
| daqp        |       100 |              94 |            100 |             94 |
| ecos        |        56 |               0 |             23 |              6 |
| gurobi      |        94 |              39 |             94 |             91 |
| highs       |         5 |               0 |              0 |              0 |
| jaxopt_osqp |        94 |               0 |             30 |             20 |
| kvxopt      |        94 |               0 |             91 |             47 |
| osqp        |       100 |              92 |            100 |             94 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |              98 |            100 |             98 |
| qpalm       |       100 |              97 |             59 |             98 |
| qpax        |        94 |               0 |             70 |              9 |
| quadprog    |        94 |              94 |             94 |             94 |
| scs         |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               6 |             97 |             53 |
| daqp        |       100 |              94 |            100 |             94 |
| ecos        |       100 |              44 |             67 |             50 |
| gurobi      |       100 |              45 |            100 |             97 |
| highs       |       100 |             100 |             94 |             95 |
| jaxopt_osqp |       100 |             100 |             36 |             73 |
| kvxopt      |       100 |               6 |             97 |             53 |
| osqp        |       100 |             100 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |              98 |             59 |             98 |
| qpax        |       100 |             100 |             77 |             81 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       2.1 |             1.1 |            1.8 |            1.9 |
| cvxopt      |     956.4 |           501.6 |         1016.7 |          928.0 |
| daqp        |       1.9 |             1.0 |            2.0 |            1.9 |
| ecos        |    7640.7 |          4009.7 |         8126.2 |         7416.9 |
| gurobi      |     959.1 |           502.7 |         1018.5 |          929.7 |
| highs       |   20219.6 |         11315.1 |        21022.5 |        19621.9 |
| jaxopt_osqp |    1530.2 |         11315.1 |         1561.6 |         9627.6 |
| kvxopt      |     957.2 |           501.6 |         1016.6 |          927.9 |
| osqp        |       1.7 |           630.3 |            1.7 |          927.9 |
| piqp        |      10.9 |             5.7 |            7.0 |            9.2 |
| proxqp      |       8.3 |           133.4 |            8.2 |          232.3 |
| qpalm       |       1.0 |           124.3 |            1.0 |            1.0 |
| qpax        |    1223.5 |         11315.1 |         1264.9 |        13612.2 |
| quadprog    |     954.7 |           501.0 |         1015.4 |          926.7 |
| scs         |       4.2 |             8.1 |            1.9 |            6.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |           default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|------------------:|----------------:|---------------:|---------------:|
| clarabel    |               1.0 |             1.0 |            1.3 |            1.0 |
| cvxopt      |   8408591722842.2 |          8796.5 |       569705.3 |      5864062.3 |
| daqp        |              13.5 |            13.5 |        82042.9 |            9.0 |
| ecos        |  59925719263422.8 |         61572.8 |      3988012.1 |     41048433.2 |
| gurobi      |   8408591725724.5 |         11661.5 |       569705.5 |      5865972.3 |
| highs       | 133836468654614.5 |        140737.2 |      8545953.9 |     89450995.3 |
| jaxopt_osqp |   8435862724245.5 |        140737.2 |      2325596.5 |     67831505.2 |
| kvxopt      |   8408591722842.2 |          8796.5 |       569705.3 |      5864062.3 |
| osqp        |     45725077120.8 |         13264.8 |       781304.4 |     12490646.2 |
| piqp        |               1.0 |             1.0 |            1.0 |            1.0 |
| proxqp      |       137185053.2 |          8280.2 |      1245784.5 |      5541021.0 |
| qpalm       |      5139775881.2 |          6119.8 |       351663.6 |      2187061.0 |
| qpax        |   8408591722842.2 |        140737.2 |       569705.3 |     67578952.7 |
| quadprog    |   8408591722842.2 |          8796.5 |       569705.3 |      5864062.3 |
| scs         |      6896944773.5 |          8603.5 |       873129.5 |      8126097.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|--------------:|----------------:|---------------:|---------------:|
| clarabel    |           1.0 |             1.0 |            1.0 |            nan |
| cvxopt      |   699782933.0 |           191.4 |         6168.8 |            nan |
| daqp        |         391.2 |        102190.6 |            3.3 |            nan |
| ecos        |  4993371488.4 |    1556185883.8 |        93390.5 |            nan |
| gurobi      |   699783015.4 |         21588.9 |         6169.5 |            nan |
| highs       | 11138189000.7 |          3059.5 |        92555.1 |            nan |
| jaxopt_osqp |   703823932.1 |          3059.5 |        40021.9 |            nan |
| kvxopt      |   699782933.0 |           191.4 |         6168.8 |            nan |
| osqp        |   513333531.3 |           621.5 |         6186.6 |            nan |
| piqp        |          12.6 |            43.6 |         1111.7 |            nan |
| proxqp      |        3472.6 |           387.5 |         1121.7 |            nan |
| qpalm       |     1059439.5 |            69.4 |         9166.5 |            nan |
| qpax        |   699993605.5 |          3059.5 |         7933.7 |            nan |
| quadprog    |   699782933.0 |           191.4 |         6168.8 |            nan |
| scs         |   123672647.5 |            68.2 |         3374.9 |            nan |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       7.5 |             2.7 |          221.6 |            nan |
| cvxopt      |   52554.1 |       2691416.3 |          171.9 |            nan |
| daqp        |       1.2 |         21442.1 |            1.0 |            nan |
| ecos        |  390629.0 |     295460817.2 |        14139.8 |            nan |
| gurobi      |   52403.3 |          1632.2 |           46.1 |            nan |
| highs       |  834105.9 |            15.7 |        15295.8 |            nan |
| jaxopt_osqp |   57504.2 |            15.7 |         4301.4 |            nan |
| kvxopt      |   52554.1 |       2691416.3 |          171.9 |            nan |
| osqp        |   27464.9 |             3.1 |          118.9 |            nan |
| piqp        |       1.0 |             3.6 |          164.8 |            nan |
| proxqp      |     137.9 |             3.8 |          207.5 |            nan |
| qpalm       |    3927.6 |             1.2 |         3308.9 |            nan |
| qpax        |   53224.2 |            15.7 |          730.9 |            nan |
| quadprog    |   52403.3 |             1.0 |           46.0 |            nan |
| scs         |   33821.2 |             1.4 |          119.4 |            nan |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
