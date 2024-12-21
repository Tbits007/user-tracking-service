import motor.motor_asyncio

from app.main.config import MongoDBConfig


def new_client(
        config: MongoDBConfig
    ) -> motor.motor_asyncio.AsyncIOMotorClient:
    """Create a new MongoDB client."""
    return motor.motor_asyncio.AsyncIOMotorClient(config.uri())


def new_database(
        client: motor.motor_asyncio.AsyncIOMotorClient,
        name: str
    ) -> motor.motor_asyncio.AsyncIOMotorDatabase:
    """Create a new MongoDB database."""
    return client[name]


def new_collection(
        database: motor.motor_asyncio.AsyncIOMotorDatabase,
        name: str
    ) -> motor.motor_asyncio.AsyncIOMotorCollection:
    """Create a new MongoDB collection."""
    return database[name]