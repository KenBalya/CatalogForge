"""Typed runtime configuration shared by CatalogForge components."""

import tomllib
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )


class RunConfig(StrictModel):
    seed: int = Field(ge=0)


class PilotConfig(StrictModel):
    master_catalog_limit: int = Field(gt=0)

    query_limit: int = Field(gt=0)

    retrieval_top_k: int = Field(gt=0)


class PathsConfig(StrictModel):
    raw_dir: Path

    staging_dir: Path

    processed_dir: Path

    artifacts_dir: Path

    @field_validator(
        "raw_dir",
        "staging_dir",
        "processed_dir",
        "artifacts_dir",
    )
    @classmethod
    def require_relative_path(cls, value: Path) -> Path:

        if value.is_absolute() or ".." in value.parts:
            raise ValueError("Data and artifact paths must be project-relative")

        return value


class CatalogForgeConfig(StrictModel):
    run: RunConfig

    pilot: PilotConfig

    paths: PathsConfig


def load_config(path: Path) -> CatalogForgeConfig:
    """
    Load and validate a CatalogForge TOML configuration.

    Relative paths are interpreted from the repository root
    by pipeline consumers.
    """

    with path.open("rb") as file:
        payload = tomllib.load(file)

    return CatalogForgeConfig.model_validate(payload)
