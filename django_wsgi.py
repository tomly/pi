__author__ = 'Tomly'
#!/usr/bin/env python
# coding: utf-8

import os
import sys

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pi.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()