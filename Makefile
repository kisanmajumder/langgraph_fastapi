.PHONY: install test

install:
	pip install -r requirements.txt

test:
	python -m pytest -vv unit_test.py