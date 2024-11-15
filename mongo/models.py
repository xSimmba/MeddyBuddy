from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int
    care_giver: bool = Field(default=False)


# class Medication(BaseModel):
#     medication_id = int
#     commentary = str