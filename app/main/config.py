from os import environ as env

from pydantic import BaseModel, Field


class MongoDBConfig(BaseModel):
    username: str = Field(alias="MONGODB_USERNAME")
    password: int = Field(alias="MONGODB_PASSWORD")

    def uri(self):
        return f"mongodb+srv://{self.username}:{self.password}@cluster0.ofbf3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


class Config(BaseModel):
    mongodb: MongoDBConfig = Field(default_factory=lambda: MongoDBConfig(**env))