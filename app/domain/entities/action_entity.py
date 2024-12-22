from dataclasses import dataclass


@dataclass(slots=True)
class ActionDM:
    _id: str | None = None
    email: str
    action_type: str
    details: str

