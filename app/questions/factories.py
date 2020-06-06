from datetime import datetime

from .models import Question
from app.exts import db
from app.core.utils import generate_uuid

import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker

fake = Faker()


class QuestionFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Question
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: f"{generate_uuid()}{n}")
    text = fake.paragraph()
    date_created = datetime.utcnow()
