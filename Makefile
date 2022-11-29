lint:
	poetry run flake8 .

install:
	poetry install

run:
	poetry run uvicorn text_finder.server:app --reload