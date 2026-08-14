from sqlmodel import Field, SQLModel, UniqueConstraint


class Emotes(SQLModel, table=True):
    """An emote available during an edition, from Twitch or a third-party provider."""

    __table_args__ = (
        UniqueConstraint("provider", "emoteID", "edition", name="emotes"),
    )

    id:         int | None = Field(default=None, primary_key=True)
    name:       str
    provider:   str
    emoteID:    str
    emoteURL:   str
    count:      int
    edition:    int = Field(foreign_key="edition.id")