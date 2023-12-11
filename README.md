# MPC test set for QP solvers

This repository contains quadratic programs (QPs) arising from model predictive control in robotics, in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark).

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Once you have [installed qpbenchmark](https://github.com/qpsolvers/qpbenchmark#installation), you can run the test set as follows:

```
qpbenchmark ./mpc.py run
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). Here is the report generated on a reference computer:

📈 **[MPC test set results](results/mpc_ref.md)**

You can check out results from various machines and share your own in the [Results forum](https://github.com/qpsolvers/mpc_qpbenchmark/discussions/categories/results).

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2023,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = dec,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {2.0.0},
  year = {2023}
}
```

You can also click on ``Cite this repository`` at the top-right of the [repository page](https://github.com/qpsolvers/qpbenchmark/).
