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
        
