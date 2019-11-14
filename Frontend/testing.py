import unittest

class TestEventMethods(unittest.TestCase):

    def test_create(self):
        test = createEvent('test', 8.0, 0)
        test2 = createEvent('test2', 8.0, 1)
        test3 = createEVent('test3', 8.0, 0)
        self.assertEqual(test.getName(), 'test')
        self.assertEqual(test.getDuration(), 8.0)
        self.assertEqual(test.getRecurring(), 0)
        self.assertEqual(test.getCreator(),'pjh96@case.edu')
        self.assertEqual(test.getEventID(), eventID)
        test.deleteEventByID(eventID)
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
        self.assertEqual('Zubair Mukhi', test.getAttendeeName("zxm132@case.edu",test))
        self.assertEqual('zxm132@case.edu', test.getAttendeeEmail("Zubair Mukhi",test))
        # self.assertEqual(test.attendeeAvailability(),<times in file from database>)
        # self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/confirmation')
        # self.assertEqual(test.attendeeEdit(),<New times in file from database>)
        return

    #def test_scheduler(self):
     #   self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/results')
      #  return

if __name__ == '__main__':
    unittest.main()
