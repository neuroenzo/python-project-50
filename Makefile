install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v -s -l

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

gendiff:
	poetry run gendiff

.PHONY: install build publish package-install lint test selfcheck check  gendiff
