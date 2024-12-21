from dataclasses import dataclass


@dataclass(slots=True)
class CreateActivityDTO:
    email: str
    action_type: str
    details: str | None = None

