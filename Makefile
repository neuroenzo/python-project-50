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

tests:
	poetry run pytest -v -s -l tests

gendiff:
	poetry run gendiff

.PHONY: install build publish package-install lint tests gendiff
