from app.application.dtos.activity_dtos import CreateActivityDTO
from app.application.interfaces import activity_interface
from app.domain.entities.activity_entity import ActivityDM


class GetActivityInteractor:
    def __init__(
        self,
        activity_gateway: activity_interface.ActivityReader,
    ) -> None:
        self._activity_gateway = activity_gateway

    async def __call__(self, _id: str) -> ActivityDM | None:
        return await self._activity_gateway.read_by_id(_id)


class CreateActivityInteractor:
    def __init__(
        self,
        activity_gateway: activity_interface.ActivitySaver,
    ) -> None:
        self._activity_gateway = activity_gateway

    async def __call__(self, dto: CreateActivityDTO) -> ActivityDM | None:
        activity = ActivityDM(
            email=dto.email,
            action_type=dto.action_type,
            details=dto.details, 
        )
        return await self._activity_gateway.save(activity)