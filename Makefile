PYTHON=python3

SEARCH=
.PHONY: clean
.PHONY: build
.PHONY: testpypi

clean:
	-@rm -rf build/
	-@rm -rf dist/
	-@rm -rf *.egg-info
	-@rm -rf .pytest_cache/

build:
	@$(PYTHON) setup.py sdist bdist_wheel

testpypi:
	@$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
