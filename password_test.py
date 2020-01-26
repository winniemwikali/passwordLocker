import unittest
from password import Users,Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class for creating and authenticating credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_user = Credentials("winnie","mwikali", "abdc")
    
    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        Credentials.users_list = []
    
    def test__init__(self):
        '''
        Test case to test if the case has been initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"mwikali")
        self.assertEqual(self.new_user.password,"abdc")
    
    def test_create(self):
        '''
        Testing if the new credential is saved into the list
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list),1)
    
    def test_authenticate(self):
        '''
        Testing to check if the authenticate function can sign in a user properly
        '''
        self.new_user.create_account()
        test_account = Credentials("winnie","abcd","Password")
        test_account.create_account()




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
        self.assertEqual(len(Users.users_list),0)

class TestCredentials(unittest.TestCase):

 if __name__ == '__main__':
    unittest.main()
