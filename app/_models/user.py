from app import app
from app._models import BaseModel


class User(BaseModel):

    def __init__(self):
        self = BaseModel('users')



user = User()

