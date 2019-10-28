import unittest

class TestEventMethods(unittest.TestCase):
    test = Event.Create('test', 8.0, 0)
    test2 = Event.Create('test2', 8.0, 1)
    def test_create(self):
        
        self.assertEqual(test.getName(), 'test')
        self.assertEqual(test.getDuration(), 8.0)
        self.assertEqual(test.getRecurring(), 0)
        self.assertEqual(test.getCreator(),'pjh96')
        self.assertEqual(test.getEventID(test.getName(),test.getCreator,test.getDuration(),test.getRecurring()), <eventID>)
        
        self.assertEqual(test.isRecurring(test.getEventID(test.getName(),test.getCreator,test.getDuration(),test.getRecurring(),test.getRecurring()), "whenisbest.com/event/<eventID>/onetime")
        self.assertEqual(test.isRecurring(test2.getEventID(test2.getName(),test2.getCreator,test2.getDuration(),test2.getRecurring()),test2.getRecurring()), "whenisbest.com/event/<eventID>/recurring")
        
        self.assertEqual(test.submit(),<eventID>)
        
        self.assertEqual(test.share(), 'whenisbest.com/event/<eventID>/share')
        return
                         
    def test_attendee(self):                
                         
        self.assertEqual(test.attendeeAccept('Zubair Mukhi','zxm132@case.edu'),(test.getAttendeeName(),test.getAttendeeEmail()))
        self.assertEqual('Zubair Mukhi', test.getAttendeeName())
        self.assertEqual('zxm132@case.edu', test.getAttendeeEmail())
        self.assertEqual(test.attendeeAvalibility(),<times in file from database>)
        self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/confirmation')
        self.assertEqual(test.attendeeEdit(),<New times in file from database>)
        return                

    def test_scheduler(self):
        self.assertEqual(test.attendeeSubmit(),'whenisbest.com/event/<eventID>/results')
        return
                         
if __name__ == '__main__':
    unittest.main()
