from app import passHandler
from app import sql


def emailEvent(address, eventID):
    print("Sending event " + eventID + " to " + address + ".")
    return


def emailRecovery(address):
    key = passHandler.getHash(address)
    query = "insert into passReset(userID, validator) values (%s, %s)"
    values = (address, key)
    sql.createQuery(query, values)
    print("Sending password link to " + address + ". Key is: " + key)
    return
