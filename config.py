import os

DEBUG = True  # enable development environment

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# database vars
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other

THREADS_PER_PAGE = 2

# Enables protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# user a secure, secret key for signing the data
CSRF_SESSION_KEY = 'fd07e726dd3e85b485cad1705f613463992f47f2a91985b469373c4453576275'

# secret key for signing cookies
SECRET_KEY = 'ee3ff14dfd08301c7464dfbbcf1e2a31b957d0e94faa27ad3a7a5b5c0917ff49'
