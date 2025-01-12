# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="base2base",  # Unique package name on PyPI
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library to convert numbers between bases 2–62.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/base2base",  # URL to your GitHub repo
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)