from __future__ import unicode_literals

ST_TOPIC_PRIVATE_CATEGORY_PK = 1

ST_RATELIMIT_ENABLE = True
ST_RATELIMIT_CACHE_PREFIX = 'srl'
ST_RATELIMIT_CACHE = 'default'

ST_NOTIFICATIONS_PER_PAGE = 20

ST_MENTIONS_PER_COMMENT = 30

ST_YT_PAGINATOR_PAGE_RANGE = 3

ST_SEARCH_QUERY_MIN_LEN = 3

ST_USER_LAST_SEEN_THRESHOLD_MINUTES = 1

ST_PRIVATE_FORUM = False

ST_ALLOWED_UPLOAD_IMAGE_FORMAT = ('jpeg', 'png', 'gif')
ST_ALLOWED_URL_PROTOCOLS = {
    'http', 'https', 'mailto', 'ftp', 'ftps',
    'git', 'svn', 'magnet', 'irc', 'ircs'}

ST_UNICODE_SLUGS = True

ST_UNIQUE_EMAILS = True
ST_CASE_INSENSITIVE_EMAILS = True

LOGIN_URL = 'spirit:user:auth:login'
LOGIN_REDIRECT_URL = 'spirit:user:update'
