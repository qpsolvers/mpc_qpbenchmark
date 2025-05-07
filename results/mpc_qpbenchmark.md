# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2025-05-07 17:59:09.145836+00:00 |
| CPU                | [11th Gen Intel(R) Core(TM) i9-11900KF @ 3.50GHz](#cpu-info) |
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
| clarabel    | 0.10.0                |
| cvxopt      | 1.3.2                 |
| daqp        | 0.6.0                 |
| ecos        | 2.0.14                |
| gurobi      | 12.0.2 (size-limited) |
| highs       | 1.10.0                |
| jaxopt_osqp | 0.8.4                 |
| kvxopt      | 1.3.2.1               |
| osqp        | 0.6.7.post3           |
| piqp        | 0.4.2                 |
| proxqp      | 0.7.2                 |
| qpalm       | 1.2.5                 |
| qpax        | 0.0.9                 |
| qpswift     | 1.0.0                 |
| quadprog    | 0.1.13                |
| scs         | 3.2.7.post2           |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.6.0.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | 11th Gen Intel(R) Core(TM) i9-11900KF @ 3.50GHz |
| `count` | 16 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `avx512_bitalg`, `avx512_vbmi2`, `avx512_vnni`, `avx512_vpopcntdq`, `avx512bitalg`, `avx512bw`, `avx512cd`, `avx512dq`, `avx512f`, `avx512ifma`, `avx512vbmi`, `avx512vbmi2`, `avx512vl`, `avx512vnni`, `avx512vpopcntdq`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `gfni`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `hwp_pkg_req`, `ibpb`, `ibrs`, `ibrs_enhanced`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `ospke`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pku`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pts`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sha`, `sha_ni`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tsc_known_freq`, `tscdeadline`, `umip`, `vaes`, `vme`, `vmx`, `vnmi`, `vpclmulqdq`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `l1_data_cache_size` | 393216 |
| `l1_instruction_cache_size` | 262144 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 4194304 |
| `l3_cache_size` | 16777216 |
| `model` | 167 |
| `python_version` | 3.12.10.final.0 (64 bit) |
| `stepping` | 1 |
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

| solver      | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel    | ``tol_feas``                     | -         |     1e-09       |     0.001      |    1e-06       |
| clarabel    | ``tol_gap_abs``                  | -         |     1e-09       |     0.001      |    1e-06       |
| clarabel    | ``tol_gap_rel``                  | -         |     0           |     0          |    0           |
| cvxopt      | ``feastol``                      | -         |     1e-09       |     0.001      |    1e-06       |
| daqp        | ``dual_tol``                     | -         |     1e-09       |     0.001      |    1e-06       |
| daqp        | ``primal_tol``                   | -         |     1e-09       |     0.001      |    1e-06       |
| ecos        | ``feastol``                      | -         |     1e-09       |     0.001      |    1e-06       |
| gurobi      | ``FeasibilityTol``               | -         |     1e-09       |     0.001      |    1e-06       |
| gurobi      | ``OptimalityTol``                | -         |     1e-09       |     0.001      |    1e-06       |
| gurobi      | ``TimeLimit``                    | 10.0      |    10           |    10          |   10           |
| highs       | ``dual_feasibility_tolerance``   | -         |     1e-09       |     0.001      |    1e-06       |
| highs       | ``primal_feasibility_tolerance`` | -         |     1e-09       |     0.001      |    1e-06       |
| highs       | ``time_limit``                   | 10.0      |    10           |    10          |   10           |
| jaxopt_osqp | ``tol``                          | -         |     1e-09       |     0.001      |    1e-06       |
| kvxopt      | ``feastol``                      | -         |     1e-09       |     0.001      |    1e-06       |
| osqp        | ``eps_abs``                      | -         |     1e-09       |     0.001      |    1e-06       |
| osqp        | ``eps_rel``                      | -         |     0           |     0          |    0           |
| osqp        | ``time_limit``                   | 10.0      |    10           |    10          |   10           |
| piqp        | ``check_duality_gap``            | -         |     1           |     1          |    1           |
| piqp        | ``eps_abs``                      | -         |     1e-09       |     0.001      |    1e-06       |
| piqp        | ``eps_duality_gap_abs``          | -         |     1e-09       |     0.001      |    1e-06       |
| piqp        | ``eps_duality_gap_rel``          | -         |     0           |     0          |    0           |
| piqp        | ``eps_rel``                      | -         |     0           |     0          |    0           |
| proxqp      | ``check_duality_gap``            | -         |     1           |     1          |    1           |
| proxqp      | ``eps_abs``                      | -         |     1e-09       |     0.001      |    1e-06       |
| proxqp      | ``eps_duality_gap_abs``          | -         |     1e-09       |     0.001      |    1e-06       |
| proxqp      | ``eps_duality_gap_rel``          | -         |     0           |     0          |    0           |
| proxqp      | ``eps_rel``                      | -         |     0           |     0          |    0           |
| qpalm       | ``eps_abs``                      | -         |     1e-09       |     0.001      |    1e-06       |
| qpalm       | ``eps_rel``                      | -         |     0           |     0          |    0           |
| qpalm       | ``time_limit``                   | 10.0      |    10           |    10          |   10           |
| qpax        | ``solver_tol``                   | -         |     1e-09       |     0.001      |    1e-06       |
| qpswift     | ``RELTOL``                       | -         |     1.73205e-09 |     0.00173205 |    1.73205e-06 |
| scs         | ``eps_abs``                      | -         |     1e-09       |     0.001      |    1e-06       |
| scs         | ``eps_rel``                      | -         |     0           |     0          |    0           |
| scs         | ``time_limit_secs``              | 10.0      |    10           |    10          |   10           |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt      |                                93.8 |                                768.0 |                             8408591722842.2 |                             699782933.0 |                              6961.6 |
| daqp        |                                93.8 |                                766.2 |                             8408591722842.2 |                             699782933.0 |                              6941.6 |
| ecos        |                                56.2 |                               6132.0 |                            59925719263422.8 |                            4993371488.4 |                             51744.5 |
| gurobi      |                                93.8 |                                771.6 |                             8408591729669.0 |                             699783015.7 |                              6941.6 |
| highs       |                                98.4 |                                217.5 |                             2097454474596.5 |                             174561113.1 |                              1735.8 |
| jaxopt_osqp |                                93.8 |                               2474.0 |                             8437258843279.8 |                             703858657.1 |                              7667.2 |
| kvxopt      |                                93.8 |                                770.9 |                             8408591722842.2 |                             699782933.0 |                              6961.6 |
| osqp        |                               100.0 |                                  1.7 |                               51519478653.8 |                             513948033.7 |                              4235.8 |
| piqp        |                                95.3 |                                573.0 |                             6301745617656.5 |                             524446393.6 |                              5202.8 |
| proxqp      |                               100.0 |                                  8.3 |                                 137185053.2 |                                  3472.6 |                                18.3 |
| qpalm       |                               100.0 |                                  1.0 |                                5139775891.8 |                               1059519.6 |                               520.3 |
| qpax        |                                93.8 |                               1584.6 |                             8410796732438.8 |                             699986213.2 |                              6981.6 |
| qpswift     |                                46.9 |                               7701.5 |                            73095282987988.8 |                            6083162911.8 |                             60344.0 |
| quadprog    |                                93.8 |                                766.0 |                             8408591722842.2 |                             699782933.0 |                              6941.6 |
| scs         |                               100.0 |                                  4.6 |                                6896944774.0 |                             123672647.5 |                              4480.1 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 2.7 |
| cvxopt      |                                 0.0 |                                366.5 |                                      8796.5 |                                   194.5 |                           2691416.3 |
| daqp        |                                93.8 |                                365.7 |                                      8796.5 |                                   194.6 |                                 1.0 |
| ecos        |                                 0.0 |                               2926.6 |                                     61573.5 |                            1581979020.0 |                         295460817.2 |
| gurobi      |                                40.6 |                                367.4 |                                     15582.8 |                                 22016.3 |                              1632.4 |
| highs       |                                 0.0 |                                366.8 |                                      8799.0 |                               1376466.5 |                            212192.5 |
| jaxopt_osqp |                                 0.0 |                               8256.4 |                                    140737.2 |                                  3110.2 |                                15.7 |
| kvxopt      |                                 0.0 |                                366.5 |                                      8796.5 |                                   194.5 |                           2691416.3 |
| osqp        |                                85.9 |                                460.3 |                                     13502.8 |                                   733.2 |                                 4.9 |
| piqp        |                                95.3 |                                273.5 |                                      6597.8 |                                   185.7 |                                 4.3 |
| proxqp      |                                98.4 |                                103.4 |                                      9171.0 |                                   393.9 |                                 3.9 |
| qpalm       |                                96.9 |                                 91.0 |                                      6120.2 |                                    70.5 |                                 1.2 |
| qpax        |                                 0.0 |                               8256.4 |                                    140737.2 |                                  3110.2 |                                15.7 |
| qpswift     |                                 0.0 |                               3675.8 |                                     74767.8 |                                  1742.0 |                               177.0 |
| quadprog    |                                93.8 |                                365.6 |                                      8796.5 |                                   194.6 |                                 1.0 |
| scs         |                               100.0 |                                  9.0 |                                      8604.0 |                                    69.3 |                                 1.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.9 |                                      5803.1 |                                     1.0 |                                 4.8 |
| cvxopt      |                                90.6 |                                862.8 |                                2513051638.0 |                                  6168.8 |                                 3.7 |
| daqp        |                                93.8 |                                860.8 |                                2874957038.4 |                                  6168.8 |                                 1.0 |
| ecos        |                                23.4 |                               6889.6 |                               17591691290.1 |                                 93390.5 |                               307.4 |
| gurobi      |                                93.8 |                                865.0 |                                2513053576.7 |                                  6169.5 |                                 1.0 |
| highs       |                                93.8 |                                 31.1 |                                         1.0 |                                    62.2 |                               317.7 |
| jaxopt_osqp |                                28.1 |                               2732.6 |                               10655062886.6 |                                 40312.8 |                               100.3 |
| kvxopt      |                                90.6 |                                862.7 |                                2513051638.0 |                                  6168.8 |                                 3.7 |
| osqp        |                                87.5 |                                  2.1 |                                4251530245.6 |                                 10693.4 |                                20.7 |
| piqp        |                               100.0 |                                  8.1 |                                      1707.1 |                                  1419.6 |                                 3.9 |
| proxqp      |                               100.0 |                                  9.2 |                                5495333561.4 |                                  1121.7 |                                 4.5 |
| qpalm       |                                59.4 |                                  1.0 |                                1551238476.9 |                                  9167.2 |                                71.9 |
| qpax        |                                84.4 |                               1625.8 |                                3139316594.6 |                                  7871.8 |                                 6.5 |
| qpswift     |                                46.9 |                               8653.2 |                               21361439551.0 |                                 52438.1 |                                 8.7 |
| quadprog    |                                93.8 |                                860.7 |                                2513051638.0 |                                  6168.8 |                                 1.0 |
| scs         |                               100.0 |                                  2.5 |                                3851498886.1 |                                  3374.9 |                                 2.6 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  1.6 |                                         1.0 |                                     1.0 |                                 3.7 |
| cvxopt      |                                46.9 |                                637.1 |                                   5864062.3 |                                  2656.6 |                              2736.9 |
| daqp        |                                93.8 |                                635.6 |                                   5864062.3 |                                  2656.6 |                                 1.0 |
| ecos        |                                 6.2 |                               5087.5 |                                  41048433.2 |                              21638799.4 |                            300347.1 |
| gurobi      |                                90.6 |                                638.7 |                                   5868586.0 |                                  2954.9 |                                 2.7 |
| highs       |                                 0.0 |                                177.9 |                                   1490067.7 |                                 22489.9 |                               618.1 |
| jaxopt_osqp |                                20.3 |                               7269.4 |                                  68933531.0 |                                 29769.3 |                                19.5 |
| kvxopt      |                                46.9 |                                637.0 |                                   5864062.3 |                                  2656.6 |                              2736.9 |
| osqp        |                                73.4 |                                637.5 |                                  12424574.0 |                                 12758.7 |                                11.8 |
| piqp        |                                98.4 |                                162.1 |                                   1466016.8 |                                  2344.6 |                                 3.3 |
| proxqp      |                                98.4 |                                160.8 |                                   5541021.0 |                                  1656.5 |                                 3.1 |
| qpalm       |                                98.4 |                                  1.0 |                                   2187061.0 |                                   848.9 |                                 2.3 |
| qpax        |                                 0.0 |                               8330.4 |                                1843725943.3 |                                160809.8 |                               183.4 |
| qpswift     |                                 0.0 |                               6389.8 |                                  49844526.2 |                                 23316.3 |                               190.2 |
| quadprog    |                                93.8 |                                635.5 |                                   5864062.3 |                                  2656.6 |                                 1.0 |
| scs         |                               100.0 |                                  6.5 |                                   8126097.3 |                                  2454.3 |                                 2.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |        94 |               0 |             91 |             47 |
| daqp        |        94 |              94 |             94 |             94 |
| ecos        |        56 |               0 |             23 |              6 |
| gurobi      |        94 |              41 |             94 |             91 |
| highs       |        98 |               0 |             94 |              0 |
| jaxopt_osqp |        94 |               0 |             28 |             20 |
| kvxopt      |        94 |               0 |             91 |             47 |
| osqp        |       100 |              86 |             88 |             73 |
| piqp        |        95 |              95 |            100 |             98 |
| proxqp      |       100 |              98 |            100 |             98 |
| qpalm       |       100 |              97 |             59 |             98 |
| qpax        |        94 |               0 |             84 |              0 |
| qpswift     |        47 |               0 |             47 |              0 |
| quadprog    |        94 |              94 |             94 |             94 |
| scs         |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               6 |             97 |             53 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |              44 |             67 |             50 |
| gurobi      |       100 |              47 |            100 |             97 |
| highs       |       100 |               6 |             94 |              2 |
| jaxopt_osqp |       100 |             100 |             34 |             73 |
| kvxopt      |       100 |               6 |             97 |             53 |
| osqp        |       100 |              94 |             88 |             80 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |              98 |             59 |             98 |
| qpax        |       100 |             100 |             91 |             64 |
| qpswift     |       100 |              53 |            100 |             53 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       2.0 |             1.0 |            1.9 |            1.6 |
| cvxopt      |     768.0 |           366.5 |          862.8 |          637.1 |
| daqp        |     766.2 |           365.7 |          860.8 |          635.6 |
| ecos        |    6132.0 |          2926.6 |         6889.6 |         5087.5 |
| gurobi      |     771.6 |           367.4 |          865.0 |          638.7 |
| highs       |     217.5 |           366.8 |           31.1 |          177.9 |
| jaxopt_osqp |    2474.0 |          8256.4 |         2732.6 |         7269.4 |
| kvxopt      |     770.9 |           366.5 |          862.7 |          637.0 |
| osqp        |       1.7 |           460.3 |            2.1 |          637.5 |
| piqp        |     573.0 |           273.5 |            8.1 |          162.1 |
| proxqp      |       8.3 |           103.4 |            9.2 |          160.8 |
| qpalm       |       1.0 |            91.0 |            1.0 |            1.0 |
| qpax        |    1584.6 |          8256.4 |         1625.8 |         8330.4 |
| qpswift     |    7701.5 |          3675.8 |         8653.2 |         6389.8 |
| quadprog    |     766.0 |           365.6 |          860.7 |          635.5 |
| scs         |       4.6 |             9.0 |            2.5 |            6.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |          default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|-----------------:|----------------:|---------------:|---------------:|
| clarabel    |              1.0 |             1.0 |         5803.1 |            1.0 |
| cvxopt      |  8408591722842.2 |          8796.5 |   2513051638.0 |      5864062.3 |
| daqp        |  8408591722842.2 |          8796.5 |   2874957038.4 |      5864062.3 |
| ecos        | 59925719263422.8 |         61573.5 |  17591691290.1 |     41048433.2 |
| gurobi      |  8408591729669.0 |         15582.8 |   2513053576.7 |      5868586.0 |
| highs       |  2097454474596.5 |          8799.0 |            1.0 |      1490067.7 |
| jaxopt_osqp |  8437258843279.8 |        140737.2 |  10655062886.6 |     68933531.0 |
| kvxopt      |  8408591722842.2 |          8796.5 |   2513051638.0 |      5864062.3 |
| osqp        |    51519478653.8 |         13502.8 |   4251530245.6 |     12424574.0 |
| piqp        |  6301745617656.5 |          6597.8 |         1707.1 |      1466016.8 |
| proxqp      |      137185053.2 |          9171.0 |   5495333561.4 |      5541021.0 |
| qpalm       |     5139775891.8 |          6120.2 |   1551238476.9 |      2187061.0 |
| qpax        |  8410796732438.8 |        140737.2 |   3139316594.6 |   1843725943.3 |
| qpswift     | 73095282987988.8 |         74767.8 |  21361439551.0 |     49844526.2 |
| quadprog    |  8408591722842.2 |          8796.5 |   2513051638.0 |      5864062.3 |
| scs         |     6896944774.0 |          8604.0 |   3851498886.1 |      8126097.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |      default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|-------------:|----------------:|---------------:|---------------:|
| clarabel    |          1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt      |  699782933.0 |           194.5 |         6168.8 |         2656.6 |
| daqp        |  699782933.0 |           194.6 |         6168.8 |         2656.6 |
| ecos        | 4993371488.4 |    1581979020.0 |        93390.5 |     21638799.4 |
| gurobi      |  699783015.7 |         22016.3 |         6169.5 |         2954.9 |
| highs       |  174561113.1 |       1376466.5 |           62.2 |        22489.9 |
| jaxopt_osqp |  703858657.1 |          3110.2 |        40312.8 |        29769.3 |
| kvxopt      |  699782933.0 |           194.5 |         6168.8 |         2656.6 |
| osqp        |  513948033.7 |           733.2 |        10693.4 |        12758.7 |
| piqp        |  524446393.6 |           185.7 |         1419.6 |         2344.6 |
| proxqp      |       3472.6 |           393.9 |         1121.7 |         1656.5 |
| qpalm       |    1059519.6 |            70.5 |         9167.2 |          848.9 |
| qpax        |  699986213.2 |          3110.2 |         7871.8 |       160809.8 |
| qpswift     | 6083162911.8 |          1742.0 |        52438.1 |        23316.3 |
| quadprog    |  699782933.0 |           194.6 |         6168.8 |         2656.6 |
| scs         |  123672647.5 |            69.3 |         3374.9 |         2454.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       1.0 |             2.7 |            4.8 |            3.7 |
| cvxopt      |    6961.6 |       2691416.3 |            3.7 |         2736.9 |
| daqp        |    6941.6 |             1.0 |            1.0 |            1.0 |
| ecos        |   51744.5 |     295460817.2 |          307.4 |       300347.1 |
| gurobi      |    6941.6 |          1632.4 |            1.0 |            2.7 |
| highs       |    1735.8 |        212192.5 |          317.7 |          618.1 |
| jaxopt_osqp |    7667.2 |            15.7 |          100.3 |           19.5 |
| kvxopt      |    6961.6 |       2691416.3 |            3.7 |         2736.9 |
| osqp        |    4235.8 |             4.9 |           20.7 |           11.8 |
| piqp        |    5202.8 |             4.3 |            3.9 |            3.3 |
| proxqp      |      18.3 |             3.9 |            4.5 |            3.1 |
| qpalm       |     520.3 |             1.2 |           71.9 |            2.3 |
| qpax        |    6981.6 |            15.7 |            6.5 |          183.4 |
| qpswift     |   60344.0 |           177.0 |            8.7 |          190.2 |
| quadprog    |    6941.6 |             1.0 |            1.0 |            1.0 |
| scs         |    4480.1 |             1.4 |            2.6 |            2.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
