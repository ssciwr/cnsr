# Welcome to the CNSR Lab Code Base

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ssciwr/cnsr/ci.yml?branch=main)](https://github.com/ssciwr/cnsr/actions/workflows/ci.yml)
[![PyPI Release](https://img.shields.io/pypi/v/cnsr.svg)](https://pypi.org/project/cnsr)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/cnsr.svg)](https://anaconda.org/conda-forge/cnsr)

This repository provides Jupyter notebook templates required to perform analysis on the data created during experiments at the [CNSR core facility of Heidelberg University](https://cnsr.uni-heidelberg.de/).

## Installation

The recommended installation for the `cnsr` Python package is via Conda:

```bash
conda install -c conda-forge cnsr
```

## Usage

After installing `cnsr`, start JupyterLab either via the command line or via the Jupyter App launcher UI on Windows:

```bash
jupyter lab
```

In the JupyterLab launcher, you will see a shortcut for each analysis task at CNSR. Clicking on this notebook will create a copy of the respective analysis notebook in the current working directory.

## Acknowledgments

The conda packaging of this repository was implemented by the [Scientific Software Center at Heidelberg University](https://ssc.uni-heidelberg.de).
