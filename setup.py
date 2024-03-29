#!/usr/bin/env python

# NOTE: We need this little hack to make sure that tox will run correctly from
# web (as it runs 'python ../pycommon/setup.py develop').
import os
os.chdir(os.path.dirname(__file__) or ".")

from setuptools import setup, find_packages

import dirt

version = "%s.%s-%s" %dirt.__version__
setup(
    name="dirt",
    version=version,
    packages=find_packages(),
    scripts=[
    ],
)
