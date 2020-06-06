from app.exts import db
from flask_testing import TestCase
from app import create_app

from .factories import UserFactory
from .models import User


class BaseTest(TestCase):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"

    def create_app(self):
        return create_app(self)

    def setUp(self):
        self.user = UserFactory()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class UserTests(BaseTest):

    def test_decode_auth_token(self):
        auth_token = User.encode_auth_token(self.user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), self.user.id)
