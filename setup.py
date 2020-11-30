import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="heru-api",
    version="1.0.0",
    description="Herucode challenge",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["api"],
    extras_require={"test": ["pytest", "coverage"]},
)
