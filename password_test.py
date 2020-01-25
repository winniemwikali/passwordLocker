import unittest
from password import Users,Credentials

class TestUsers(unittest.TestCase):
    '''
    Test class that test cases authentication for the users.

    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run each test cases.
        '''
        self.new_user = Users("winnie","mwikali")# create users object


    def test_init(self):
        '''
        test_int test case to test initialization
        '''
        self.assertEqual(self.new_user.user_name,"winnie")
        self.assertEqual(self.new_user.password,"mwikali")

    def test_creat(self):
        '''
        test_creat_account test case if the account is created
        '''
        
        self.new_user.creat_account()
        self.assertEqual(len(Users.users_list),1)
    
    def tearDown(self):
        '''
        tearDown to clean up each case
        '''
        Users.users_list = []

    def test_save(self):
        '''
        test_save_multiple_password to check if we can save passwords
        '''
        self.new_user.save_password()
        
        self.assertEqual(len(Users.users_list),1)

    def test_delete_password(self):
        '''
        test_delete_password to test if we can delete passwords
        '''
        
        self.new_user.delete_password()
        self.assertEqual(len(Users.users_list),0)
    def test_add_password(self):
        '''
        test_add_password to add new password for new accounts
        '''
        self.new_user.add_password()
        self.assertEqual(len(Users.users_list),1)
    def test_view_password(self):
        '''
        test_view_password to view various passwords
        '''
        self.new_user.view_password()
        self.assertEqual(len(Users.users_list),1)

class TestCredentials(unittest.TestCase):

 if __name__ == '__main__':
    unittest.main()
