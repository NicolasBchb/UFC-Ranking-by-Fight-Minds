# Developper

## Recreating the environment
Before starting developping, you need to recreate the python environment for this package. Please follow these steps : 
- Create a conda environment with the following command:

`conda create -n env_fmranker python=3.10 -y`

- Activate conda environment:

`conda activate env_fmranker`

- Launch the create_env function in `codepal.py`. This will install the packages in the requirement (in setup.cfg) and the local fmranker package as editable for an easier development.

`python codepal.py create_env -e env_fmranker`

If you need to add another package in fmranker, please write it in the setup.cfg file, with a pinned version.


The fmranker package files are located in core_module/fmranker.

## Respecting code standards

To help respect the code standard, the codepal.py at the root level contains helper functions.

Example : `python codepal.py format`

this will format the code (black+isort) in place.

you can also run the other steps of the CI : pytest, pylint, mypy, bandit.

