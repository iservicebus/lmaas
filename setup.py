# Copyright (c) 2024, Jingnan Zhou.
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

from setuptools import setup, find_packages

def get_requirements(path: str):
    return [l.strip() for l in open(path)]

setup(
    name='LMaaS',
    version="0.0.1",
    packages=find_packages(where='src'),  # Include modules under 'src'
    package_dir={'': 'src'},  # Set base package directory to 'src'
    # ... other setuptools arguments
    install_requires=get_requirements("requirements.txt"),
)

