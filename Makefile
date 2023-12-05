install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C first.py

test:
	python -m pytest -vv --cov=first test_first.py