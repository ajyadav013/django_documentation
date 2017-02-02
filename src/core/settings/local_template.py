"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = "DXfPe2YM?Xn2We45dw(CvOssqh4gCb:nK*}abC)((?6z8/>K{{%z_]I)^*J#"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djdoc',
        'USER': 'djdoc',
        'PASSWORD': 'djdoc',
    }
}

ALLOWED_HOSTS = ["*"]
