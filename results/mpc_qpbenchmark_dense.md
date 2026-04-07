# Model predictive control test set (dense)

| Number of problems | 60 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2026-04-07 18:03:58.295980+00:00 |
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

Problems arising from model predictive control in robotics, restricted to instances with dense cost matrices (LIPMWALK and WHLIPBAL).

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
| clarabel    |                               100.0 |                                 11.3 |                                         1.0 |                                  1947.1 |                           8349450.2 |
| cvxopt      |                               100.0 |                                 31.7 |                                         1.0 |                                     1.0 |                         165878236.1 |
| daqp        |                               100.0 |                                  1.4 |                                         1.0 |                                     2.3 |                                 2.8 |
| ecos        |                                60.0 |                              57378.1 |                          -218763017610834.0 |                         8426165932211.4 |                      372332354170.9 |
| gurobi      |                               100.0 |                                 41.1 |                                    -12224.0 |                                161525.0 |                            100532.8 |
| highs       |                                 0.0 |                             179491.6 |                          -562949953421310.0 |                        21651921285435.0 |                      909450651730.7 |
| jaxopt_osqp |                               100.0 |                               4696.7 |                             -115665286171.0 |                            7920954112.0 |                        5608305972.4 |
| kvxopt      |                               100.0 |                                 48.9 |                                         1.0 |                                     1.0 |                         165878236.1 |
| osqp        |                               100.0 |                                 12.6 |                              -80682804007.0 |                         1012360959304.0 |                       30361362296.5 |
| piqp        |                               100.0 |                                  4.7 |                                         1.0 |                                 22681.0 |                           1105896.1 |
| proxqp      |                               100.0 |                                  3.6 |                                -481817437.0 |                               1565025.2 |                          77147476.5 |
| qpalm       |                               100.0 |                                  6.9 |                               -3691710967.0 |                            2068094338.7 |                        4286535441.2 |
| qpax        |                               100.0 |                               2287.0 |                                         1.0 |                             412948785.3 |                         902879837.5 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.6 |                                 1.0 |
| scs         |                               100.0 |                                  6.9 |                              -19277793671.0 |                          243870292642.6 |                       37409867562.1 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                 14.6 |                                         1.0 |                                     4.7 |                               158.7 |
| cvxopt      |                                 0.0 |                                 22.4 |                                         1.0 |                                     1.0 |                         165878236.1 |
| daqp        |                               100.0 |                                  1.2 |                                         1.0 |                                     2.3 |                                 2.8 |
| ecos        |                                 0.0 |                              73242.6 |                                   -225181.0 |                           11747226786.0 |                       18211071435.0 |
| gurobi      |                                41.7 |                                 40.4 |                                    -12224.0 |                                161525.0 |                            100532.8 |
| highs       |                                 0.0 |                             229127.6 |                                   -562951.0 |                                 21652.0 |                               909.5 |
| jaxopt_osqp |                                 0.0 |                             229127.6 |                                   -562951.0 |                                 21652.0 |                               909.5 |
| kvxopt      |                                 0.0 |                                 15.5 |                                         1.0 |                                     1.0 |                         165878236.1 |
| osqp        |                                98.3 |                               2678.9 |                                    -19061.0 |                                  3248.1 |                               130.5 |
| piqp        |                               100.0 |                                  5.6 |                                         1.0 |                                   187.7 |                               212.7 |
| proxqp      |                               100.0 |                                  3.9 |                                    -24066.0 |                                  2555.7 |                               206.6 |
| qpalm       |                                96.7 |                               2669.0 |                                     -9611.0 |                                   523.6 |                                71.7 |
| qpax        |                                 0.0 |                             229127.6 |                                   -562951.0 |                                 21652.0 |                               909.5 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.6 |                                 1.0 |
| scs         |                               100.0 |                                 13.5 |                                     -3221.0 |                                   514.7 |                                59.1 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                 12.8 |                                         1.0 |                                  1060.2 |                         276485181.2 |
| cvxopt      |                                96.7 |                                 15.9 |                                         1.0 |                                     1.0 |                         165878236.1 |
| daqp        |                               100.0 |                                  1.1 |                               -5404420365.0 |                                     2.3 |                                 2.8 |
| ecos        |                                25.0 |                              76139.1 |                             -225173226328.0 |                           20408196704.2 |                       18575568839.3 |
| gurobi      |                               100.0 |                                 39.0 |                                    -12224.0 |                                161525.0 |                            100532.8 |
| highs       |                                 0.0 |                             238188.9 |                             -562949953418.0 |                           21651921285.3 |                         909450651.7 |
| jaxopt_osqp |                                31.7 |                               5820.7 |                             -115665286171.0 |                            7920954112.0 |                        5608305972.4 |
| kvxopt      |                                96.7 |                                 29.9 |                                         1.0 |                                     1.0 |                         165878236.1 |
| osqp        |                               100.0 |                                 13.2 |                              -36447477230.0 |                            1444222365.7 |                         135157969.2 |
| piqp        |                               100.0 |                                  4.2 |                                         1.0 |                             111889694.7 |                         205957733.9 |
| proxqp      |                               100.0 |                                  3.2 |                              -81960186779.0 |                             261487781.1 |                         270730309.7 |
| qpalm       |                                58.3 |                                  7.8 |                               -4927158057.0 |                            2123826529.3 |                        4303474215.0 |
| qpax        |                                75.0 |                               2641.4 |                                         1.0 |                             412948785.3 |                         902879837.5 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.6 |                                 1.0 |
| scs         |                               100.0 |                                 11.0 |                              -47630793308.0 |                             512053784.7 |                         105663042.9 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                 13.7 |                                         1.0 |                                     nan |                                 nan |
| cvxopt      |                                50.0 |                                 19.0 |                                         1.0 |                                     nan |                                 nan |
| daqp        |                               100.0 |                                  1.1 |                                         1.0 |                                     nan |                                 nan |
| ecos        |                                 6.7 |                              73493.1 |                                -225179973.0 |                                     nan |                                 nan |
| gurobi      |                                96.7 |                                 36.8 |                                    -12224.0 |                                     nan |                                 nan |
| highs       |                                 0.0 |                             229909.6 |                                -562949947.0 |                                     nan |                                 nan |
| jaxopt_osqp |                                21.7 |                              98858.3 |                                -396591633.0 |                                     nan |                                 nan |
| kvxopt      |                                50.0 |                                 37.9 |                                         1.0 |                                     nan |                                 nan |
| osqp        |                                98.3 |                               2685.6 |                                 -42438069.0 |                                     nan |                                 nan |
| piqp        |                               100.0 |                                  4.5 |                                         1.0 |                                     nan |                                 nan |
| proxqp      |                               100.0 |                                  3.4 |                                 -25706294.0 |                                     nan |                                 nan |
| qpalm       |                                98.3 |                                  7.9 |                                  -6247936.0 |                                     nan |                                 nan |
| qpax        |                                10.0 |                             144719.8 |                                -394975295.0 |                                     nan |                                 nan |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     nan |                                 nan |
| scs         |                               100.0 |                                 11.4 |                                 -32531169.0 |                                     nan |                                 nan |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               0 |             97 |             50 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |        60 |               0 |             25 |              7 |
| gurobi      |       100 |              42 |            100 |             97 |
| highs       |         0 |               0 |              0 |              0 |
| jaxopt_osqp |       100 |               0 |             32 |             22 |
| kvxopt      |       100 |               0 |             97 |             50 |
| osqp        |       100 |              98 |            100 |             98 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |              97 |             58 |             98 |
| qpax        |       100 |               0 |             75 |             10 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               0 |             97 |             50 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |              40 |             65 |             47 |
| gurobi      |       100 |              42 |            100 |             97 |
| highs       |       100 |             100 |            100 |            100 |
| jaxopt_osqp |       100 |             100 |             32 |             72 |
| kvxopt      |       100 |               0 |             97 |             50 |
| osqp        |       100 |             100 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |              98 |             58 |             98 |
| qpax        |       100 |             100 |             75 |             80 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |      11.3 |            14.6 |           12.8 |           13.7 |
| cvxopt      |      31.7 |            22.4 |           15.9 |           19.0 |
| daqp        |       1.4 |             1.2 |            1.1 |            1.1 |
| ecos        |   57378.1 |         73242.6 |        76139.1 |        73493.1 |
| gurobi      |      41.1 |            40.4 |           39.0 |           36.8 |
| highs       |  179491.6 |        229127.6 |       238188.9 |       229909.6 |
| jaxopt_osqp |    4696.7 |        229127.6 |         5820.7 |        98858.3 |
| kvxopt      |      48.9 |            15.5 |           29.9 |           37.9 |
| osqp        |      12.6 |          2678.9 |           13.2 |         2685.6 |
| piqp        |       4.7 |             5.6 |            4.2 |            4.5 |
| proxqp      |       3.6 |             3.9 |            3.2 |            3.4 |
| qpalm       |       6.9 |          2669.0 |            7.8 |            7.9 |
| qpax        |    2287.0 |        229127.6 |         2641.4 |       144719.8 |
| quadprog    |       1.0 |             1.0 |            1.0 |            1.0 |
| scs         |       6.9 |            13.5 |           11.0 |           11.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |            default |   high_accuracy |    low_accuracy |   mid_accuracy |
|:------------|-------------------:|----------------:|----------------:|---------------:|
| clarabel    |                1.0 |             1.0 |             1.0 |            1.0 |
| cvxopt      |                1.0 |             1.0 |             1.0 |            1.0 |
| daqp        |                1.0 |             1.0 |   -5404420365.0 |            1.0 |
| ecos        | -218763017610834.0 |       -225181.0 | -225173226328.0 |   -225179973.0 |
| gurobi      |           -12224.0 |        -12224.0 |        -12224.0 |       -12224.0 |
| highs       | -562949953421310.0 |       -562951.0 | -562949953418.0 |   -562949947.0 |
| jaxopt_osqp |    -115665286171.0 |       -562951.0 | -115665286171.0 |   -396591633.0 |
| kvxopt      |                1.0 |             1.0 |             1.0 |            1.0 |
| osqp        |     -80682804007.0 |        -19061.0 |  -36447477230.0 |    -42438069.0 |
| piqp        |                1.0 |             1.0 |             1.0 |            1.0 |
| proxqp      |       -481817437.0 |        -24066.0 |  -81960186779.0 |    -25706294.0 |
| qpalm       |      -3691710967.0 |         -9611.0 |   -4927158057.0 |     -6247936.0 |
| qpax        |                1.0 |       -562951.0 |             1.0 |   -394975295.0 |
| quadprog    |                1.0 |             1.0 |             1.0 |            1.0 |
| scs         |     -19277793671.0 |         -3221.0 |  -47630793308.0 |    -32531169.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |          default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|-----------------:|----------------:|---------------:|---------------:|
| clarabel    |           1947.1 |             4.7 |         1060.2 |            nan |
| cvxopt      |              1.0 |             1.0 |            1.0 |            nan |
| daqp        |              2.3 |             2.3 |            2.3 |            nan |
| ecos        |  8426165932211.4 |   11747226786.0 |  20408196704.2 |            nan |
| gurobi      |         161525.0 |        161525.0 |       161525.0 |            nan |
| highs       | 21651921285435.0 |         21652.0 |  21651921285.3 |            nan |
| jaxopt_osqp |     7920954112.0 |         21652.0 |   7920954112.0 |            nan |
| kvxopt      |              1.0 |             1.0 |            1.0 |            nan |
| osqp        |  1012360959304.0 |          3248.1 |   1444222365.7 |            nan |
| piqp        |          22681.0 |           187.7 |    111889694.7 |            nan |
| proxqp      |        1565025.2 |          2555.7 |    261487781.1 |            nan |
| qpalm       |     2068094338.7 |           523.6 |   2123826529.3 |            nan |
| qpax        |      412948785.3 |         21652.0 |    412948785.3 |            nan |
| quadprog    |              1.6 |             1.6 |            1.6 |            nan |
| scs         |   243870292642.6 |           514.7 |    512053784.7 |            nan |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|---------------:|----------------:|---------------:|---------------:|
| clarabel    |      8349450.2 |           158.7 |    276485181.2 |            nan |
| cvxopt      |    165878236.1 |     165878236.1 |    165878236.1 |            nan |
| daqp        |            2.8 |             2.8 |            2.8 |            nan |
| ecos        | 372332354170.9 |   18211071435.0 |  18575568839.3 |            nan |
| gurobi      |       100532.8 |        100532.8 |       100532.8 |            nan |
| highs       | 909450651730.7 |           909.5 |    909450651.7 |            nan |
| jaxopt_osqp |   5608305972.4 |           909.5 |   5608305972.4 |            nan |
| kvxopt      |    165878236.1 |     165878236.1 |    165878236.1 |            nan |
| osqp        |  30361362296.5 |           130.5 |    135157969.2 |            nan |
| piqp        |      1105896.1 |           212.7 |    205957733.9 |            nan |
| proxqp      |     77147476.5 |           206.6 |    270730309.7 |            nan |
| qpalm       |   4286535441.2 |            71.7 |   4303474215.0 |            nan |
| qpax        |    902879837.5 |           909.5 |    902879837.5 |            nan |
| quadprog    |            1.0 |             1.0 |            1.0 |            nan |
| scs         |  37409867562.1 |            59.1 |    105663042.9 |            nan |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
