lint:
	pipenv run pylint --rcfile=setup.cfg transformers_vectorizer

test:
	pipenv run pytest tests

requirements:
	pipenv lock -r > requirements.txt

build-docker: requirements
	docker build -t radcheb/transformers-vectorizer:0.0.1 .
