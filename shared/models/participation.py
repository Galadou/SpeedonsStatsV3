from sqlmodel import Field, SQLModel, UniqueConstraint


class Participation(SQLModel, table=True):
    """Links a user to an edition they took part in."""

    __table_args__ = (
        UniqueConstraint("user", "edition", name="participation"),
    )

    id:         int | None = Field(default=None, primary_key=True)
    user:       int = Field(foreign_key="user.userID")
    edition:    int = Field(foreign_key="edition.id")