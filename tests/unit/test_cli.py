from pathlib import Path

from catalogforge.__main__ import main

ROOT = Path(__file__).resolve().parents[2]


def test_check_config_command(capsys) -> None:

    code = main(
        [
            "check-config",
            "--config",
            str(ROOT / "configs" / "pilot.toml"),
        ]
    )

    output = capsys.readouterr()

    assert code == 0

    assert "CatalogForge configuration OK" in output.out

    assert '"retrieval_top_k": 20' in output.out


def test_check_config_missing_file(
    tmp_path: Path,
    capsys,
) -> None:

    code = main(
        [
            "check-config",
            "--config",
            str(tmp_path / "missing.toml"),
        ]
    )

    output = capsys.readouterr()

    assert code == 1

    assert "Configuration error" in output.err
