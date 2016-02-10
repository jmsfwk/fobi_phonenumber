__title__ = 'fobi_phonenumber.apps'
__author__ = 'James Fenwick <jfenwick@tecaz.com'
__copyright__ = 'Copyright (c) 2016 Tecaz Ltd'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'fobi_phonenumber'
        label = 'fobi_phonenumber'

except ImportError:
    pass
