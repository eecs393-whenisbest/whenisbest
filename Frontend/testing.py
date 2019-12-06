import unittest
from app import userHandler
from app import eventHandler
from app import attendeeHandler
import main
from datetime import datetime, timedelta


class TestEventMethods(unittest.TestCase):

    def test_create(self):
        test = main.createEvent('test', 15.0, 0)
        test2 = main.createEvent('test2', 15.0, 1)
        test3 = main.createEvent('test3', 15.0, 0)
        self.assertEqual(main.getName(test), 'test')
        self.assertEqual(main.getDuration(test), 15.0)
        self.assertEqual(main.getRecurring(test), 0)
        self.assertEqual(main.getCreator(test), 'pjh96@case.edu')
        self.assertEqual(main.getEventID('pjh96@case.edu', 'test'), (test))
        eventHandler.deleteEventByID(test)
        self.assertEqual(eventHandler.getName(test), ())
        eventHandler.deleteEventByCreator('pjh96@case.edu')
        self.assertEqual(eventHandler.getName(test2), ())
        self.assertEqual(eventHandler.getName(test3), ())

        # self.assertEqual(test.getRecurring(test.getEventID(), "whenisbest.com/event/<eventID>/onetime")
        # self.assertEqual(test.isRecurring(test2.getEventID(), "whenisbest.com/event/<eventID>/recurring")

        # functionality absorbed by createEvent - Frontend collates data before handing it to backend for processing
        # self.assertEqual(test.submit(),eventID)

        # self.assertEqual(test.share(), 'whenisbest.com/event/<eventID>/share')
        return

    def test_attendee(self):
        test = main.createEvent('attTest', 8.0, 0)
        now = datetime.now().replace(microsecond=0)
        timeArr = ()
        for i in range(0, 5):
            timeArr = timeArr + ((now + timedelta(seconds=3600) * i),)
        attendeeHandler.attendeeSubmit("zxm132@case.edu", test, "Zubair", timeArr)
        attendeeHandler.attendeeSubmit("pjh96@case.edu", test, "Patrick", timeArr)
        zubairList = ()
        patrickList = ()
        for t in timeArr:
            zubairList = zubairList + (('zxm132@case.edu', t),)
            patrickList = patrickList + (('pjh96@case.edu', t),)
        self.assertEqual(attendeeHandler.attendeeAvailability('zxm132@case.edu', test), zubairList)
        self.assertEqual(attendeeHandler.attendeeEdit("pjh96@case.edu", timeArr[1:4], test), patrickList[1:4])
        # self.assertEqual(eventHandler.getAllMatching(test), 2)
        responses = eventHandler.getAllResponses(test)
        # self.assertEqual(responses, {{"Zubair", timeArr}, {"Patrick", timeArr[1:4]}})

        return

    def test_user(self):
        user1 = userHandler.createUser('zxm132@case.edu', 'Zubair', 'Mukhi', 'password')
        self.assertEqual(userHandler.createUser('zxm132@case.edu', 'Zubair', 'Mukhi', 'password'), False)
        self.assertEqual(userHandler.getUser('zxm132@case.edu')[0], ('Zubair', 'Mukhi', 'zxm132@case.edu'))
        userHandler.editFirstName('Zubar', 'zxm132@case.edu')
        self.assertEqual(userHandler.getFirstName('zxm132@case.edu')[0][0], 'Zubar')
        userHandler.editLastName('Mukh', 'zxm132@case.edu')
        self.assertEqual(userHandler.getLastName('zxm132@case.edu')[0][0], 'Mukh')
        userHandler.editName('Zubair', 'Mukhi', 'zxm132@case.edu')
        self.assertEqual(userHandler.getName('zxm132@case.edu'), 'Zubair Mukhi')
        userHandler.updatePassword('zxm132@case.edu', 'password', '1s3mK0')
        userHandler.deleteUser('zxm132@case.edu')
        self.assertFalse(userHandler.getUser('zxm132@case.edu'))
        return

    # def test_scheduler(self):
        # self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/results')
        # return


if __name__ == '__main__':
    unittest.main()
