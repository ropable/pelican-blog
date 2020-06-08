Title: Python virtualenv management with pyenv and Poetry
Date: 2020-06-08 0920
Slug: python-pyenv-poetry
Author: Ashley Felton
Summary: Python virtualenv management with pyenv and Poetry

This is a summary of the workflow for managing Python virtual environments using
more-modern tools that my using combo of virtualenv and pip.

Links:

* Hypermodern Python setup: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
* Overview of Python dependency management tools: https://modelpredict.com/python-dependency-management-tools
* pyenv: https://github.com/pyenv/pyenv
* pyenv installer: https://github.com/pyenv/pyenv-installer
* Poetry: https://python-poetry.org/

Easiest install of pyenv:

~~~bash
curl https://pyenv.run | bash
~~~

Add the following lines to `~.bashrc`:

~~~
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
~~~

User pyenv to install different Python versions locally:

~~~bash
pyenv install 3.7.7
pyenv install 3.8.2
~~~

Inside a project repository, activate and use an installed version of Python:

~~~bash
pyenv local 3.7.7
~~~

Add the `.python-version` file to the repository. Install Poetry:

~~~bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
~~~

Inside an existing project repository, initialise the project dependencies:

~~~bash
poetry init
~~~

Add the `pyproject.toml` file to the repository. Use `poetry new` to initialise a
new project repository instead of `poetry init`.

Use Poetry to create a virtual environment and install any dependencies:

~~~bash
poetry install
poetry install --no-dev
~~~

Add project dependencies (this will automatically update `pyproject.toml`):

~~~bash
poetry add requests
poetry add Django==3.0.5
postry add --dev ipython
~~~

Add the `poetry.lock` file to the repository. Invoke `poetry run python` to make
use of an installed Python version using the virtualenv:

~~~bash
poetry run python --version
poetry run python myscript.py
~~~

List the Poetry-managed virtual environments available to the project:

~~~bash
poetry env list
poetry env info
~~~
