define USAGE
Super awesome hand-crafted build system ⚙️

Commands:
	init      Install Python dependencies with pipenv
	test      Run linters, test db migrations and tests.
	serve     Run app in dev environment.
endef

export USAGE
help:
	@echo "$$USAGE"

init:
	pip3 install pipenv
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=. pytest

serve:
	FLASK_APP=api/main.py pipenv run flask run