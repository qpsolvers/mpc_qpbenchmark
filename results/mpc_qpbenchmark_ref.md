# Model predictive control test set

| Number of problems | 64 |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0 |
| Date               | 2023-12-21 15:09:20.204446+00:00 |
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
| qpalm    | 1.2.1     |
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.2.0.

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
| clarabel |                               100.0 |                                  2.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                93.8 |                                774.1 |                             8408591722842.2 |                              48634023.9 |                              8710.1 |
| daqp     |                                93.8 |                                769.6 |                             8408591722842.2 |                              48634023.9 |                              8600.2 |
| ecos     |                                51.6 |                               5903.9 |                            57742209839725.0 |                             343974925.3 |                             73029.9 |
| highs    |                                93.8 |                                774.5 |                             8408591722843.5 |                              48684542.1 |                              8610.6 |
| osqp     |                                96.9 |                                  1.8 |                               28845300900.2 |                             136955634.4 |                             57709.6 |
| piqp     |                                95.3 |                                576.1 |                             6301745617656.5 |                              36448352.7 |                              6445.4 |
| proxqp   |                               100.0 |                                 14.7 |                                 135890317.5 |                                   765.6 |                                22.8 |
| qpalm    |                               100.0 |                                  1.0 |                                5094196230.5 |                                254876.0 |                               547.2 |
| qpoases  |                                93.8 |                                770.3 |                             8408591722842.2 |                              48634023.9 |                              8600.2 |
| quadprog |                                96.9 |                                383.5 |                             4198034738010.8 |                              24280798.6 |                              4293.7 |
| scs      |                                95.3 |                                 10.3 |                                4909131068.5 |                              57756388.4 |                             19698.9 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 5.6 |
| cvxopt   |                                 0.0 |                                394.1 |                                      8796.5 |                                    18.6 |                          23645978.9 |
| daqp     |                                93.8 |                                391.3 |                                      8796.5 |                                    18.6 |                                 2.0 |
| ecos     |                                 0.0 |                               3001.9 |                                     59374.0 |                            2110319364.4 |                        1590212143.2 |
| highs    |                                 0.0 |                                393.3 |                                      8799.0 |                              18317502.4 |                           2234518.5 |
| osqp     |                                89.1 |                                492.3 |                                     13502.8 |                                    68.2 |                                 6.7 |
| piqp     |                                95.3 |                                293.0 |                                      6597.8 |                                    15.3 |                                 5.3 |
| proxqp   |                               100.0 |                                 75.3 |                                      6719.8 |                                    70.3 |                                 6.6 |
| qpalm    |                                96.9 |                                  1.3 |                                      3921.5 |                                     4.8 |                                 1.8 |
| qpoases  |                                93.8 |                                391.9 |                                      8796.5 |                                    18.6 |                                 2.0 |
| quadprog |                                96.9 |                                195.6 |                                      4399.0 |                                     9.3 |                                 1.0 |
| scs      |                                98.4 |                                205.5 |                                      8747.8 |                                     6.8 |                                 2.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.7 |                                       344.3 |                                  1209.3 |                             90097.9 |
| cvxopt   |                                85.9 |                                813.5 |                                 149079334.5 |                               6239177.7 |                            244923.6 |
| daqp     |                                93.8 |                                804.9 |                                 170548298.9 |                               6239177.7 |                             18631.8 |
| ecos     |                                45.3 |                               6174.2 |                                1006303588.5 |                            1220573917.7 |                          27923922.9 |
| highs    |                                89.1 |                                807.9 |                                 149079334.5 |                              12398100.6 |                             40016.1 |
| osqp     |                                87.5 |                                  2.4 |                                 245401101.9 |                               9775810.2 |                            353876.0 |
| piqp     |                               100.0 |                                 13.0 |                                       101.7 |                               1446006.3 |                             42008.3 |
| proxqp   |                               100.0 |                                 17.6 |                                 321704771.1 |                              10990264.8 |                             79987.6 |
| qpalm    |                                96.9 |                                  1.0 |                                  91250084.7 |                               3340665.8 |                             42885.2 |
| qpoases  |                               100.0 |                                 35.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| quadprog |                                96.9 |                                402.4 |                                  74539550.8 |                               3119584.0 |                              9315.9 |
| scs      |                               100.0 |                                  4.6 |                                 200576014.8 |                               3245935.1 |                             44324.7 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.4 |                                         1.0 |                                     1.0 |                                 8.3 |
| cvxopt   |                                46.9 |                                580.1 |                                   5864062.3 |                                   369.2 |                             28327.0 |
| daqp     |                                93.8 |                                575.0 |                                   5864062.3 |                                   369.2 |                                 2.3 |
| ecos     |                                 4.7 |                               4411.1 |                                  39582417.7 |                              69733106.5 |                           3479356.7 |
| highs    |                                39.1 |                                577.3 |                                   5864063.5 |                                364812.1 |                              2679.0 |
| osqp     |                                89.1 |                                576.8 |                                  12424574.0 |                                  1553.8 |                                10.0 |
| piqp     |                                96.9 |                                287.1 |                                   2932031.8 |                                   217.7 |                                 8.9 |
| proxqp   |                               100.0 |                                 31.9 |                                   4075011.8 |                                  1648.0 |                                 8.8 |
| qpalm    |                               100.0 |                                  1.0 |                                   2150703.5 |                                    44.3 |                                 1.0 |
| qpoases  |                                93.8 |                                575.5 |                                   5864062.3 |                                   369.2 |                                 2.3 |
| quadprog |                                96.9 |                                287.5 |                                   2932031.5 |                                   184.6 |                                 1.2 |
| scs      |                               100.0 |                                 15.8 |                                   7862807.7 |                                   400.7 |                                 6.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |        94 |               0 |             86 |             47 |
| daqp     |        94 |              94 |             94 |             94 |
| ecos     |        52 |               0 |             45 |              5 |
| highs    |        94 |               0 |             89 |             39 |
| osqp     |        97 |              89 |             88 |             89 |
| piqp     |        95 |              95 |            100 |             97 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              97 |             97 |            100 |
| qpoases  |        94 |              94 |            100 |             94 |
| quadprog |        97 |              97 |             97 |             97 |
| scs      |        95 |              98 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |               6 |             92 |             53 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |        94 |              42 |             88 |             47 |
| highs    |       100 |               6 |             95 |             45 |
| osqp     |        97 |              97 |             88 |             95 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              97 |             97 |            100 |
| qpoases  |       100 |             100 |            100 |            100 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |        95 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       2.1 |             1.0 |            1.7 |            1.4 |
| cvxopt   |     774.1 |           394.1 |          813.5 |          580.1 |
| daqp     |     769.6 |           391.3 |          804.9 |          575.0 |
| ecos     |    5903.9 |          3001.9 |         6174.2 |         4411.1 |
| highs    |     774.5 |           393.3 |          807.9 |          577.3 |
| osqp     |       1.8 |           492.3 |            2.4 |          576.8 |
| piqp     |     576.1 |           293.0 |           13.0 |          287.1 |
| proxqp   |      14.7 |            75.3 |           17.6 |           31.9 |
| qpalm    |       1.0 |             1.3 |            1.0 |            1.0 |
| qpoases  |     770.3 |           391.9 |           35.2 |          575.5 |
| quadprog |     383.5 |           195.6 |          402.4 |          287.5 |
| scs      |      10.3 |           205.5 |            4.6 |           15.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |          default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-----------------:|----------------:|---------------:|---------------:|
| clarabel |              1.0 |             1.0 |          344.3 |            1.0 |
| cvxopt   |  8408591722842.2 |          8796.5 |    149079334.5 |      5864062.3 |
| daqp     |  8408591722842.2 |          8796.5 |    170548298.9 |      5864062.3 |
| ecos     | 57742209839725.0 |         59374.0 |   1006303588.5 |     39582417.7 |
| highs    |  8408591722843.5 |          8799.0 |    149079334.5 |      5864063.5 |
| osqp     |    28845300900.2 |         13502.8 |    245401101.9 |     12424574.0 |
| piqp     |  6301745617656.5 |          6597.8 |          101.7 |      2932031.8 |
| proxqp   |      135890317.5 |          6719.8 |    321704771.1 |      4075011.8 |
| qpalm    |     5094196230.5 |          3921.5 |     91250084.7 |      2150703.5 |
| qpoases  |  8408591722842.2 |          8796.5 |            1.0 |      5864062.3 |
| quadprog |  4198034738010.8 |          4399.0 |     74539550.8 |      2932031.5 |
| scs      |     4909131068.5 |          8747.8 |    200576014.8 |      7862807.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |     default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|------------:|----------------:|---------------:|---------------:|
| clarabel |         1.0 |             1.0 |         1209.3 |            1.0 |
| cvxopt   |  48634023.9 |            18.6 |      6239177.7 |          369.2 |
| daqp     |  48634023.9 |            18.6 |      6239177.7 |          369.2 |
| ecos     | 343974925.3 |    2110319364.4 |   1220573917.7 |     69733106.5 |
| highs    |  48684542.1 |      18317502.4 |     12398100.6 |       364812.1 |
| osqp     | 136955634.4 |            68.2 |      9775810.2 |         1553.8 |
| piqp     |  36448352.7 |            15.3 |      1446006.3 |          217.7 |
| proxqp   |       765.6 |            70.3 |     10990264.8 |         1648.0 |
| qpalm    |    254876.0 |             4.8 |      3340665.8 |           44.3 |
| qpoases  |  48634023.9 |            18.6 |            1.0 |          369.2 |
| quadprog |  24280798.6 |             9.3 |      3119584.0 |          184.6 |
| scs      |  57756388.4 |             6.8 |      3245935.1 |          400.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             5.6 |        90097.9 |            8.3 |
| cvxopt   |    8710.1 |      23645978.9 |       244923.6 |        28327.0 |
| daqp     |    8600.2 |             2.0 |        18631.8 |            2.3 |
| ecos     |   73029.9 |    1590212143.2 |     27923922.9 |      3479356.7 |
| highs    |    8610.6 |       2234518.5 |        40016.1 |         2679.0 |
| osqp     |   57709.6 |             6.7 |       353876.0 |           10.0 |
| piqp     |    6445.4 |             5.3 |        42008.3 |            8.9 |
| proxqp   |      22.8 |             6.6 |        79987.6 |            8.8 |
| qpalm    |     547.2 |             1.8 |        42885.2 |            1.0 |
| qpoases  |    8600.2 |             2.0 |            1.0 |            2.3 |
| quadprog |    4293.7 |             1.0 |         9315.9 |            1.2 |
| scs      |   19698.9 |             2.7 |        44324.7 |            6.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
