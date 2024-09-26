install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
format:
	black */*.py
	
lint:
	pylint --disable=R,C tests/*.py router/*.py
	
test:
	python -m pytest -vv --cov=router tests/test_*.py
	
all: install format lint test