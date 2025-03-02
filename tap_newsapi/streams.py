"""Stream type classes for tap-newsapi."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_newsapi.client import NewsAPIStream

# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ArticlesStream(NewsAPIStream):
    """NewsAPI Article stream."""

    name = "articles"
    path = "/everything"
    primary_keys: t.ClassVar[list[str]] = ["source_id", "author", "title"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property(
            "source_id",
            th.StringType,
            description="The ID of the source, e.g. 'cnn'",
        ),
        th.Property(
            "source_name",
            th.StringType,
            description="The display name of the source, e.g. 'CNN'",
        ),
        th.Property(
            "author",
            th.StringType,
            description="The author of the article",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The headline or title of the article",
        ),
        th.Property(
            "description",
            th.StringType,
            description="A description or snippet from the article",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The URL to the article",
        ),
        th.Property(
            "url_to_image",
            th.StringType,
            description="The URL to an image associated with the article",
        ),
        th.Property(
            "published_at",
            th.DateTimeType,
            description="The date and time the article was published",
        ),
        th.Property(
            "content",
            th.StringType,
            description="The full text of the article",
        ),
    ).to_dict()
