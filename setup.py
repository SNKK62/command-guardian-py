from setuptools import setup, find_packages

setup(
    name="cmgd-py",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cmgd-py": ["bin/cmgd-arm64", "bin/cmgd-x86_64"],
    },
    entry_points={},
)
