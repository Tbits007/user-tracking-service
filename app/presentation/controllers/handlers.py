from dishka.integrations.base import FromDishka
from faststream.kafka import KafkaRouter

from app.application.dtos.action_dtos import CreateActionDTO
from app.application.interactors.action_interactors import CreateActionInteractor
from app.presentation.controllers.schemas import ActionSchema

actions = KafkaRouter()


@actions.subscriber("user-service-actions")
async def handle_user_actions(data: ActionSchema, interactor: FromDishka[CreateActionInteractor]) -> None:
    dto = CreateActionDTO(
        email=data.email,
        action_type=data.action_type,
        details=data.details,
    )
    await interactor(dto)
