Title: Python virtualenv management with pyenv and Poetry
Date: 2020-06-08 0920
Slug: python-pyenv-poetry
Author: Ashley Felton
Summary: Python virtualenv management with pyenv and Poetry

This is a summary of the workflow for managing Python virtual environments using
more-modern tools than my usual combo of virtualenv and pip.

Links:

* Hypermodern Python setup: <https://cjolowicz.github.io/posts/hypermodern-python-01-setup/>
* Overview of Python dependency management tools: <https://modelpredict.com/python-dependency-management-tools>
* pyenv: <https://github.com/pyenv/pyenv>
* pyenv installer: <https://github.com/pyenv/pyenv-installer>
* Poetry: <https://python-poetry.org/>

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

Install Poetry:

~~~bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
~~~

## Set up a project virtualenv

Inside an existing project repository, create a new named virtualenv using an installed version of Python:

~~~bash
pyenv virtualenv 3.7.7 myproject
~~~

Don't add the `.python-version` file to the repository (this is a local setting);
add it to `.gitignore` if necessary. If pyenv is configured properly, the
presence of `.python-version` will cause it to activate the virtualenv
automatically when you change into that directory.

Inside the project directory, initialise the project dependencies:

~~~bash
poetry init
~~~

Add the `pyproject.toml` file to the repository. Use `poetry new` to initialise a
brand new project repository instead of `poetry init`.

Use Poetry to install project dependencies (use `--no-dev` to skip dev
dependencies):

~~~bash
poetry install
poetry install --no-dev
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

If the virtualenv is activated, you should be able to run scripts as usual:

~~~bash
python --version
python myscript.py
~~~
