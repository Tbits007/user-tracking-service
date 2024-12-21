import motor.motor_asyncio
from bson import ObjectId
from app.application.interfaces.activity_interface import (
    ActivitySaver,
    ActivityReader,
)
from app.domain.entities.activity_entity import ActivityDM


class ActivityGateway(
    ActivitySaver,
    ActivityReader,
):
    def __init__(
            self,
            client: motor.motor_asyncio.AsyncIOMotorClient,
            db: motor.motor_asyncio.AsyncIOMotorDatabase,
            collection: motor.motor_asyncio.AsyncIOMotorCollection,
        ) -> None:
        self.client = client
        self.db = db
        self.collection = collection

    async def save(self, activity: ActivityDM) -> ActivityDM | None:
        """Save activity to the database."""
        activity_dict = activity.dict()
        result = await self.collection.insert_one(activity_dict)
        if result.inserted_id:
            activity.id = str(result.inserted_id)
            return activity
        return None

    async def read_by_id(self, _id: str) -> ActivityDM | None:
        """Read activity by _id."""
        activity_data = await self.collection.find_one({"_id": ObjectId(_id)})
        if activity_data:
            return ActivityDM(**activity_data)
        return None
