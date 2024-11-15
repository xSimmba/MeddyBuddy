from urllib.parse import quote_plus
from django.conf import settings
from mongo.models import User
from pymongo import MongoClient


class Mongo:
    def __init__(
        self,
        database: str = settings.MONGO_DB_NAME,
        host: str = settings.MONGO_HOST,
        password: str = settings.MONGO_PASSWORD,
        port: int = settings.MONGO_PORT,
        user: str = settings.MONGO_USER,
    ):
        self.default_database = database
        self.uri = "mongodb://%s:%s@%s:%i/" % (
            quote_plus(user),
            quote_plus(password),
            host,
            port,
        )

    def get_user(self, user_id: int) -> User:
        with MongoClient(self.uri) as client:
            user = client[self.default_database].users.find_one({"user_id": user_id})
            return User(**user)

    def set_user(self, user_id: int, is_caregiver: bool = False):
        with MongoClient(self.uri) as client:
            client[self.default_database].users.insert_one({"user_id": user_id})
            client[self.default_database].users.update_one(
                {"user_id": user_id}, {"$set": {"care_giver": is_caregiver}}
            )

    def update_user(self, user: User):
        with MongoClient(self.uri) as client:
            client[self.default_database].users.update_one(
                {"user_id": user["user_id"]}, {"$set": user.model_dump()}
            )

    def get_medication(self, medication_id: int) -> str:
        pass
