import unittest
from app import userHandler
from app import eventHandler


class TestEventMethods(unittest.TestCase):

    def test_create(self):
        test = createEvent('test', 15.0, 0)
        test2 = createEvent('test2', 15.0, 1)
        test3 = createEVent('test3', 15.0, 0)
        self.assertEqual(test.getName(), 'test')
        self.assertEqual(test.getDuration(), 15.0)
        self.assertEqual(test.getRecurring(), 0)
        self.assertEqual(test.getCreator(),'pjh96@case.edu')
        self.assertEqual(test.getEventID(), test)
        test.deleteEventByID(test)
        self.assertFalse(test)
        test2.deleteEventByCreator('pjh96@case.edu')
        self.assertFalse(test2)
        self.assertFalse(test3)

        #self.assertEqual(test.getRecurring(test.getEventID(), "whenisbest.com/event/<eventID>/onetime")
        #self.assertEqual(test.isRecurring(test2.getEventID(), "whenisbest.com/event/<eventID>/recurring")

        # functionality absorbed by createEvent - Frontend collates data before handing it to backend for processing
        # self.assertEqual(test.submit(),eventID)

        #self.assertEqual(test.share(), 'whenisbest.com/event/<eventID>/share')
        
        
        return

    test = createEvent('test', 8.0, 0)
    test2 = createEvent('test2', 8.0, 1)
    def test_attendee(self):
        test.attendeeAccept('Zubair Mukhi','zxm132@case.edu', test)
        test.attendeeAccept('Patrick Hogrell','pjh96@case.edu', test)
        self.assertEqual('Zubair Mukhi', test.getAttendeeName("zxm132@case.edu",test))
        self.assertEqual('zxm132@case.edu', test.getAttendeeEmail("Zubair Mukhi",test))
        
        from datetime import datetime, timedelta
        now = datetime.now()
        timeArr = []
        for i in range(0, 5):
            timeArr.append(now + timedelta(seconds=3600))

        attendeeSubmit("zxm132@case.edu", test, "Zubair", timeArr)
        attendeeSubmit("pjh96@case.edu", test, "Patrick", timeArr)
        
        self.assertEqual(test.attendeeAvailability(),{"Zubair", timeArr})
        self.assertEqual(test.attendeeEdit("pjh96@case.edu", test, timeArr[1:4]), {"Patrick", timeArr[1:4]})
        
        self.assertEqual(eventHandler.getAllMatching(test),2)
        responses = eventHandler.getAllResponses(test)
        self.asserEqual(responses, {{"Zubair", timeArr}, {"Patrick", timeArr[1:4]}})
        
        return
    
    def test_user(self):
        user1 = createUser('zxm132@case.edu','Zubair', 'Mukhi', 'password')
        self.assertEqual(createUser('zxm132@case.edu','Zubair', 'Mukhi', 'password'),"user exists")
        self.assertEqual(User1.getUser('zxm132@case.edu'),'zxm132@case.edu')
        User1.editFirstName('Zubar','zxm132@case.edu')
        self.assertEqual(User1.getFirstName('zxm132@case.edu'),'Zubar')
        User1.editLastName('Mukh','zxm132@case.edu')
        self.assertEqual(User1.getLastName('zxm132@case.edu'), 'Mukh')
        User1.editName('Zubair','Mukhi','zxm132@case.edu')
        self.assertEqual(User1.getName('zxm132@case.edu'),'Zubair Mukhi')
        User1.updatePassword('zxm132@case.edu','password','1s3mK0')
        deleteUser('blp27.edu')
        User1.updateEmail('zxm132@case.edu','blp27.edu','1s3mK0')
        self.assertEqual(User1.getUser('blp27@case.edu'),'blp27@case.edu')
        deleteUser('blp27.edu')
        self.assertFalse(User1.getUser('blp27.edu'))
        return


    #def test_scheduler(self):
     #   self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/results')
      #  return

if __name__ == '__main__':
    unittest.main()
