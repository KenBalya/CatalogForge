from pathlib import Path

import pytest
from pydantic import ValidationError

from catalogforge.config import CatalogForgeConfig, load_config


ROOT = Path(__file__).resolve().parents[2]


def test_sample_config_loads() -> None:

    config = load_config(ROOT / "configs" / "pilot.toml")

    assert config.run.seed == 42

    assert config.pilot.master_catalog_limit == 100000

    assert config.pilot.retrieval_top_k == 20

    assert config.paths.raw_dir == Path("data/raw")


def test_invalid_master_limit_is_rejected() -> None:

    valid = load_config(ROOT / "configs" / "pilot.toml")

    payload = valid.model_dump()

    payload["pilot"]["master_catalog_limit"] = 0

    with pytest.raises(ValidationError):
        CatalogForgeConfig.model_validate(payload)


def test_path_traversal_is_rejected() -> None:

    valid = load_config(ROOT / "configs" / "pilot.toml")

    payload = valid.model_dump()

    payload["paths"]["raw_dir"] = "../outside"

    with pytest.raises(ValidationError):
        CatalogForgeConfig.model_validate(payload)


def test_missing_config_raises(tmp_path: Path) -> None:

    with pytest.raises(FileNotFoundError):
        load_config(tmp_path / "missing.toml")
