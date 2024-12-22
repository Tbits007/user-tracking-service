from app.application.dtos.action_dtos import CreateActionDTO
from app.application.interactors.action_interactors import CreateActionInteractor
from app.infrastructure.database.broker import new_broker
from dishka.integrations.base import FromDishka

from app.presentation.controllers.schemas import ActionSchema 


broker = new_broker()


@broker.subscriber("user-service-actions")
async def handle_user_actions(
    data: ActionSchema,
    interactor: FromDishka[CreateActionInteractor]
    ) -> None:
    dto = CreateActionDTO(
        email=data.email,
        action_type=data.action_type,
        details=data.details,
        )
    await interactor(dto)
