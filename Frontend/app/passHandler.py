# Following steps outlined in
# https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
# https://www.vitoshacademy.com/hashing-passwords-in-python/

import hashlib
import os
import binascii
from app import sql


def getHash(rawPass):
    salt = os.urandom(32)
    hashPass = genHash(rawPass, salt)
    store = binascii.hexlify(salt) + binascii.hexlify(hashPass)
    return store


def confirmPass(email, guess):
    query = "select Pass from Users where userID = %s"
    values = (email,)
    target = sql.getQueryResults(query, values)[0][0]
    salt = binascii.unhexlify(target[:64])
    currentHash = genHash(guess, salt)
    currentTry = binascii.hexlify(salt).decode() + binascii.hexlify(currentHash).decode()
    return currentTry == target


def genHash(input, salt):
    hashPass = hashlib.pbkdf2_hmac('sha512', input.encode('utf-8'), salt, 100000, dklen=32)
    return hashPass
