
from django.apps import AppConfig

default_app_config = 'leonardo_spirit.Config'


LEONARDO_APPS = [
    'leonardo_spirit',

    'djconfig',
    'spirit.core',
    'spirit.admin',
    'spirit.search',

    'spirit.user',
    'spirit.user.admin',
    'spirit.user.auth',

    'spirit.category',
    'spirit.category.admin',

    'spirit.topic',
    'spirit.topic.admin',
    'spirit.topic.favorite',
    'spirit.topic.moderate',
    'spirit.topic.notification',
    'spirit.topic.poll',  # todo: remove in Spirit v0.5
    'spirit.topic.private',
    'spirit.topic.unread',

    'spirit.comment',
    'spirit.comment.bookmark',
    'spirit.comment.flag',
    'spirit.comment.flag.admin',
    'spirit.comment.history',
    'spirit.comment.like',
    'spirit.comment.poll',
]

LEONARDO_PLUGINS = [
    ('leonardo_spirit.apps.spirit', 'Spirit Forum')
]

LEONARDO_AUTH_BACKENDS = [
    'spirit.user.auth.backends.UsernameAuthBackend',
    'spirit.user.auth.backends.EmailAuthBackend',
]

LEONARDO_CONTEXT_PROCESSORS = [
    'djconfig.context_processors.config',
]

LEONARDO_MIDDLEWARES = [
    'spirit.user.middleware.TimezoneMiddleware',
    'spirit.user.middleware.LastIPMiddleware',
    'spirit.user.middleware.LastSeenMiddleware',
    'spirit.user.middleware.ActiveUserMiddleware',
    'spirit.core.middleware.PrivateForumMiddleware',
    'djconfig.middleware.DjConfigMiddleware',
]

LEONARDO_ABSOLUTE_URL_OVERRIDES = {
    'spirit_category.category': 'leonardo_spirit.overrides.category',
    'spirit_topic.topic': 'leonardo_spirit.overrides.topic',
    'spirit_user.userprofile': 'leonardo_spirit.overrides.userprofile',
    'spirit_comment.comment': 'leonardo_spirit.overrides.comment',
}


class Config(AppConfig):
    name = 'leonardo_spirit'
    verbose_name = "leonardo-spirit"
