import datetime

from app.exts import db
from .models import User
from app.core.utils import generate_uuid, generate_email, generate_password

import factory
from factory.alchemy import SQLAlchemyModelFactory

from faker import Faker

fake = Faker()


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: f"{generate_uuid()}{n}")
    email = factory.Sequence(lambda n: generate_email())
    password = factory.Sequence(lambda n: generate_password())
    created_on = datetime.datetime.utcnow()
