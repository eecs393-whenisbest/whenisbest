import requests
import cookielib
from app import routes

cookie_file = '/tmp/cookies'
user = cookielib.LWPCookieJar(cookie_file)

def makeCookie(userID):
  s = requests.Session()
  s.cookies = user

  s.get('Login_Page.html/cookies/set/sessioncookie/%s' )
  r = s.get('Login_Page.html/cookies')
  

  # Save cookies to disk, even session cookies
  user.save(ignore_discard=True)
  return

def loadCookie():
  # Load existing cookies (file might not yet exist)
  try:
    user.load()
  except:
    return loginPage()

