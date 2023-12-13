# Model predictive control test set

| Benchmark version | 2.1.0rc0 |
|:------------------|:--------------------|
| Date              | 2023-12-13 18:15:31.254810+00:00 |
| CPU               | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by            | [@stephane-caron](https://github.com/stephane-caron/) |

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
| `hz_actual_friendly` | 2.9220 GHz |
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
| clarabel |                               100.0 |                                  1.6 |                                         1.0 |                                 15606.0 |                                47.1 |
| cvxopt   |                                25.0 |                                452.5 |                           417143093101495.0 |                       417143093101495.0 |                       20332574320.8 |
| daqp     |                               100.0 |                                 47.1 |                            13594223429300.0 |                                     1.0 |                                 1.0 |
| ecos     |                                 0.0 |                                653.2 |                           562949953421313.0 |                       562949953421313.0 |                       27439557097.9 |
| highs    |                                 0.0 |                                653.2 |                           562949953421313.0 |                       562949953421313.0 |                       27439557097.9 |
| osqp     |                               100.0 |                                  1.0 |                             1364516583255.0 |                          236543767075.0 |                        2631028782.8 |
| piqp     |                                25.0 |                                446.6 |                           417143093101495.0 |                       417143093180989.0 |                       20332574258.9 |
| proxqp   |                               100.0 |                                  8.2 |                                1552519965.0 |                            2060140186.0 |                          34121012.2 |
| qpoases  |                                 0.0 |                                653.2 |                           562949953421313.0 |                       562949953421313.0 |                       27439557097.9 |
| quadprog |                                 0.0 |                                653.2 |                           562949953421313.0 |                       562949953421313.0 |                       27439557097.9 |
| scs      |                               100.0 |                                  5.0 |                              158386784017.0 |                            1174784564.0 |                            792222.8 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                  9746.0 |                                 7.3 |
| cvxopt   |                                 0.0 |                                406.6 |                                    422214.0 |                                422214.0 |                                96.1 |
| daqp     |                                50.0 |                                 44.0 |                                  23043176.0 |                                     1.0 |                                 1.0 |
| ecos     |                                 0.0 |                                585.6 |                                    562951.0 |                                562951.0 |                                27.4 |
| highs    |                                 0.0 |                                585.6 |                                    562951.0 |                                562951.0 |                                27.4 |
| osqp     |                                 0.0 |                                585.6 |                                    562951.0 |                                562951.0 |                                27.4 |
| piqp     |                                25.0 |                                401.6 |                                    422214.0 |                                424481.0 |                                20.8 |
| proxqp   |                               100.0 |                                 91.0 |                                     56839.0 |                                  3541.0 |                                11.8 |
| qpoases  |                                 0.0 |                                585.6 |                                    562951.0 |                                562951.0 |                                27.4 |
| quadprog |                                 0.0 |                                585.6 |                                    562951.0 |                                562951.0 |                                27.4 |
| scs      |                                75.0 |                                265.2 |                                    508604.0 |                                143324.0 |                                11.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                      4832.2 |                              90838319.0 |                           6881910.5 |
| cvxopt   |                               100.0 |                                 81.2 |                                        14.2 |                           12884894312.0 |                               249.0 |
| daqp     |                                50.0 |                                 74.4 |                             3071528084925.0 |                                     1.0 |                                 1.0 |
| ecos     |                                 0.0 |                               1079.2 |                                2092750756.2 |                          562949953420.0 |                          26697806.8 |
| highs    |                                 0.0 |                               1079.2 |                                2092750756.2 |                          562949953420.0 |                          26697806.8 |
| osqp     |                                25.0 |                                  1.3 |                                1613917153.2 |                           51545315382.0 |                         402998948.3 |
| piqp     |                               100.0 |                                 12.9 |                                      1427.6 |                           47531741543.0 |                           2411429.5 |
| proxqp   |                               100.0 |                                 14.5 |                                   5770962.4 |                             380482399.0 |                           1222556.8 |
| qpoases  |                               100.0 |                                 37.5 |                                         1.0 |                                 89066.0 |                              1432.2 |
| quadprog |                                 0.0 |                               1079.2 |                                2092750756.2 |                          562949953420.0 |                          26697806.8 |
| scs      |                               100.0 |                                  3.9 |                                 551206982.3 |                          108264449609.0 |                          22784338.8 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                 30956.0 |                              6034.1 |
| cvxopt   |                                25.0 |                                754.4 |                                   6397158.5 |                             422212460.0 |                             20655.2 |
| daqp     |                                75.0 |                                 79.5 |                              205973082262.1 |                                     1.0 |                                 1.0 |
| ecos     |                                 0.0 |                               1086.0 |                                   8529544.7 |                             562949952.0 |                             27439.6 |
| highs    |                                 0.0 |                               1086.0 |                                   8529544.7 |                             562949952.0 |                             27439.6 |
| osqp     |                                25.0 |                                742.8 |                                   8479089.4 |                             422218885.0 |                             20597.9 |
| piqp     |                                50.0 |                                455.7 |                                   4264772.7 |                             305191877.0 |                             16206.3 |
| proxqp   |                               100.0 |                                 38.0 |                                     85028.8 |                              14688216.0 |                             12240.2 |
| qpoases  |                                 0.0 |                               1086.0 |                                   8529544.7 |                             562949952.0 |                             27439.6 |
| quadprog |                                 0.0 |                               1086.0 |                                   8529544.7 |                             562949952.0 |                             27439.6 |
| scs      |                               100.0 |                                 18.6 |                                   6267825.8 |                                436901.0 |                              7513.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |        25 |               0 |            100 |             25 |
| daqp     |       100 |              50 |             50 |             75 |
| ecos     |         0 |               0 |              0 |              0 |
| highs    |         0 |               0 |              0 |              0 |
| osqp     |       100 |               0 |             25 |             25 |
| piqp     |        25 |              25 |            100 |             50 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpoases  |         0 |               0 |            100 |              0 |
| quadprog |         0 |               0 |              0 |              0 |
| scs      |       100 |              75 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              75 |            100 |            100 |
| daqp     |       100 |              50 |             50 |             75 |
| ecos     |       100 |             100 |            100 |            100 |
| highs    |       100 |             100 |            100 |            100 |
| osqp     |       100 |             100 |             25 |            100 |
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
| clarabel |       1.6 |             1.0 |            1.0 |            1.0 |
| cvxopt   |     452.5 |           406.6 |           81.2 |          754.4 |
| daqp     |      47.1 |            44.0 |           74.4 |           79.5 |
| ecos     |     653.2 |           585.6 |         1079.2 |         1086.0 |
| highs    |     653.2 |           585.6 |         1079.2 |         1086.0 |
| osqp     |       1.0 |           585.6 |            1.3 |          742.8 |
| piqp     |     446.6 |           401.6 |           12.9 |          455.7 |
| proxqp   |       8.2 |            91.0 |           14.5 |           38.0 |
| qpoases  |     653.2 |           585.6 |           37.5 |         1086.0 |
| quadprog |     653.2 |           585.6 |         1079.2 |         1086.0 |
| scs      |       5.0 |           265.2 |            3.9 |           18.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |           default |   high_accuracy |    low_accuracy |   mid_accuracy |
|:---------|------------------:|----------------:|----------------:|---------------:|
| clarabel |               1.0 |             1.0 |          4832.2 |            1.0 |
| cvxopt   | 417143093101495.0 |        422214.0 |            14.2 |      6397158.5 |
| daqp     |  13594223429300.0 |      23043176.0 | 3071528084925.0 | 205973082262.1 |
| ecos     | 562949953421313.0 |        562951.0 |    2092750756.2 |      8529544.7 |
| highs    | 562949953421313.0 |        562951.0 |    2092750756.2 |      8529544.7 |
| osqp     |   1364516583255.0 |        562951.0 |    1613917153.2 |      8479089.4 |
| piqp     | 417143093101495.0 |        422214.0 |          1427.6 |      4264772.7 |
| proxqp   |      1552519965.0 |         56839.0 |       5770962.4 |        85028.8 |
| qpoases  | 562949953421313.0 |        562951.0 |             1.0 |      8529544.7 |
| quadprog | 562949953421313.0 |        562951.0 |    2092750756.2 |      8529544.7 |
| scs      |    158386784017.0 |        508604.0 |     551206982.3 |      6267825.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |           default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|------------------:|----------------:|---------------:|---------------:|
| clarabel |           15606.0 |          9746.0 |     90838319.0 |        30956.0 |
| cvxopt   | 417143093101495.0 |        422214.0 |  12884894312.0 |    422212460.0 |
| daqp     |               1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 562949953421313.0 |        562951.0 | 562949953420.0 |    562949952.0 |
| highs    | 562949953421313.0 |        562951.0 | 562949953420.0 |    562949952.0 |
| osqp     |    236543767075.0 |        562951.0 |  51545315382.0 |    422218885.0 |
| piqp     | 417143093180989.0 |        424481.0 |  47531741543.0 |    305191877.0 |
| proxqp   |      2060140186.0 |          3541.0 |    380482399.0 |     14688216.0 |
| qpoases  | 562949953421313.0 |        562951.0 |        89066.0 |    562949952.0 |
| quadprog | 562949953421313.0 |        562951.0 | 562949953420.0 |    562949952.0 |
| scs      |      1174784564.0 |        143324.0 | 108264449609.0 |       436901.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel |          47.1 |             7.3 |      6881910.5 |         6034.1 |
| cvxopt   | 20332574320.8 |            96.1 |          249.0 |        20655.2 |
| daqp     |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 27439557097.9 |            27.4 |     26697806.8 |        27439.6 |
| highs    | 27439557097.9 |            27.4 |     26697806.8 |        27439.6 |
| osqp     |  2631028782.8 |            27.4 |    402998948.3 |        20597.9 |
| piqp     | 20332574258.9 |            20.8 |      2411429.5 |        16206.3 |
| proxqp   |    34121012.2 |            11.8 |      1222556.8 |        12240.2 |
| qpoases  | 27439557097.9 |            27.4 |         1432.2 |        27439.6 |
| quadprog | 27439557097.9 |            27.4 |     26697806.8 |        27439.6 |
| scs      |      792222.8 |            11.6 |     22784338.8 |         7513.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
