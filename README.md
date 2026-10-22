# CatalogForge

Intelligent Product Identity Resolution at Scale.

CatalogForge is a machine learning platform for reconciling
noisy supplier catalogs against a master product catalog.

## Product Objective

Transform inconsistent supplier records into:

- MATCH
- REVIEW
- NO_MATCH

The system combines candidate retrieval, supervised matching,
confidence-based decision policies, and human review.

## Technology Stack

- Python 3.12
- uv
- Polars
- DuckDB
- Parquet
- RapidFuzz
- LightGBM (planned)
- SQLite FTS5 (planned)
- FastAPI (planned)
- PostgreSQL (planned)
- React + TypeScript (planned)

## Getting Started

Install dependencies:

```bash
uv sync
```

Verify package installation:

```bash
uv run python -c "import catalogforge; print('OK')"
```

Validate configuration:

```bash
uv run python -m catalogforge check-config
```

## Development

Run unit tests:

```bash
uv run pytest -q
```

Run lint:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

Format code:

```bash
uv run ruff format .
```

## Repository Layout

- `apps/api/` — Backend API
- `apps/web/` — Frontend application
- `src/catalogforge/data/` — Data ingestion and normalization
- `src/catalogforge/ml/` — Training and evaluation
- `src/catalogforge/search/` — Candidate retrieval
- `src/catalogforge/serve/` — Inference and decision policies
- `src/catalogforge/jobs/` — Batch processing
- `configs/` — Experiment configurations
- `tests/` — Automated tests
- `reports/` — Evaluation and benchmark reports

## Development Roadmap

Day 1: Data engineering and quality audit.

Day 2: Candidate generation and retrieval.

Day 3: Machine learning and decision policies.

Day 4: Backend API and batch processing.

Day 5: Fullstack reconciliation workbench.

Day 6: Performance engineering and benchmarking.

Day 7: Deployment, CI, documentation and demo.

## Status

Sprint 1 / CF-01 — Project initialization.