#!/usr/bin/env bash
pipenv run isort --recursive --diff wordle_main
pipenv run black --check .
pipenv run flake8 wordle_main
pipenv run mypy wordle_main
pipenv run pytest --cov=wordle_main --cov-fail-under=90     