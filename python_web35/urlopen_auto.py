__author__ = 'wenhai.dai'

#-*- encode:utf-8  -*-
import urllib.request, urllib.parse, urllib.error

LOGIN = 'daidai'
PASSWD = 'daidai'
URL = 'http://123.207.124.135:8080/personweb/personweb/loginin.jsp'
REALM = 'Secure Archive'

def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    b64str = encodestring(bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]
    req.add_header("Authorization", "Base %s" % b64str)
    return req
for funcType in ('handler', 'request'):
    print('***Using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    f = urllib.request.urlopen(url)
    print(str(f.read(), 'utf-8'))
    f.close()
