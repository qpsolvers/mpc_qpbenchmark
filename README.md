# MPC test set for QP solvers

This repository contains quadratic programs (QPs) arising from model predictive control in robotics, in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Here is the report produced by this benchmarking tool:

<p align=center>
  📈 <a href="results/mpc_qpbenchmark_ref.md"><strong>MPC test set results</strong></a>
</p>

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```
python ./mpc_qpbenchmark.py run
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/mpc_qpbenchmark/discussions/categories/results).

## Contributions

The problems in this test set have been contributed by:

| Problems | Contributor | Details |
|----------|-------------|---------|
| ``QUADCMPC*`` | [@paLeziart](https://github.com/paLeziart) | Proposed in [#1](https://github.com/qpsolvers/mpc_qpbenchmark/issues/1), details in [this thesis](https://laas.hal.science/tel-03936109/document) |
| ``LIPMWALK*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#3](https://github.com/qpsolvers/mpc_qpbenchmark/issues/3), details in [this paper](https://hal.archives-ouvertes.fr/hal-01875387/document) |
| ``WHLIPBAL*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#4](https://github.com/qpsolvers/mpc_qpbenchmark/issues/4), details in [this paper](https://inria.hal.science/hal-04198663/) |

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2024,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = jan,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {2.2.0},
  year = {2024}
}
```
