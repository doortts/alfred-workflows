#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import sys
import webbrowser
from urllib import quote
from unicodedata import normalize

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError
    query = normalize('NFC', unicode(sys.argv[1])).encode('utf-8')
    url = u'http://dic.daum.net/search.do?dic=eng&q=%s' % quote(query)
    webbrowser.open(url)
    sys.exit(0)
