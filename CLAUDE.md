# AI-Augmented SDLC

## Stack
- Backend : Python 3.12, FastAPI, Pydantic
- Base de données : PostgreSQL
- Conteneurisation : Docker Compose
- Tests : Pytest
- Lint : Ruff
- CI/CD : GitHub Actions

## Règles
- Écrire des tests pour toute nouvelle fonctionnalité.
- Ne jamais committer de secret en clair.
- Toute modification non triviale commence par un plan validé.
- Toute PR doit passer lint + tests avant merge.

## Commandes
- Tests : `uv run pytest`
- Lint : `uv run ruff check .`
- App locale : `docker compose up`
