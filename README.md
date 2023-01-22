# PyPi Wrangler

To easily collect Python dependencies that you need and prep them for you to easily self host.

## Downloading all packages

https://pip.pypa.io/en/stable/cli/pip_download/

The following lines would install all `.whl`'s and `.tar.gz`'s for the requests library and all dependencies that it would need.

`pip download requests && pip download --no-binary :all: requests`