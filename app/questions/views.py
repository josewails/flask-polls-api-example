from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from .schemas import QuestionCreateSchema, QuestionGetSchema
from .models import Question
from app.exts import db

from marshmallow import ValidationError
from flasgger import SwaggerView

questions = Blueprint('questions', __name__, url_prefix='/questions')

question_create_schema = QuestionCreateSchema()
question_get_schema = QuestionGetSchema()
questions_get_schema = QuestionGetSchema(many=True)


class QuestionCreate(SwaggerView):
    tags = ['questions']
    parameters = QuestionCreateSchema
    responses = {
        200: {
            "description": "Question Created",
            "schema": QuestionGetSchema
        }
    }

    validation = True

    def post(self):

        request_json = request.get_json(force=True)

        try:
            data = question_create_schema.load(request_json)

        except ValidationError as err:
            res = dict(
                errors=err.messages
            )

            return make_response(jsonify(res), 400)

        question = Question(**data)
        db.session.add(question)
        db.session.commit()
        res = question_get_schema.dump(question)

        return make_response(jsonify(res), 200)


class QuestionList(SwaggerView):
    tags = ['questions']

    responses = {
        200: {
            'description': "Question List",
            "schema": {
                "type": "array",
                "items": QuestionGetSchema
            }
        }
    }

    def get(self):
        query = Question.query.all()
        res = questions_get_schema.dump(query)
        return make_response(jsonify(res), 200)


class QuestionDetail(SwaggerView):
    tags = ['questions']
    responses = {
        200: {
            'description': 'Question Detail',
            "schema": QuestionGetSchema
        }
    }

    def get(self, question_id):
        query = Question.query.filter_by(id=question_id).first()
        res = question_get_schema.dump(query)
        return make_response(jsonify(res), 200)


questions.add_url_rule('', view_func=QuestionCreate.as_view('question_create'), methods=['POST', ])
questions.add_url_rule('', view_func=QuestionList().as_view('question_list'), methods=['GET'])
questions.add_url_rule('/<question_id>', view_func=QuestionDetail().as_view('question_detail'), methods=['GET'])
