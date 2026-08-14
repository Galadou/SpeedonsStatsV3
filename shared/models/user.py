from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """A Twitch chatter, identified by their stable Twitch user ID."""

    userID:         int = Field(primary_key=True)
    name:           str
    color:          str
    isSubscriber:   bool
    isModo:         bool
    badgeTwitch:    str