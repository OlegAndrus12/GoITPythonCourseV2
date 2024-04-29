from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="moskali",
    version="6",
    description="Very useful code",
    long_description=long_description,
    url="http://github.com/dummy_user/useful",
    author="Oleh Andrus",
    author_email="andrus@test.gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "faker",
    ],
    entry_points={"console_scripts": ["run_main = moskali:main"]},
    include_package_data=True,
    package_data={"": ["*.txt"]},
)
