import uuid
import dataclasses
from typing import Dict


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, kwargs: Dict):
        return cls(**kwargs)

    def to_dict(self):
        return dataclasses.asdict(self)
