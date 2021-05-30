https://qiita.com/ttsubo/items/5fea7c0a1f9fc868dc1f


# How to setup development environment

`$ pipenv --python 3`

`$ pipenv install --dev pytest`
`$ pipenv install graphviz`

# How to create a library and upload it to PyPI

1. define external dependencies; `<projectdir>/requirements.txt` by `pipenv run pip freeze > requirements.txt`
2. configure the distributable by setup.py; `<projectdir>/setup.py`
3. add/exclude resources other than *.py; `<projectdir>/MANIFEST.ini`
4. create the library; `$ pipenv run python setup.py sdist`
5. you will find the distributable under the dist dir.
