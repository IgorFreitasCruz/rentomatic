from typing import Optional

from sqlmodel import Field, SQLModel, Column, String


class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    size: int
    price: float
    longitude: float
    latitude: float
