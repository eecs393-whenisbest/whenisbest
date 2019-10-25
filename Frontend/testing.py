import unittest

class TestEventMethods(unittest.TestCase):
    def test_create(self):
        test = Event.Create('test', 8.0, 0)
        test2 = Event.Create('test2', 8.0, 1)
        self.assertEqual(test.getName(), 'test')
        self.assertEqual(test.getDuration(), 8.0)
        self.assertEqual(test.getRecurring(), 0)
        self.assertEqual(test.getCreator(),'pjh96')
        self.assertEqual(test.getEventID(test.getName(),test.getCreator,test.getDuration(),test.getRecurring()), <eventID>)
        
        self.assertEqual(test.isRecurring(test.getEventID(test.getName(),test.getCreator,test.getDuration(),test.getRecurring(),test.getRecurring()), "whenisbest.com/event/<eventID>/onetime")
        self.assertEqual(test.isRecurring(test2.getEventID(test2.getName(),test2.getCreator,test2.getDuration(),test2.getRecurring()),test2.getRecurring()), "whenisbest.com/event/<eventID>/recurring")
        
        self.assertEqual(test.submit(),<eventID>)
        
        self.assertEqual(test.share(), "whenisbest.com/event/<eventID>/share")
                         
    def test_attendee(self):
                         
                         
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
