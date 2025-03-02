"""NewsAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_newsapi import streams


class TapNewsAPI(Tap):
    """NewsAPI tap class."""

    name = "tap-newsapi"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            title="API Key",
            description="The api key to authenticate against the API service",
        ),
        th.Property(
            "q",
            th.StringType,
            required=True,
            title="Query",
            description="A list of keywords or phrases to search for in the article title and body",
        ),
        th.Property(
            "sort_by",
            th.StringType,
            title="Sort By",
            default="relevancy",
            description="The order to sort the articles in. Possible options are 'relevancy', 'popularity', 'publishedAt'",
        ),
        th.Property(
            "from_date",
            th.DateTimeType,
            title="From Date",
            description="A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-02-23 or 2025-02-23T16:21:37)",
        ),
        th.Property(
            "to_date",
            th.DateTimeType,
            title="To Date",
            description="A date and optional time for the newest article allowed. This should be in ISO 8601 format (e.g. 2025-02-23 or 2025-02-23T16:21:37)",
        ),
        th.Property(
            "api_url",
            th.StringType,
            title="API URL",
            default="https://newsapi.org/v2",
            description="The url for the API service",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            title="User Agent",
            default="tap-newsapi",
            description=(
                "A custom User-Agent header to send with each request. Default is "
                "'<tap_name>/<tap_version>'"
            ),
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.NewsAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ArticlesStream(self),
        ]


if __name__ == "__main__":
    TapNewsAPI.cli()
