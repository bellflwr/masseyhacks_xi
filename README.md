# MasseyHacks 2025

## Development

### Environment

Make sure your have poetry installed, and run `poetry install`

Make sure you have the virtual environment enabled, and run `wsgi.py` to run the project.

If you are unsure if it enabled, you can run `poetry shell`, but your editor might enable it automatically.

### Pre-Commit

Before you commit make sure you run:

`ruff check . --fix`
To get a list of things you might want to fix, and fix them before commiting

AND

`ruff format .`
To format the code, this is really important to help reduce merge conflicts.