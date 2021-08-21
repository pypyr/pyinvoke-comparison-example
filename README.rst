==================================
pypyr-to-invoke-comparison-example
==================================

This project takes existing pypyr_ CI/CD stuff and shows alternative implementation of the same using invoke_.

The CI/CD tasks are inspired from those, used in pypyr package itself.

.. _pypyr: https://pypyr.io/
.. _invoke: http://docs.pyinvoke.org

The repo includes minimal example of python package named arbpackage.

Python package arbpackage
=========================
The arbpackage is very simple python package, which does nothing special apart from allowing us to build it and exercise on it various CI/CD tasks.

The package is using following design decisions (rewriting CI/CD to other ones shall be easy):

- using setup.py and setuptools
- version management: version is hard coded into arbpackage/version.py module as value of `__version__` variable. Value is changed using bumpversion_ tool.
- tests are based on pytest_ and are all located in dedicated test suite directory tests.
- coding standards: code shall pass flake8 linter checks.
- linted package metadata: the package itself shell pass simple metadata check using

.. _bumpversion: https://github.com/peritus/bumpversion
.. _pytest: https://docs.pytest.org

Pipeline `build`
================
When you call `pypyr ops/build` or `pypyr ops/build package` or `pypyr ops/build package publish`, following commands are called:

Lint python package metadata::

  $ python setup.py -m -s

Lint the code::

  $ flake8

When running tests locally::

  $ pytest --cov=arbpackage --cov-report term-missing tests

When running the tests on GitHub::

  $ pytest --cov=arbpackage --cov-report term-missing --cov-report .test-results/codecoverage/coverage.xml --junitxml=.test-results/testresults/junitresults.xml tests
  $ codecov

Optionally, build the package itself::

  $ python setup.py bdist_wheel sdist
  $ twine check dist/*

Optionally, publish the package to pypi or to a private pypi. Assuming version 0.1.1::

  # upload the package
  $ twine upload dist/arbpackage-0.1.1*
  # uninstall currently installed package
  $ pip uninstall -y arbpackage
  # wait a moment
  $ sleep 10
  # try to install the new version
  $ pip install --upgrade --no-cache-dir arbpackage==0.1.1
  # assert the newly published package version is the one expected (using some python tricks)
  # install the package in editable mode for development again
  $ pip install -e .

Pipeline `bump`
===============
When you call `pypyr ops/bump major`, `pypyr ops/bump minor` or `pypyr ops/bump patch`, following commands are called (assuming `patch` variant):

Call the build pipeline incl. the package step to ensure all is linted, tested and the package exists.

Then::

  $ bumpversion --no-tag  --commit patch
  $ git push
  # finally print the new version somehow

Pipeline `tag`
==============
When you call `pypyr ops/tag`, following commands and actions take place:

Print current version (using some python tricks).

  # (if running locally, make sure local branch has latest tags from origin
  $ git pull --tags
Then continue::

  # check, if the tag already exists
  $ git tag -l "v0.1.1"
  # stop, if the tag alrady exists
  # create the tag
  $ git tag "v0.1.1"
  # if on GitHub, configure git to use proper identities
  $ git config user.name github-actions
  $ git config user.email github-actions@github.com
  # push new tag to origin
  $ git push --tags

Using invoke
============
See `ops_invoke/README.rst` for description, how to do these things when implemented by `invoke_`





