import os
import sys

from flask import Flask

from app.models.comments import all_post_comments
from app.models.friendship import all_friends
from app.models.likes import liked, disliked, len_post_likes, len_post_dislikes
from app.models.posts import all_user_post
from app.models.users import get_user_by_id

app = Flask(__name__)

app.secret_key = os.urandom(16)

settings = {}

# load settings from env
print('load settings from env')
env = dict(os.environ)
for setting in env:
    settings[setting] = env[setting]

try:
    from .local_settings import settings_local
    print('Successfully imported local settings, use it only for development')
except ImportError as e:
    pass

settings.update(settings_local)

from app.views import newsfeed, login, chat, profiles, posts, friends, comments, likes, notifications, tags, geolocation, search
from app.views.notifications import get_users_online_list