from sqlmodel import Field, SQLModel, UniqueConstraint


class UserEmoteCount(SQLModel, table=True):
    """How many times a user used a given emote."""

    __table_args__ = (
        UniqueConstraint("user", "emotes", name="user_emote_count"),
    )

    id:         int | None = Field(default=None, primary_key=True)
    user:       int = Field(foreign_key="user.userID")
    emotes:     int = Field(foreign_key="emotes.id")
    count:      int