# coding:utf-8

import os

ROOT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(ROOT_DIR, 'static')
MEDIA_ROOT=os.path.join(os.path.dirname(__file__),'static').replace('\\','/')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/'
# fix for django 1.4
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ynv1e*b9gn$pd7777777j298=+s9aaaaaaaxcr%33b5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.media',
	'djblog.context_processors.globals_vars',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'djblog.urls'



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'djblog.blog',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


from os import environ
import os

# 时区
TIME_ZONE = 'Asia/Shanghai'

# 语言
LANGUAGE_CODE = 'zh-cn'

# 邮箱（报错时发送）
EMAIL = 'scudongchao@gmail.com'

# 是否本地环境
LOCAL_DEBUG = not environ.get("SERVER_SOFTWARE", "")
if not LOCAL_DEBUG:
	import sae.const
	# 数据库信息
	DATABASES = {
    		'default': {
        	'ENGINE': 'django.db.backends.mysql', # mysql 可以改成 'postgresql_psycopg2', 'postgresql', 'sqlite3' or 'oracle'.
        	'NAME': sae.const.MYSQL_DB,                      # 数据库名
        	'USER': sae.const.MYSQL_USER,                      # sqlite3 不使用此配置
        	'PASSWORD': sae.const.MYSQL_PASS,                  # sqlite3 不使用此配置
        	'HOST': sae.const.MYSQL_HOST,
        	'PORT': sae.const.MYSQL_PORT,
    		}
	}
else :
	# 数据库信息
	DATABASES = {
    		'default': {
        	'ENGINE': 'django.db.backends.sqlite3', # mysql 可以改成 'postgresql_psycopg2', 'postgresql', 'sqlite3' or 'oracle'.
        	'NAME': 'djblog',                      # 数据库名
        	'USER': '',                      # sqlite3 不使用此配置
        	'PASSWORD': '',                  # sqlite3 不使用此配置
        	'HOST': '',
        	'PORT': '',
    		}
	}
# 主题
THEME = 'classic'

#### 以下配置不要改动 ####
TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), 'templates/' + THEME),
)
# 站点名称
SITE_TITLE = '达摩流浪者'
# 副标题
SITE_SUBTITLE = u'我是一名程序员而且我坚信我十年后还是一名程序员。'
# 作者
SITE_AUTHOR = 'hobo'
# 描述
SITE_DESC = 'hobo\'s personal site'

# 分页大小
PER_PAGE = 5
# recent 个数
RECENT_COUNT = 5

# google 统计的 id
GA_ID = 'UA-15372596-1'

# google custom search id, see http://www.google.com/cse/
CSE_ID = '017823656936221718810:8oexw_fkbz0'

# disqus 评论 id
DISQUS_SHORTNAME = 'scudc'



ADMINS = (
    ('admin', EMAIL),
)
MANAGERS = ADMINS

DATETIME_FORMAT = 'Y/m/d H:i:s'

# overwrite configs
#try:
#	from local_settings import *
#except:
#	pass
