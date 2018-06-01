.PHONY: clean-pyc clean-build clean

clean: clean-build clean-pyc

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:
	-@find . -name '*.pyc' -follow -print0 | xargs -0 rm -f &> /dev/null
	-@find . -name '*.pyo' -follow -print0 | xargs -0 rm -f &> /dev/null
	-@find . -name '__pycache__' -type d -follow -print0 | xargs -0 rm -rf &> /dev/null

format:
	black flake8_csv.py

lint:
	flake8 flake8_csv

build: clean  ## Create distribution files for release
	python setup.py sdist bdist_wheel

release: build  ## Create distribution files and publish to PyPI
	python setup.py check -r -s
	twine upload dist/*

sdist: clean  ##sdist Create source distribution only
	python setup.py sdist
	ls -l dist
