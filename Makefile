.PHONY: install format lint typecheck progress check

install:
	pip install -r requirements-dev.txt

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
