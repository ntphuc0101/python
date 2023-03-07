import sys
sys.path.append('../')  # replace with the actual path to user.py

import unittest
import json
from user import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.test_username = "test_user"
        self.test_password = "test_password"
        self.test_dict = {self.test_username: self.test_password}
        self.user = user()

    def test_getDict(self):
        with open("user.json", "w") as file:
            json.dump(self.test_dict, file)
        self.user.getDict()
        self.assertTrue(self.test_dict == self.user.thisdict)

    def test_saveFile(self):
        self.user.thisdict = self.test_dict
        self.user.saveFile()
        with open("user.json", "r") as file:
            data = json.load(file)
            self.assertTrue(data == self.test_dict)

if __name__ == '__main__':
    unittest.main()
