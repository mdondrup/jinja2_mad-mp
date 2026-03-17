#!/usr/bin/env python3
"""Render a Jinja2 template with data from a JSON file."""

import argparse
import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined


def render(template_path: str, data_path: str, output_path: str | None = None) -> str:
    """Load *data_path* (JSON) and render *template_path* (Jinja2).

    Returns the rendered string and optionally writes it to *output_path*.
    """
    template_file = Path(template_path)
    data_file = Path(data_path)

    env = Environment(
        loader=FileSystemLoader(str(template_file.parent)),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    template = env.get_template(template_file.name)

    with data_file.open(encoding="utf-8") as fh:
        data = json.load(fh)

    rendered = template.render(**data)

    if output_path:
        Path(output_path).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

    return rendered


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a Jinja2 template with data from a JSON file."
    )
    parser.add_argument(
        "template",
        nargs="?",
        default="template.j2",
        help="Path to the Jinja2 template file (default: template.j2)",
    )
    parser.add_argument(
        "data",
        nargs="?",
        default="data.json",
        help="Path to the JSON data file (default: data.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Write rendered output to this file instead of stdout",
    )
    args = parser.parse_args()

    try:
        render(args.template, args.data, args.output)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
