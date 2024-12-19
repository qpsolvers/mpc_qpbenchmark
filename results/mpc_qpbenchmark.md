# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-12-19 11:21:27.115184+00:00 |
| CPU                | [12th Gen Intel(R) Core(TM) i7-12800H](#cpu-info) |
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

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.7.1                 |
| cvxopt   | 1.3.2                 |
| daqp     | 0.6.0                 |
| ecos     | 2.0.14                |
| gurobi   | 12.0.0 (size-limited) |
| highs    | 1.8.1                 |
| hpipm    | 0.2                   |
| osqp     | 0.6.7.post3           |
| piqp     | 0.4.2                 |
| proxqp   | 0.6.7                 |
| qpalm    | 1.2.5                 |
| qpoases  | 3.2.1                 |
| quadprog | 0.1.13                |
| scs      | 3.2.7                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.4.0.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | 12th Gen Intel(R) Core(TM) i7-12800H |
| `count` | 20 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_lbr`, `arch_perfmon`, `art`, `avx`, `avx2`, `avx_vnni`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `clwb`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `gfni`, `hfi`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `hwp_pkg_req`, `ibpb`, `ibrs`, `ibrs_enhanced`, `ibt`, `ida`, `intel_pt`, `invpcid`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `movdir64b`, `movdiri`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `ospke`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pconfig`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pku`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pts`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `serialize`, `sha`, `sha_ni`, `smap`, `smep`, `smx`, `split_lock_detect`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tme`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tsc_known_freq`, `tscdeadline`, `umip`, `user_shstk`, `vaes`, `vme`, `vmx`, `vnmi`, `vpclmulqdq`, `vpid`, `waitpkg`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `l1_data_cache_size` | 557056 |
| `l1_instruction_cache_size` | 720896 |
| `l2_cache_associativity` | 8 |
| `l2_cache_line_size` | 2048 |
| `l2_cache_size` | 11.5 MiB |
| `l3_cache_size` | 25165824 |
| `model` | 154 |
| `python_version` | 3.11.10.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |        10 |          10     |         10     |         10     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | high_accuracy   | low_accuracy   | mid_accuracy   |
|:---------|:---------------------------------|:----------|:----------------|:---------------|:---------------|
| clarabel | ``tol_feas``                     | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_rel``                  | -         | 0.0             | 0.0            | 0.0            |
| cvxopt   | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``dual_tol``                     | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``primal_tol``                   | -         | 1e-09           | 0.001          | 1e-06          |
| ecos     | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``OptimalityTol``                | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``TimeLimit``                    | 10.0      | 10.0            | 10.0           | 10.0           |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| hpipm    | ``tol_dual_gap``                 | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_eq``                       | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_ineq``                     | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_stat``                     | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| piqp     | ``check_duality_gap``            | -         | True            | True           | True           |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | True            | True           | True           |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| qpalm    | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           | -              |
| qpoases  | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| scs      | ``time_limit_secs``              | 10.0      | 10.0            | 10.0           | 10.0           |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                96.9 |                                289.5 |                                     30601.3 |                                100607.7 |                               189.8 |
| cvxopt   |                                93.8 |                                596.3 |                                     61293.8 |                                201515.4 |                               381.1 |
| daqp     |                                93.8 |                                583.5 |                                     61293.8 |                                201515.4 |                               380.0 |
| ecos     |                                57.8 |                               4476.2 |                                    420907.4 |                               1385605.8 |                              2733.7 |
| gurobi   |                                93.8 |                                586.9 |                                     61293.8 |                                201515.4 |                               380.0 |
| highs    |                                98.4 |                                159.1 |                                     15289.2 |                                 50268.1 |                                95.0 |
| hpipm    |                                87.5 |                                898.4 |                                    241690.7 |                                302724.2 |                               570.8 |
| osqp     |                                96.9 |                                289.2 |                                     31077.4 |                                248968.8 |                               391.2 |
| piqp     |                                95.3 |                                435.8 |                                     45936.1 |                                151024.0 |                               284.8 |
| proxqp   |                               100.0 |                                  4.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                               100.0 |                                  1.0 |                                        37.5 |                                   305.1 |                                28.5 |
| qpoases  |                                93.8 |                                586.0 |                                     61293.8 |                                201515.4 |                               380.0 |
| qpswift  |                                 0.0 |                              13171.9 |                                   1025895.2 |                               3372832.7 |                              6359.6 |
| quadprog |                                93.8 |                                583.3 |                                     61293.8 |                                201515.4 |                               380.0 |
| scs      |                               100.0 |                                  2.3 |                                        50.7 |                                 35612.8 |                               245.2 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                96.9 |                                  2.0 |                                         1.0 |                                     1.3 |                                 3.1 |
| cvxopt   |                                 0.0 |                                  4.1 |                                         2.0 |                                     2.6 |                           2707693.0 |
| daqp     |                                93.8 |                                  4.0 |                                         2.0 |                                     2.6 |                                 1.0 |
| ecos     |                                 0.0 |                                 30.8 |                                        13.5 |                              21205546.7 |                         297710104.3 |
| gurobi   |                                40.6 |                                  4.0 |                                         2.5 |                                   292.9 |                              1639.1 |
| highs    |                                 0.0 |                                  1.1 |                                        13.3 |                                 21228.1 |                            583258.6 |
| hpipm    |                                87.5 |                                  8.2 |                                         4.0 |                                     5.2 |                                 2.8 |
| osqp     |                                89.1 |                                  3.0 |                                         3.0 |                                     8.5 |                                 4.5 |
| piqp     |                                95.3 |                                  3.0 |                                         1.5 |                                     2.1 |                                 4.3 |
| proxqp   |                                98.4 |                                  1.1 |                                         2.1 |                                     5.3 |                                 3.9 |
| qpalm    |                                95.3 |                                  1.0 |                                         1.4 |                                     1.0 |                                 1.5 |
| qpoases  |                                93.8 |                                  4.0 |                                         2.0 |                                     2.6 |                                 1.0 |
| qpswift  |                                 0.0 |                                 90.7 |                                        32.0 |                                    41.6 |                                15.8 |
| quadprog |                                93.8 |                                  4.0 |                                         2.0 |                                     2.6 |                                 1.0 |
| scs      |                                98.4 |                                  1.1 |                                         1.9 |                                     1.6 |                                 1.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                96.9 |                                331.1 |                                1599291539.3 |                               3147029.8 |                             94681.2 |
| cvxopt   |                                90.6 |                                673.9 |                                3198429357.5 |                               6287119.9 |                             69617.7 |
| daqp     |                                93.8 |                                667.6 |                                3659036230.6 |                               6287119.9 |                             18634.0 |
| ecos     |                                25.0 |                               5121.8 |                               21589786080.5 |                              93715469.4 |                           5731623.0 |
| gurobi   |                                93.8 |                                670.5 |                                3198430198.8 |                               6287821.8 |                             18664.9 |
| highs    |                                93.8 |                                 16.5 |                                         1.0 |                                 63377.1 |                           5919821.0 |
| hpipm    |                                87.5 |                               1366.3 |                                6396878704.0 |                              12574279.1 |                             37268.5 |
| osqp     |                                89.1 |                                331.0 |                                5331799443.6 |                              13466472.5 |                            113856.6 |
| piqp     |                               100.0 |                                  5.3 |                                      2199.2 |                               1443786.6 |                             73053.9 |
| proxqp   |                               100.0 |                                  5.0 |                                6994060896.3 |                               1143235.4 |                             84063.4 |
| qpalm    |                                59.4 |                                  1.0 |                                1974303803.7 |                               9342021.0 |                           1340349.4 |
| qpoases  |                               100.0 |                                 15.2 |                                        21.3 |                                     1.0 |                                 1.0 |
| qpswift  |                                 0.0 |                              15071.8 |                               51177268492.7 |                             100598633.6 |                            298158.3 |
| quadprog |                                93.8 |                                667.4 |                                3198429357.5 |                               6287119.9 |                             18634.0 |
| scs      |                               100.0 |                                  1.5 |                                4892662813.8 |                               3434622.9 |                             48266.5 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                96.9 |                                255.0 |                                         2.0 |                                     1.6 |                                 4.2 |
| cvxopt   |                                46.9 |                                518.5 |                                         3.9 |                                     3.1 |                              2736.9 |
| daqp     |                                93.8 |                                514.0 |                                         3.9 |                                     3.1 |                                 1.0 |
| ecos     |                                 4.7 |                               3943.2 |                                        26.6 |                                 25560.6 |                            300816.3 |
| gurobi   |                                90.6 |                                516.1 |                                         3.9 |                                     3.5 |                                 2.7 |
| highs    |                                 0.0 |                                138.8 |                                         1.0 |                                    26.5 |                               618.1 |
| hpipm    |                                87.5 |                               1051.9 |                                         7.9 |                                     6.3 |                                 2.0 |
| osqp     |                                75.0 |                                384.2 |                                         7.3 |                                    14.2 |                                11.5 |
| piqp     |                                96.9 |                                255.1 |                                         2.0 |                                     1.8 |                                 3.2 |
| proxqp   |                                98.4 |                                130.4 |                                         3.7 |                                     2.0 |                                 3.1 |
| qpalm    |                                98.4 |                                  1.0 |                                         1.5 |                                     1.0 |                                 2.3 |
| qpoases  |                                93.8 |                                516.2 |                                         3.9 |                                     3.1 |                                 1.0 |
| qpswift  |                                 0.0 |                              11603.6 |                                        63.0 |                                    50.1 |                                16.0 |
| quadprog |                                93.8 |                                513.8 |                                         3.9 |                                     3.1 |                                 1.0 |
| scs      |                               100.0 |                                  3.6 |                                         5.8 |                                     2.9 |                                 2.7 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        97 |              97 |             97 |             97 |
| cvxopt   |        94 |               0 |             91 |             47 |
| daqp     |        94 |              94 |             94 |             94 |
| ecos     |        58 |               0 |             25 |              5 |
| gurobi   |        94 |              41 |             94 |             91 |
| highs    |        98 |               0 |             94 |              0 |
| hpipm    |        88 |              88 |             88 |             88 |
| osqp     |        97 |              89 |             89 |             75 |
| piqp     |        95 |              95 |            100 |             97 |
| proxqp   |       100 |              98 |            100 |             98 |
| qpalm    |       100 |              95 |             59 |             98 |
| qpoases  |        94 |              94 |            100 |             94 |
| qpswift  |         0 |               0 |              0 |              0 |
| quadprog |        94 |              94 |             94 |             94 |
| scs      |       100 |              98 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |               6 |             97 |             53 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |       100 |              42 |             67 |             47 |
| gurobi   |       100 |              47 |            100 |             97 |
| highs    |       100 |               2 |             94 |              2 |
| hpipm    |        97 |             100 |            100 |            100 |
| osqp     |       100 |              94 |             92 |             80 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              97 |             59 |             98 |
| qpoases  |       100 |             100 |            100 |            100 |
| qpswift  |       100 |             100 |            100 |            100 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     289.5 |             2.0 |          331.1 |          255.0 |
| cvxopt   |     596.3 |             4.1 |          673.9 |          518.5 |
| daqp     |     583.5 |             4.0 |          667.6 |          514.0 |
| ecos     |    4476.2 |            30.8 |         5121.8 |         3943.2 |
| gurobi   |     586.9 |             4.0 |          670.5 |          516.1 |
| highs    |     159.1 |             1.1 |           16.5 |          138.8 |
| hpipm    |     898.4 |             8.2 |         1366.3 |         1051.9 |
| osqp     |     289.2 |             3.0 |          331.0 |          384.2 |
| piqp     |     435.8 |             3.0 |            5.3 |          255.1 |
| proxqp   |       4.4 |             1.1 |            5.0 |          130.4 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| qpoases  |     586.0 |             4.0 |           15.2 |          516.2 |
| qpswift  |   13171.9 |            90.7 |        15071.8 |        11603.6 |
| quadprog |     583.3 |             4.0 |          667.4 |          513.8 |
| scs      |       2.3 |             1.1 |            1.5 |            3.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   30601.3 |             1.0 |   1599291539.3 |            2.0 |
| cvxopt   |   61293.8 |             2.0 |   3198429357.5 |            3.9 |
| daqp     |   61293.8 |             2.0 |   3659036230.6 |            3.9 |
| ecos     |  420907.4 |            13.5 |  21589786080.5 |           26.6 |
| gurobi   |   61293.8 |             2.5 |   3198430198.8 |            3.9 |
| highs    |   15289.2 |            13.3 |            1.0 |            1.0 |
| hpipm    |  241690.7 |             4.0 |   6396878704.0 |            7.9 |
| osqp     |   31077.4 |             3.0 |   5331799443.6 |            7.3 |
| piqp     |   45936.1 |             1.5 |         2199.2 |            2.0 |
| proxqp   |       1.0 |             2.1 |   6994060896.3 |            3.7 |
| qpalm    |      37.5 |             1.4 |   1974303803.7 |            1.5 |
| qpoases  |   61293.8 |             2.0 |           21.3 |            3.9 |
| qpswift  | 1025895.2 |            32.0 |  51177268492.7 |           63.0 |
| quadprog |   61293.8 |             2.0 |   3198429357.5 |            3.9 |
| scs      |      50.7 |             1.9 |   4892662813.8 |            5.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |  100607.7 |             1.3 |      3147029.8 |            1.6 |
| cvxopt   |  201515.4 |             2.6 |      6287119.9 |            3.1 |
| daqp     |  201515.4 |             2.6 |      6287119.9 |            3.1 |
| ecos     | 1385605.8 |      21205546.7 |     93715469.4 |        25560.6 |
| gurobi   |  201515.4 |           292.9 |      6287821.8 |            3.5 |
| highs    |   50268.1 |         21228.1 |        63377.1 |           26.5 |
| hpipm    |  302724.2 |             5.2 |     12574279.1 |            6.3 |
| osqp     |  248968.8 |             8.5 |     13466472.5 |           14.2 |
| piqp     |  151024.0 |             2.1 |      1443786.6 |            1.8 |
| proxqp   |       1.0 |             5.3 |      1143235.4 |            2.0 |
| qpalm    |     305.1 |             1.0 |      9342021.0 |            1.0 |
| qpoases  |  201515.4 |             2.6 |            1.0 |            3.1 |
| qpswift  | 3372832.7 |            41.6 |    100598633.6 |           50.1 |
| quadprog |  201515.4 |             2.6 |      6287119.9 |            3.1 |
| scs      |   35612.8 |             1.6 |      3434622.9 |            2.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     189.8 |             3.1 |        94681.2 |            4.2 |
| cvxopt   |     381.1 |       2707693.0 |        69617.7 |         2736.9 |
| daqp     |     380.0 |             1.0 |        18634.0 |            1.0 |
| ecos     |    2733.7 |     297710104.3 |      5731623.0 |       300816.3 |
| gurobi   |     380.0 |          1639.1 |        18664.9 |            2.7 |
| highs    |      95.0 |        583258.6 |      5919821.0 |          618.1 |
| hpipm    |     570.8 |             2.8 |        37268.5 |            2.0 |
| osqp     |     391.2 |             4.5 |       113856.6 |           11.5 |
| piqp     |     284.8 |             4.3 |        73053.9 |            3.2 |
| proxqp   |       1.0 |             3.9 |        84063.4 |            3.1 |
| qpalm    |      28.5 |             1.5 |      1340349.4 |            2.3 |
| qpoases  |     380.0 |             1.0 |            1.0 |            1.0 |
| qpswift  |    6359.6 |            15.8 |       298158.3 |           16.0 |
| quadprog |     380.0 |             1.0 |        18634.0 |            1.0 |
| scs      |     245.2 |             1.7 |        48266.5 |            2.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
