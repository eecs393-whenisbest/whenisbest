import requests
import http.cookiejar as cookielib
from app import routes
from datetime import datetime

cookie_file = '/tmp/cookies'
user = cookielib.LWPCookieJar(cookie_file)


def makeCookie(userID):
    s = requests.Session()
    s.cookies = user
    s.get('/login/cookies/set/sessioncookie/{}'.format(userID))
    r = s.get('/login/cookies')
    s.cookies.expires(datetime.now + 3600)
    # Save cookies to disk, even session cookies
    user.save(ignore_discard=True)
    return


def loadCookie():
    # Load existing cookies (file might not yet exist)
    try:
        user.load()
    except exception as e:
        return print('Please log in'), routes.loginPage()
