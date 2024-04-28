from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()
    
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name="customer-signup-prediction",
    version="0.0.1",
    description="Data preprocessing for customer signup prediction",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Neuraldominator/customer-signup-prediction",
    author="Dominik Kessler",
    # author_email="name@mail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    extras_require={},
    python_requires="==3.8",
)