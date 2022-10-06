.PHONY: test

test:
	@poetry run coverage run -m py.test -v -s tests
	@poetry run coverage report -m

run:
	@poetry run uvicorn app.main:app