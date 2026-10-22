"""CatalogForge development CLI."""

import argparse
import json
import sys
import tomllib
from collections.abc import Sequence
from pathlib import Path

from pydantic import ValidationError

from catalogforge.config import load_config


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser(
        prog="catalogforge",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    check = subparsers.add_parser(
        "check-config",
        help="Validate the pilot configuration",
    )

    check.add_argument(
        "--config",
        type=Path,
        default=Path("configs/pilot.toml"),
    )

    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)

    except (
        OSError,
        tomllib.TOMLDecodeError,
        ValidationError,
    ) as exc:
        print(
            f"Configuration error: {exc}",
            file=sys.stderr,
        )

        return 1

    print("CatalogForge configuration OK")

    print(
        json.dumps(
            config.model_dump(mode="json"),
            indent=2,
            sort_keys=True,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
