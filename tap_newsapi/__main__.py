"""NewsAPI entry point."""

from __future__ import annotations

from tap_newsapi.tap import TapNewsAPI

TapNewsAPI.cli()
