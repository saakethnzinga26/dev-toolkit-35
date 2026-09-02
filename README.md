# dev-toolkit-35

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

dev-toolkit-35 is a lightweight collection of Python utilities that simplifies routine development tasks. It offers reliable tools for configuration handling, logging, and performance measurement with minimal overhead.

## Features
- Schema-based configuration loader supporting YAML and JSON with automatic validation
- Context-aware structured logger that outputs in JSON format for easy parsing
- Precise execution timer implemented as a context manager for code profiling
- CLI command to initialize new Python projects with standard layout

## Installation

Install via pip:

```bash
pip install dev-toolkit-35
```

Install from source:

```bash
git clone https://github.com/Developer/dev-toolkit-35.git
cd dev-toolkit-35
pip install -e .
```

## Usage

```python
from dev_toolkit import load_config, get_logger, Timer

config = load_config('config.yaml')
logger = get_logger(__name__)

with Timer() as t:
    # perform work
    pass

logger.info("Task completed", duration=t.elapsed)
```