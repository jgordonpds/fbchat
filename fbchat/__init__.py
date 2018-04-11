# -*- coding: UTF-8 -*-

"""Facebook Chat (Messenger) for Python

Copyright:
    (c) 2015 - 2018 by Taehoon Kim

License:
    BSD, see LICENSE.txt for more details
"""

from __future__ import unicode_literals
import logging

from .models import *

from .base import Base
from .get import Get
from .listener import Listener
from .message_management import MessageManagement
from .search import Search
from .send import Send
from .thread_control import ThreadControl
from .thread_interraction import ThreadInterraction
from .thread_options import ThreadOptions

from .client import Client

__copyright__ = 'Copyright 2015 - 2018 by Taehoon Kim'
__version__ = '2.0.0'
__license__ = 'BSD'
__author__ = 'Taehoon Kim; Moreels Pieter-Jan; Mads Marquart'
__email__ = 'carpedm20@gmail.com; madsmtm@gmail.com'
__source__ = 'https://github.com/carpedm20/fbchat/'
__description__ = 'Facebook Chat (Messenger) for Python'

__all__ = [
    'Message',
    'Mention',

    'Size',
    'Colour',
    'Color',

    'Thread',
    'User',
    'Group',
    'Page',

    'Client'
]


try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
