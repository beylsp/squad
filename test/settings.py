from squad.settings import *  # noqa

LOGGING['loggers']['django']['level'] = 999  # noqa
LOGGING['loggers']['']['level'] = 999  # noqa

# see  https://github.com/evansd/whitenoise/issues/94
MIDDLEWARE_CLASSES.remove('whitenoise.middleware.WhiteNoiseMiddleware')  # noqa
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'