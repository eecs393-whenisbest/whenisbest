from app import passHandler
from app import sql
#  from app import mailjet


def emailEvent(address, eventID):
    #  mailjet.mail(address, eventID)
    return


def emailRecovery(address):
    key = passHandler.getHash(address)
    query = "insert into passReset(userID, validator) values (%s, %s)"
    values = (address, key)
    sql.createQuery(query, values)
    #  mailjet.mailReset(address, key)
    return


def eventConfirm(address, timeSlot):
    #  mailjet.eventMail(address, timeSlot)
    return
