.PHONY: install format lint typecheck progress check new

install:
	pip install -r requirements-dev.txt

new:
	python scripts/new_solution.py

format:
	ruff format .

lint:
	ruff format --check .
	ruff check .

typecheck:
	./scripts/typecheck.sh

progress:
	python scripts/update_progress.py

check: lint typecheck
	python scripts/update_progress.py --check
