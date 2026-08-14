from datetime import datetime

from sqlmodel import Field, SQLModel


class Messages(SQLModel, table=True):
    """A single chat message, stored as raw text exactly as received."""

    id:         int | None = Field(default=None, primary_key=True)
    user:       int = Field(foreign_key="user.userID")
    text:       str
    date:       datetime
    edition:    int = Field(foreign_key="edition.id")