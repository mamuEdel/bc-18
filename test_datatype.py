import unittest

def test_data_type(self):
	self.assertEqual(data_type(1), "less than 100")
	self.assertEqual(data_type(100), "equal to 100")
	self.assertEqual(data_type(101), "more than 100")
	self.assertEqual(data_type('MaryDoe'), 6)
	self.assertEqual(data_type(True), True)
	self.assertEqual(data_type(False), False)
	self.assertEqual(data_type([1,2,3,4]), 3)