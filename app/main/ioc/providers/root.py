import motor.motor_asyncio
from dishka import Provider, Scope, from_context, provide
from faststream.kafka import KafkaBroker

from app.application.interfaces.uow_interface import UnitOfWork
from app.infrastructure.adapters.uow import MongoUnitOfWork
from app.main.config import Config


class RootProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)
    broker = from_context(provides=KafkaBroker, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_client(
        self,
    ):
        return motor.motor_asyncio.AsyncIOMotorClient(self.config.mongodb.uri)

    @provide(scope=Scope.APP)
    def get_collection(
        self,
        config: Config,
        client: motor.motor_asyncio.AsyncIOMotorClient,
    ) -> motor.motor_asyncio.AsyncIOMotorCollection:
        db = client[config.mongodb.db_name]
        collection = db[config.mongodb.collection_name]
        return collection

    unit_of_work = provide(
        MongoUnitOfWork,
        scope=Scope.REQUEST,
        provides=UnitOfWork,
    )
