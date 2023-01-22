# PyPi Wrangler

To easily collect Python dependencies that you need and prep them for you to easily self host.

#### Contents

- [Building Package](#1-building-package)
- [Using PyPi Wrangler](#2-using-pypi-wrangler)
    - [Downloading all packages](#21-downloading-all-packages)
    - [Building dist](#22-building-dist)

## 1. Building Package

`python3 setup.py sdist bdist_wheel` will create the required `build`, `dist`, `PyPi-Wrangler.egg-info`.

## 2. Using PyPi Wrangler

### 2.1. Downloading all packages

https://pip.pypa.io/en/stable/cli/pip_download/

The following lines would install all `.whl`'s and `.tar.gz`'s for the requests library and all dependencies that it would need.

`pip download requests && pip download --no-binary :all: requests`

### 2.2. Building dist

To build a `/dist`, simply ensure you have all packages and dependencies installed into a singular directory [Downloading all packages](#21-downloading-all-packages). Once that has been taken care of, in Python:

```
import pypi_wrangler as wrangler

# building a "./dist" in to_path
wrangler.create_dist(from_path='./packages', to_path='./cleaned/', cleanup=True)
```

NOTE: the `cleanup` parameter is optional. If the `cleanup` boolean is `True`, and we successfully created the new dist, we remove the original `from_path` directory and anything lying inside of it. By default it's defined to `False` as it's better not assume that the user is wanting to delete the original directory and EVERYTHING inside of it.