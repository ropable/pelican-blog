Title: Python virtualenv management with pyenv and Poetry
Date: 2020-11-26 0920
Slug: python-pyenv-poetry
Author: Ashley Felton
Summary: Python virtualenv management with pyenv and Poetry

This is a summary of the workflow for managing Python virtual environments using
more-modern tools than my usual combo of virtualenv and pip.

Links:

* Hypermodern Python setup: <https://cjolowicz.github.io/posts/hypermodern-python-01-setup/>
* Set up an awesome Python environment: <https://towardsdatascience.com/how-to-setup-an-awesome-python-environment-for-data-science-or-anything-else-35d358cc95d5>
* Overview of Python dependency management tools: <https://modelpredict.com/python-dependency-management-tools>
* pyenv: <https://github.com/pyenv/pyenv>
* pyenv installer: <https://github.com/pyenv/pyenv-installer>
* pyenv tutorial: <https://amaral.northwestern.edu/resources/guides/pyenv-tutorial>
* Poetry: <https://python-poetry.org/>

## Pyenv

Use **pyenv** to install different versions of Python on a host easily, and
enable easy switching between them. To install, follow the
[installation instructions](https://github.com/pyenv/pyenv#installation) or use
the automatic installer like so (installs to local user directory, not globally):

~~~bash
curl https://pyenv.run | bash
~~~

Add the following lines to your `.bashrc`:

~~~
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
~~~

Use pyenv to install different Python versions:

~~~bash
pyenv install 3.7.7
pyenv install 3.8.6
~~~

Note that the `install` command has a `--list` switch to display available
Python versions to be installed:

~~~bash
pyenv install --list | grep 3.9
  3.9.0a6
  3.9-dev
  miniconda-3.9.1
  miniconda3-3.9.1
~~~

Set a global installed Python version to be used by default:

~~~bash
pyenv global 3.8.6
~~~

Set a 'default' Python version to be used upon changing to a project directory:

~~~bash
pyenv local 3.7.7
~~~

Don't add the `.python-version` file to the repository (this is a local setting);
add it to `.gitignore` if necessary. If pyenv is configured properly, the
presence of `.python-version` will cause it to activate the virtualenv
automatically when you change into that directory.

Update pyenv like so (note this requires the pyenv-update plugin, installed by default
using the method outlined above):

~~~bash
penv update
~~~

## Poetry

pyenv comes with virtualenv but instead of that, use **Poetry** to manage virtual
environments and dependencies (it has better dependency tree management).

Install Poetry (installs to local user directory, not globally):

~~~bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
~~~

Add the following line to your `.bashrc`:

~~~
source $HOME/.poetry/env
~~~

Inside a project directory, initialise the project dependencies:

~~~bash
poetry init
~~~

Add the `pyproject.toml` file to the project repository. Use `poetry new` instead
to initialise a brand new project repository instead of `poetry init`.

Set up a new virtual environment for the project:

~~~bash
poetry install
~~~

Add the `poetry.lock` file the the project repository, as this keeps track of
installed library versions. Add new project dependencies (this will automatically
update `pyproject.toml` and `poetry.lock`):

~~~bash
poetry add requests
poetry add Django==3.0.5
postry add --dev ipython ipdb
~~~

List the Poetry-managed virtual environments available to the project:

~~~bash
poetry env list
poetry env info
~~~

Run python scripts in the virtual environment by preceding them with `poetry run`:

~~~bash
poetry run python myscript.py
~~~

## Update project Python version

Let's say that you want to update the Python version from 3.7 to 3.8, and you're using
pyenv and Poetry like you should be. Assuming that you've that you've installed the new
Python version using pyenv, carry out the following process to upgrade the
version of Python defined in the project `pyproject.toml` file.

Delete the local project venv:

~~~bash
poetry env list
poetry env remove <venv name>
~~~

Set a new local Python version in the project (using Python 3.8.6 in this example):

~~~bash
pyenv local 3.8.6
~~~

Delete your project poetry.lock file (we'll recreate it in a second anyway), and update your pyproject.toml file
to set the new Python version under `[tool.poetry.dependencies]`, e.g.:

    python = "^3.8"

Create a new project venv using Poetry (this should recreate the poetry.lock file):

~~~bash
poetry install
~~~

Test and confirm that your project works with the new version of Python.
