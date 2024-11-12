from mongoengine import Document, fields
from django.contrib.auth.hashers import make_password, check_password


class Profile(Document):

    username = fields.StringField(max_length=150, required=True)
    email = fields.EmailField(required=True)
    password = fields.StringField(required=True, unique=True)
    is_active = fields.BooleanField(default=True)
    care_taker = fields.BooleanField(default=False)
    health_card = fields.StringField(max_length=1000)
    backend = "users.auth_backend.MongoEngineBackend"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
