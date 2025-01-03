from typing import Any, Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.client_session import ClientSession

from app.application.interfaces.uow_interface import UnitOfWork


class MongoUnitOfWork(UnitOfWork):
    def __init__(self, client: AsyncIOMotorClient):
        self._client = client
        self._session: Optional[ClientSession] = None

    async def __aenter__(self) -> "MongoUnitOfWork":
        self._session = await self._client.start_session()
        self._session.start_transaction()
        return self

    async def __aexit__(self, exc_type: Optional[type], exc: Optional[BaseException], tb: Optional[Any]) -> None:
        await self.rollback()

    async def commit(self) -> None:
        if self._session:
            await self._session.commit_transaction()

    async def rollback(self) -> None:
        if self._session:
            await self._session.abort_transaction()
