from setuptools import setup, find_packages

setup(
    name="myapi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi[all]",
        "uvicorn",
        "pytest",
        "pydantic"
    ],
)