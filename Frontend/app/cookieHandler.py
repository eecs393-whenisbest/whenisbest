import requests
import cookielib

cookie_file = '/tmp/cookies'
user = cookielib.LWPCookieJar(cookie_file)

def makeCookie
  s = requests.Session()
  s.cookies = user

  s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
  r = s.get("http://httpbin.org/cookies")

  # Save cookies to disk, even session cookies
  cj.save(ignore_discard=True)
  return

def loadCookie
  # Load existing cookies (file might not yet exist)
  try:
    user.load()
  except:
    pass

