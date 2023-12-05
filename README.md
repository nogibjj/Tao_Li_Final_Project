[![Python template with Github Actions](https://github.com/drktao/python-template/actions/workflows/main.yml/badge.svg)](https://github.com/drktao/python-template/actions/workflows/main.yml)

# python-template
The purpose of this project is to make a python template for use in IDS 706 for all subsequent python-based projects. The following are the important files contained in this repo:

1. `main.yml` - Github Actions for install, test, format, and lint.
2. `Makefile` - `make` commands for install, test, format, and lint
3. `first.py` - python script containing a function definition
4. `test_first.py` - python script containing tests for `first.py`
5. `requirements.txt` - contains names of required packages for installation.

## Instructions
Use Github codespaces, which will allow for a container to be built with the required packages, as detailed in requirements.txt. In the terminal, use `make install` to install the necessary packages from `requirements.txt`. Use `make format` to format the code using python black and `make lint` to lint the code. Finally, use `make test` to run the test cases from `test_first.py`. One can also directly run the two python scripts in this repo using `python first.py` and `python test_first.py`. 


