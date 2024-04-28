from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

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
    install_requires=["chardet==5.2.0",
                     # "charset-normalizer==3.3.2",
                      "ftfy==6.2.0",
                      "fuzzywuzzy==0.18.0",
                     # "Levenshtein==0.25.1"
                      "ipykernel==6.29.4",
                      "ipython==8.12.3",
                      "matplotlib==3.7.5",
                      "numpy==1.24.4",
                      "pandas==2.0.3",
                      "seaborn==0.13.2",
                      #jupyter_client==8.6.1
                      #jupyter_core==5.7.2
                      #jupyterlab_pygments==0.3.0
                      #matplotlib-inline==0.1.7
                      #rapidfuzz==3.8.1
    ],
    extras_require={},
    python_requires="==3.8",
)