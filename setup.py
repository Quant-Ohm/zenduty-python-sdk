from setuptools import setup, find_packages

# Read README.md for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zenduty-api",
    version="1.0.1",
    description="Python SDK wrapper for the Zenduty API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vishwa Krishnakumar",
    author_email="vishwa@yellowant.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
        "urllib3>=2.2.2",
        "six>=1.16.0",
        "charset-normalizer>=3.4.0",
        "idna>=3.10",
        "certifi>=2024.7.4"
    ],
    scripts=["bin/client.py"],
)
