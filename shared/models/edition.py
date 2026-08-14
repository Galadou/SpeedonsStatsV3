from datetime import datetime

from sqlmodel import Field, SQLModel


class Edition(SQLModel, table=True):
    """One Speedons event edition, delimited by its start and end dates."""

    id:         int | None = Field(default=None, primary_key=True)
    edition:    str = Field(unique=True)
    start:      datetime
    end:        datetime