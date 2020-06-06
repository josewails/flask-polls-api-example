from flask_testing import TestCase

from app import create_app
from app.exts import db
from .factories import QuestionFactory

from faker import Faker

fake = Faker()


class BaseTest(TestCase):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

    def create_app(self):
        return create_app(self)

    def setUp(self):
        self.questions = [QuestionFactory() for _ in range(5)]
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class QuestionTests(BaseTest):

    def test_question_create(self):
        data = dict(
            text=fake.paragraph()
        )

        response = self.client.post('/questions', json=data)
        self.assert200(response)

    def test_question_list(self):
        response = self.client.get('/questions')
        self.assert200(response)
        self.assertEqual(len(self.questions), len(response.json))

    def test_question_detail(self):
        question = self.questions[0]
        print(question.date_created)
        response = self.client.get(f'/questions/{question.id}')
        self.assert200(response)
        self.assertEqual(question.id, response.json['id'])
