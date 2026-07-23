# MPC test set for QP solvers

This repository contains quadratic programs (QPs) arising from model predictive control in robotics, in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Here is the report produced by this benchmarking tool:

- 📈 <a href="./results/mpc_qpbenchmark.md"><strong>MPC test set results</strong></a>
- 📈 [Dense subtest results](https://github.com/qpsolvers/mpc_qpbenchmark/blob/main/results/mpc_qpbenchmark_dense.md)
- 📈 [Sparse subtest results](https://github.com/qpsolvers/mpc_qpbenchmark/blob/main/results/mpc_qpbenchmark_sparse.md)

The methodology and limitations of the benchmark are described in the [qpbenchmark readme](https://github.com/qpsolvers/qpbenchmark/). This test set, in particular, does not reflect the warm-starting that is frequently used on robots that do model predictive control.

## Installation

The recommended process is to install the benchmark and all solvers using [pixi](https://pixi.prefix.dev/):

```console
pixi install
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```console
pixi run mpc_qpbenchmark         # full test set
pixi run mpc_qpbenchmark_dense   # dense subset
pixi run mpc_qpbenchmark_sparse  # sparse subset
```

The outcome, written to the `results/` directory, is a standardized report comparing all available solvers against the different benchmark metrics. You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/mpc_qpbenchmark/discussions/categories/results).

# Adding HPIPM to the pixi environment

The HPIPM solver is not packaged, but instructions to install from source are given in [hpipm](https://github.com/giaf/hpipm#python):

- Clone BLASFEO: `git clone https://github.com/giaf/blasfeo.git`
- From the BLASFEO directory, run: `make shared_library -j 4`
- Check that you are in your pixi environment (`pixi shell`), then run:

```console
cp -f ./lib/libblasfeo.so ${CONDA_PREFIX}/lib/
cp -f ./include/*.h ${CONDA_PREFIX}/include/
```

- Clone HPIPM: `git clone https://github.com/giaf/hpipm.git`
- From the HPIPM directory, run: `make shared_library -j4 BLASFEO_PATH=${CONDA_PREFIX}`
- Check that you are in your pixi environment, then run:

```console
cp -f libhpipm.so ${CONDA_PREFIX}/lib/
cp -f ./include/*.h ${CONDA_PREFIX}/include/
```

- Go to `hpipm/interfaces/python/hpipm_python` and run `pip install .`
- Try to import the package in Python:

```py
import hpipm_python.common as hpipm
```

## Contributions

The problems in this test set have been contributed by:

| Problems | Contributor | Details |
|----------|-------------|---------|
| ``QUADCMPC*`` | [@paLeziart](https://github.com/paLeziart) | Proposed in [#1](https://github.com/qpsolvers/mpc_qpbenchmark/issues/1), details in [this thesis](https://laas.hal.science/tel-03936109/document) |
| ``LIPMWALK*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#3](https://github.com/qpsolvers/mpc_qpbenchmark/issues/3), details in [this paper](https://hal.archives-ouvertes.fr/hal-01875387/document) |
| ``WHLIPBAL*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#4](https://github.com/qpsolvers/mpc_qpbenchmark/issues/4), details in [this paper](https://inria.hal.science/hal-04198663/) |

## Citation

This test set is run using `qpbenchmark`. If you use it in your work, you can refer to it using [this citation](https://github.com/qpsolvers/qpbenchmark#citation).

## See also

Related test sets that may be relevant to your use cases:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems welcome!
- [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/): a standard test set with problems designed to be difficult.
