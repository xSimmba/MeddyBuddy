from mongoengine import Document, fields
from users.models import Profile


class Medication(Document):
    id = fields.IntField(primary_key=True)
    user = fields.ReferenceField(Profile)
    name = fields.StringField(max_length=150)
    dosage = fields.IntField()
    instructions = fields.StringField()
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)
