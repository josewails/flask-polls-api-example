from app.exts import ma
from .models import Question

from marshmallow_sqlalchemy import auto_field


class QuestionCreateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Question

    text = auto_field()


class QuestionGetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        fields = ('id', 'text', 'date_created')
