Title: Python virtualenv management with pyenv and Poetry
Date: 2020-06-08 0920
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
* Poetry: <https://python-poetry.org/>

## Pyenv

Use **pyenv** to install different versions of Python on a host easily, and
enable easy switching between them. Install pyenv:

~~~bash
curl https://pyenv.run | bash
~~~

Add the following lines to `.bashrc`:

~~~
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
~~~

Use pyenv to install different Python versions:

~~~bash
pyenv install 3.7.7
pyenv install 3.8.2
~~~

Set a 'default' Python version to be used upon changing to a project directory:

~~~bash
pyenv local 3.7.7
~~~

Don't add the `.python-version` file to the repository (this is a local setting);
add it to `.gitignore` if necessary. If pyenv is configured properly, the
presence of `.python-version` will cause it to activate the virtualenv
automatically when you change into that directory.

## Poetry

pyenv comes with virtualenv but instead of that, use **Poetry** to manage virtual
environments and dependencies. Install Poetry:

~~~bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
~~~

Add the following line to `.bashrc`:

~~~
source ~/.poetry/env
~~~

Inside the project directory, initialise the project dependencies:

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
