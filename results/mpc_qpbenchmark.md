# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-12-09 17:05:37.261039+00:00 |
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
| clarabel | 0.9.0                 |
| cvxopt   | 1.3.2                 |
| daqp     | 0.5.1.post1           |
| ecos     | 2.0.14                |
| gurobi   | 11.0.3 (size-limited) |
| highs    | 1.7.2                 |
| hpipm    | 0.2                   |
| osqp     | 0.6.7.post0           |
| piqp     | 0.4.2                 |
| proxqp   | 0.6.7                 |
| qpalm    | 1.2.3                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.12                |
| scs      | 3.2.7                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.3.3.

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
| `l2_cache_associativity` | 7 |
| `l2_cache_line_size` | 1280 |
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
| proxqp   | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
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
| clarabel |                                93.8 |                                748.8 |                                     61294.2 |                          862419665105.5 |                       17950502204.1 |
| cvxopt   |                                95.3 |                                595.9 |                                     45936.4 |                          646332883862.9 |                       13502494531.5 |
| daqp     |                               100.0 |                                 28.8 |                                      1546.6 |                                     1.0 |                                 1.0 |
| ecos     |                                57.8 |                               5739.4 |                                    420910.4 |                         5929937018188.9 |                      129128586020.9 |
| gurobi   |                                93.8 |                                751.7 |                                     61294.2 |                          862419765203.1 |                       17947932483.6 |
| highs    |                                98.4 |                                203.3 |                                     15289.3 |                          215130905960.8 |                        4488037476.2 |
| hpipm    |                                87.5 |                               1171.1 |                                    255865.4 |                         1295559826350.3 |                       26962024721.6 |
| osqp     |                               100.0 |                                  1.1 |                                       375.5 |                          633394827887.4 |                       10951932554.9 |
| piqp     |                                96.9 |                                373.7 |                                     30601.5 |                          430567894981.5 |                        8961869808.3 |
| proxqp   |                               100.0 |                                  5.9 |                                         1.0 |                               4279646.3 |                          47235377.5 |
| qpalm    |                               100.0 |                                  1.0 |                                        37.5 |                            1305627642.7 |                        1345182549.9 |
| qpoases  |                                93.8 |                                751.0 |                                     61294.2 |                          862419663882.4 |                       17947901222.9 |
| qpswift  |                                46.9 |                               7517.2 |                                    532826.3 |                         7496952363882.5 |                      156023402116.7 |
| quadprog |                                96.9 |                                371.1 |                                     30601.5 |                          430567665437.9 |                        8960586420.9 |
| scs      |                               100.0 |                                  3.0 |                                        50.7 |                          152411111391.4 |                       11582998896.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                93.8 |                                 26.0 |                                         2.0 |                                   905.2 |                                67.8 |
| cvxopt   |                                 0.0 |                                 20.0 |                                         1.5 |                                   677.3 |                          51366746.3 |
| daqp     |                                96.9 |                                  1.0 |                                        81.8 |                                     1.0 |                                 1.0 |
| ecos     |                                 0.0 |                                199.3 |                                        13.5 |                            7357237255.0 |                        5647754491.5 |
| gurobi   |                                40.6 |                                 26.1 |                                         2.5 |                                101622.3 |                             31094.0 |
| highs    |                                 0.0 |                                  7.1 |                                        13.3 |                               7364918.2 |                          11063790.7 |
| hpipm    |                                87.5 |                                 53.1 |                                         4.0 |                                  1809.5 |                                53.8 |
| osqp     |                                85.9 |                                 32.7 |                                         3.1 |                                  3402.6 |                                94.1 |
| piqp     |                                95.3 |                                 19.4 |                                         1.5 |                                   833.2 |                                82.4 |
| proxqp   |                                98.4 |                                  7.4 |                                         1.9 |                                  1828.1 |                                73.4 |
| qpalm    |                                95.3 |                                  6.4 |                                         1.4 |                                   346.9 |                                29.0 |
| qpoases  |                                93.8 |                                 26.2 |                                         2.0 |                                   904.1 |                                19.0 |
| qpswift  |                                 0.0 |                                261.0 |                                        17.0 |                                  8084.7 |                              3377.3 |
| quadprog |                                96.9 |                                 12.9 |                                         1.0 |                                   452.1 |                                 9.7 |
| scs      |                                98.4 |                                  7.1 |                                         1.9 |                                   550.5 |                                31.9 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                93.8 |                                879.8 |                                2513051638.0 |                             902121763.3 |                         102478459.9 |
| cvxopt   |                                96.9 |                                 36.5 |                                        18.6 |                              18067746.4 |                          50425085.1 |
| daqp     |                                96.9 |                                 30.7 |                             3456902242332.7 |                                     1.0 |                                 1.0 |
| ecos     |                                25.0 |                               6744.3 |                               16963403349.0 |                           13446968382.4 |                        5668845375.1 |
| gurobi   |                                93.8 |                                882.2 |                                2513052299.1 |                             902221821.4 |                          18460428.6 |
| highs    |                                93.8 |                                 21.2 |                                         1.0 |                               9093401.5 |                        5854988138.2 |
| hpipm    |                                87.5 |                               1798.7 |                                5026118981.7 |                            1804247847.7 |                          36860309.2 |
| osqp     |                                87.5 |                                  1.5 |                                4251509865.0 |                            1563792743.4 |                         381352542.8 |
| piqp     |                               100.0 |                                  7.8 |                                      1649.6 |                             201031732.8 |                          72210185.1 |
| proxqp   |                               100.0 |                                  6.7 |                                5495333269.1 |                             164039604.4 |                          83142616.0 |
| qpalm    |                                59.4 |                                  1.0 |                                1551238702.9 |                            1340460243.9 |                        1325668752.7 |
| qpoases  |                               100.0 |                                 19.9 |                                        16.9 |                                   143.4 |                               989.0 |
| qpswift  |                                46.9 |                               8834.3 |                               21361439551.0 |                            7668458670.2 |                         160006360.8 |
| quadprog |                                96.9 |                                435.9 |                                1256523855.8 |                             451059846.6 |                           9214947.4 |
| scs      |                               100.0 |                                  1.9 |                                3844235068.0 |                             492824345.9 |                          47737873.8 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                93.8 |                                725.7 |                                         3.9 |                                902456.0 |                             84062.5 |
| cvxopt   |                                48.4 |                                545.4 |                                         3.0 |                                676623.2 |                          51380813.7 |
| daqp     |                                98.4 |                                 26.7 |                                     94926.2 |                                     1.0 |                                 1.0 |
| ecos     |                                 4.7 |                               5562.3 |                                        26.6 |                            7363321078.1 |                        5647881334.2 |
| gurobi   |                                90.6 |                                727.6 |                                         3.9 |                               1002883.5 |                             49850.2 |
| highs    |                                 0.0 |                                195.2 |                                         1.0 |                               7637187.9 |                          11603384.1 |
| hpipm    |                                87.5 |                               1483.6 |                                         7.9 |                               1804334.9 |                             37904.6 |
| osqp     |                                73.4 |                                726.5 |                                         8.3 |                               4329012.0 |                            220937.2 |
| piqp     |                                96.9 |                                360.1 |                                         2.0 |                                533787.1 |                             61048.3 |
| proxqp   |                                98.4 |                                183.1 |                                         3.7 |                                562543.7 |                             58525.9 |
| qpalm    |                                98.4 |                                  1.0 |                                         1.5 |                                288073.6 |                             43403.1 |
| qpoases  |                                93.8 |                                727.9 |                                         3.9 |                                902164.6 |                             18775.2 |
| qpswift  |                                 0.0 |                               7286.2 |                                        33.5 |                               7917976.0 |                           3570286.6 |
| quadprog |                                96.9 |                                359.5 |                                         2.0 |                                451082.6 |                              9387.9 |
| scs      |                               100.0 |                                  5.3 |                                         5.8 |                                831360.6 |                             50948.3 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        94 |              94 |             94 |             94 |
| cvxopt   |        95 |               0 |             97 |             48 |
| daqp     |       100 |              97 |             97 |             98 |
| ecos     |        58 |               0 |             25 |              5 |
| gurobi   |        94 |              41 |             94 |             91 |
| highs    |        98 |               0 |             94 |              0 |
| hpipm    |        88 |              88 |             88 |             88 |
| osqp     |       100 |              86 |             88 |             73 |
| piqp     |        97 |              95 |            100 |             97 |
| proxqp   |       100 |              98 |            100 |             98 |
| qpalm    |       100 |              95 |             59 |             98 |
| qpoases  |        94 |              94 |            100 |             94 |
| qpswift  |        47 |               0 |             47 |              0 |
| quadprog |        97 |              97 |             97 |             97 |
| scs      |       100 |              98 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |               5 |             97 |             53 |
| daqp     |       100 |              97 |             97 |             98 |
| ecos     |       100 |              42 |             67 |             47 |
| gurobi   |       100 |              47 |            100 |             97 |
| highs    |       100 |               2 |             94 |              2 |
| hpipm    |        97 |             100 |            100 |            100 |
| osqp     |       100 |              94 |             88 |             80 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              97 |             59 |             98 |
| qpoases  |       100 |             100 |            100 |            100 |
| qpswift  |       100 |              53 |            100 |             53 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     748.8 |            26.0 |          879.8 |          725.7 |
| cvxopt   |     595.9 |            20.0 |           36.5 |          545.4 |
| daqp     |      28.8 |             1.0 |           30.7 |           26.7 |
| ecos     |    5739.4 |           199.3 |         6744.3 |         5562.3 |
| gurobi   |     751.7 |            26.1 |          882.2 |          727.6 |
| highs    |     203.3 |             7.1 |           21.2 |          195.2 |
| hpipm    |    1171.1 |            53.1 |         1798.7 |         1483.6 |
| osqp     |       1.1 |            32.7 |            1.5 |          726.5 |
| piqp     |     373.7 |            19.4 |            7.8 |          360.1 |
| proxqp   |       5.9 |             7.4 |            6.7 |          183.1 |
| qpalm    |       1.0 |             6.4 |            1.0 |            1.0 |
| qpoases  |     751.0 |            26.2 |           19.9 |          727.9 |
| qpswift  |    7517.2 |           261.0 |         8834.3 |         7286.2 |
| quadprog |     371.1 |            12.9 |          435.9 |          359.5 |
| scs      |       3.0 |             7.1 |            1.9 |            5.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |    low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|----------------:|---------------:|
| clarabel |   61294.2 |             2.0 |    2513051638.0 |            3.9 |
| cvxopt   |   45936.4 |             1.5 |            18.6 |            3.0 |
| daqp     |    1546.6 |            81.8 | 3456902242332.7 |        94926.2 |
| ecos     |  420910.4 |            13.5 |   16963403349.0 |           26.6 |
| gurobi   |   61294.2 |             2.5 |    2513052299.1 |            3.9 |
| highs    |   15289.3 |            13.3 |             1.0 |            1.0 |
| hpipm    |  255865.4 |             4.0 |    5026118981.7 |            7.9 |
| osqp     |     375.5 |             3.1 |    4251509865.0 |            8.3 |
| piqp     |   30601.5 |             1.5 |          1649.6 |            2.0 |
| proxqp   |       1.0 |             1.9 |    5495333269.1 |            3.7 |
| qpalm    |      37.5 |             1.4 |    1551238702.9 |            1.5 |
| qpoases  |   61294.2 |             2.0 |            16.9 |            3.9 |
| qpswift  |  532826.3 |            17.0 |   21361439551.0 |           33.5 |
| quadprog |   30601.5 |             1.0 |    1256523855.8 |            2.0 |
| scs      |      50.7 |             1.9 |    3844235068.0 |            5.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |         default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------------:|----------------:|---------------:|---------------:|
| clarabel |  862419665105.5 |           905.2 |    902121763.3 |       902456.0 |
| cvxopt   |  646332883862.9 |           677.3 |     18067746.4 |       676623.2 |
| daqp     |             1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 5929937018188.9 |    7357237255.0 |  13446968382.4 |   7363321078.1 |
| gurobi   |  862419765203.1 |        101622.3 |    902221821.4 |      1002883.5 |
| highs    |  215130905960.8 |       7364918.2 |      9093401.5 |      7637187.9 |
| hpipm    | 1295559826350.3 |          1809.5 |   1804247847.7 |      1804334.9 |
| osqp     |  633394827887.4 |          3402.6 |   1563792743.4 |      4329012.0 |
| piqp     |  430567894981.5 |           833.2 |    201031732.8 |       533787.1 |
| proxqp   |       4279646.3 |          1828.1 |    164039604.4 |       562543.7 |
| qpalm    |    1305627642.7 |           346.9 |   1340460243.9 |       288073.6 |
| qpoases  |  862419663882.4 |           904.1 |          143.4 |       902164.6 |
| qpswift  | 7496952363882.5 |          8084.7 |   7668458670.2 |      7917976.0 |
| quadprog |  430567665437.9 |           452.1 |    451059846.6 |       451082.6 |
| scs      |  152411111391.4 |           550.5 |    492824345.9 |       831360.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|---------------:|----------------:|---------------:|---------------:|
| clarabel |  17950502204.1 |            67.8 |    102478459.9 |        84062.5 |
| cvxopt   |  13502494531.5 |      51366746.3 |     50425085.1 |     51380813.7 |
| daqp     |            1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 129128586020.9 |    5647754491.5 |   5668845375.1 |   5647881334.2 |
| gurobi   |  17947932483.6 |         31094.0 |     18460428.6 |        49850.2 |
| highs    |   4488037476.2 |      11063790.7 |   5854988138.2 |     11603384.1 |
| hpipm    |  26962024721.6 |            53.8 |     36860309.2 |        37904.6 |
| osqp     |  10951932554.9 |            94.1 |    381352542.8 |       220937.2 |
| piqp     |   8961869808.3 |            82.4 |     72210185.1 |        61048.3 |
| proxqp   |     47235377.5 |            73.4 |     83142616.0 |        58525.9 |
| qpalm    |   1345182549.9 |            29.0 |   1325668752.7 |        43403.1 |
| qpoases  |  17947901222.9 |            19.0 |          989.0 |        18775.2 |
| qpswift  | 156023402116.7 |          3377.3 |    160006360.8 |      3570286.6 |
| quadprog |   8960586420.9 |             9.7 |      9214947.4 |         9387.9 |
| scs      |  11582998896.4 |            31.9 |     47737873.8 |        50948.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
