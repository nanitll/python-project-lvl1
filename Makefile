
make install: poetry install
make brain-games: poetry run brain-games
make build: poetry build
make publish: poetry publish --dry-run
make package-install: python3 -m pip install -user dist/*.whl
make lint: poetry run flake8 brain_games