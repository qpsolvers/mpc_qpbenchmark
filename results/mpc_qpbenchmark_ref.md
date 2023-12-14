# Model predictive control test set

| Number of problems | 64       |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0rc1 |
| Date               | 2023-12-14 14:34:57.347883+00:00              |
| CPU                | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
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

| solver   | version   |
|:---------|:----------|
| clarabel | 0.6.0     |
| cvxopt   | 1.3.2     |
| daqp     | 0.5.1     |
| ecos     | 2.0.11    |
| highs    | 1.5.3     |
| osqp     | 0.6.3     |
| piqp     | 0.2.3     |
| proxqp   | 0.6.1     |
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.1.1.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| `count` | 4 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fxsr`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `ibpb`, `ibrs`, `ida`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pti`, `pts`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sgx`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tscdeadline`, `vme`, `vmx`, `vnmi`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 2.6000 GHz |
| `hz_advertised_friendly` | 2.5000 GHz |
| `l1_data_cache_size` | 65536 |
| `l1_instruction_cache_size` | 65536 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 524288 |
| `l3_cache_size` | 4194304 |
| `model` | 78 |
| `python_version` | 3.10.13.final.0 (64 bit) |
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
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| piqp     | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
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
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                46.9 |                               3247.9 |                            73095282987988.8 |                             422772071.5 |                             74760.9 |
| daqp     |                                46.9 |                               3245.9 |                            73095282987988.8 |                             422772071.5 |                             74760.8 |
| ecos     |                                51.6 |                               2477.2 |                            57742209839725.0 |                             343974925.3 |                             73029.9 |
| highs    |                                93.8 |                                323.9 |                             8408591722843.5 |                              48684542.1 |                              8610.6 |
| osqp     |                                96.9 |                                  1.5 |                               28845300900.2 |                             136955634.4 |                             57709.6 |
| piqp     |                                96.9 |                                160.9 |                             4198034738010.8 |                              24280806.9 |                              4293.8 |
| proxqp   |                               100.0 |                                  6.1 |                                 135889350.0 |                                   765.6 |                                22.8 |
| qpoases  |                                46.9 |                               3246.3 |                            73095282987988.8 |                             422772071.5 |                             74760.8 |
| quadprog |                                46.9 |                               3245.9 |                            73095282987988.8 |                             422772071.5 |                             74760.8 |
| scs      |                                53.1 |                               2804.4 |                            64307737419222.8 |                             371928957.4 |                             65774.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| cvxopt   |                                 0.0 |                               3461.2 |                                     74766.5 |                                   157.7 |                               541.3 |
| daqp     |                                46.9 |                               3458.8 |                                     74766.5 |                                   157.7 |                                 3.1 |
| ecos     |                                 0.0 |                               2639.5 |                                     59374.0 |                            2110319364.4 |                         298142091.6 |
| highs    |                                 0.0 |                                345.1 |                                      8799.0 |                              18317502.4 |                            418940.3 |
| osqp     |                                89.1 |                                433.4 |                                     13502.8 |                                    68.2 |                                 1.3 |
| piqp     |                                95.3 |                                257.8 |                                      6597.8 |                                    17.2 |                                 1.0 |
| proxqp   |                               100.0 |                                 73.3 |                                      6442.2 |                                    70.3 |                                 1.2 |
| qpoases  |                                46.9 |                               3459.2 |                                     74766.5 |                                   157.7 |                                 3.1 |
| quadprog |                                46.9 |                               3458.8 |                                     74766.5 |                                   157.7 |                                 3.1 |
| scs      |                                51.6 |                               3230.9 |                                     74667.2 |                                   146.0 |                                 3.2 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         3.5 |                                     1.0 |                                 2.3 |
| cvxopt   |                                46.9 |                               4463.6 |                                  12958107.1 |                                 43854.9 |                                 4.0 |
| daqp     |                                46.9 |                               4460.1 |                                  13177653.6 |                                 43854.9 |                                 4.0 |
| ecos     |                                45.3 |                               3403.8 |                                  10290205.2 |                               1009311.8 |                               697.8 |
| highs    |                                89.1 |                                445.0 |                                   1524447.5 |                                 10252.2 |                                 1.0 |
| osqp     |                                87.5 |                                  1.8 |                                   2509409.4 |                                  8083.9 |                                 8.8 |
| piqp     |                               100.0 |                                  7.1 |                                         1.0 |                                  1179.4 |                                 1.0 |
| proxqp   |                               100.0 |                                 10.4 |                                   3289671.2 |                                  9088.0 |                                 2.0 |
| qpoases  |                                53.1 |                               3874.1 |                                  11433588.2 |                                 38695.3 |                                 3.5 |
| quadprog |                                46.9 |                               4460.0 |                                  12958107.1 |                                 43854.9 |                                 4.0 |
| scs      |                                53.1 |                               3849.4 |                                  13484723.7 |                                 41377.3 |                                 4.6 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                46.9 |                               3856.1 |                                  49844526.2 |                                  3138.3 |                                 2.8 |
| daqp     |                                46.9 |                               3852.7 |                                  49844526.2 |                                  3138.3 |                                 2.4 |
| ecos     |                                 4.7 |                               2940.3 |                                  39582417.7 |                              69733106.5 |                            419227.4 |
| highs    |                                39.1 |                                384.4 |                                   5864063.5 |                                364812.1 |                               322.8 |
| osqp     |                                89.1 |                                384.8 |                                  12424574.0 |                                  1556.5 |                                 1.2 |
| piqp     |                                96.9 |                                191.7 |                                   2932043.5 |                                   218.4 |                                 1.1 |
| proxqp   |                               100.0 |                                 20.6 |                                   4075066.0 |                                  1647.6 |                                 1.0 |
| qpoases  |                                46.9 |                               3853.0 |                                  49844526.2 |                                  3138.3 |                                 2.4 |
| quadprog |                                46.9 |                               3852.7 |                                  49844526.2 |                                  3138.3 |                                 2.4 |
| scs      |                                53.1 |                               3335.3 |                                  53356592.5 |                                  3096.4 |                                 2.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |        47 |               0 |             47 |             47 |
| daqp     |        47 |              47 |             47 |             47 |
| ecos     |        52 |               0 |             45 |              5 |
| highs    |        94 |               0 |             89 |             39 |
| osqp     |        97 |              89 |             88 |             89 |
| piqp     |        97 |              95 |            100 |             97 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpoases  |        47 |              47 |             53 |             47 |
| quadprog |        47 |              47 |             47 |             47 |
| scs      |        53 |              52 |             53 |             53 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              53 |            100 |            100 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |        94 |              42 |             88 |             47 |
| highs    |       100 |               6 |             95 |             45 |
| osqp     |        97 |              97 |             88 |             95 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpoases  |       100 |             100 |            100 |            100 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |    3247.9 |          3461.2 |         4463.6 |         3856.1 |
| daqp     |    3245.9 |          3458.8 |         4460.1 |         3852.7 |
| ecos     |    2477.2 |          2639.5 |         3403.8 |         2940.3 |
| highs    |     323.9 |           345.1 |          445.0 |          384.4 |
| osqp     |       1.5 |           433.4 |            1.8 |          384.8 |
| piqp     |     160.9 |           257.8 |            7.1 |          191.7 |
| proxqp   |       6.1 |            73.3 |           10.4 |           20.6 |
| qpoases  |    3246.3 |          3459.2 |         3874.1 |         3853.0 |
| quadprog |    3245.9 |          3458.8 |         4460.0 |         3852.7 |
| scs      |    2804.4 |          3230.9 |         3849.4 |         3335.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |          default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-----------------:|----------------:|---------------:|---------------:|
| clarabel |              1.0 |             1.0 |            3.5 |            1.0 |
| cvxopt   | 73095282987988.8 |         74766.5 |     12958107.1 |     49844526.2 |
| daqp     | 73095282987988.8 |         74766.5 |     13177653.6 |     49844526.2 |
| ecos     | 57742209839725.0 |         59374.0 |     10290205.2 |     39582417.7 |
| highs    |  8408591722843.5 |          8799.0 |      1524447.5 |      5864063.5 |
| osqp     |    28845300900.2 |         13502.8 |      2509409.4 |     12424574.0 |
| piqp     |  4198034738010.8 |          6597.8 |            1.0 |      2932043.5 |
| proxqp   |      135889350.0 |          6442.2 |      3289671.2 |      4075066.0 |
| qpoases  | 73095282987988.8 |         74766.5 |     11433588.2 |     49844526.2 |
| quadprog | 73095282987988.8 |         74766.5 |     12958107.1 |     49844526.2 |
| scs      | 64307737419222.8 |         74667.2 |     13484723.7 |     53356592.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |     default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|------------:|----------------:|---------------:|---------------:|
| clarabel |         1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   | 422772071.5 |           157.7 |        43854.9 |         3138.3 |
| daqp     | 422772071.5 |           157.7 |        43854.9 |         3138.3 |
| ecos     | 343974925.3 |    2110319364.4 |      1009311.8 |     69733106.5 |
| highs    |  48684542.1 |      18317502.4 |        10252.2 |       364812.1 |
| osqp     | 136955634.4 |            68.2 |         8083.9 |         1556.5 |
| piqp     |  24280806.9 |            17.2 |         1179.4 |          218.4 |
| proxqp   |       765.6 |            70.3 |         9088.0 |         1647.6 |
| qpoases  | 422772071.5 |           157.7 |        38695.3 |         3138.3 |
| quadprog | 422772071.5 |           157.7 |        43854.9 |         3138.3 |
| scs      | 371928957.4 |           146.0 |        41377.3 |         3096.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.1 |            2.3 |            1.0 |
| cvxopt   |   74760.9 |           541.3 |            4.0 |            2.8 |
| daqp     |   74760.8 |             3.1 |            4.0 |            2.4 |
| ecos     |   73029.9 |     298142091.6 |          697.8 |       419227.4 |
| highs    |    8610.6 |        418940.3 |            1.0 |          322.8 |
| osqp     |   57709.6 |             1.3 |            8.8 |            1.2 |
| piqp     |    4293.8 |             1.0 |            1.0 |            1.1 |
| proxqp   |      22.8 |             1.2 |            2.0 |            1.0 |
| qpoases  |   74760.8 |             3.1 |            3.5 |            2.4 |
| quadprog |   74760.8 |             3.1 |            4.0 |            2.4 |
| scs      |   65774.0 |             3.2 |            4.6 |            2.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
