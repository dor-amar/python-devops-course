"""Setup configuration for example_package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="example_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An example Python package demonstrating package structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/example_package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "mypy>=0.950",
            "pydocstyle>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "example-cli=example_package.cli:main",
        ],
    },
) 