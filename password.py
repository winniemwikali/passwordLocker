class Credentials:
    '''
    Class that creates accounts and authenticates the users
    '''
    users_list=[]

    def __init__(self, identify, user_name, password):
        '''
        Initalizing the variables
        '''
        self.user_name = user_name
        self.password = password

    def create_account(self):
        '''
        creating and saving log in credentials for users
        '''
        Credentials.users_list.append(self)
    
    @classmethod
    def authenticate_account(cls, name, key):
        '''
        Method that checks if the username and password are correct
        '''
        for user in cls.users_list:
            if user.user_name == name and user.password == key:
                return user
        return 0

class Users:
    '''
    class that generates new instances of users
    '''

    

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password
        
    users_list = []

    def creat_account(self):
        '''
        creat_account method creats account for new users
        '''
        Users.users_list.append(self)

    def save_password(self):
        '''
        save password 
        '''
        Users.users_list.append(self)
    
    def delete_password(self):
        '''
        delete_password deletes a saved password from users_list
        '''
        # Users.users_list.remove(self)
    def add_password(self):
        '''
        add password
        '''
        Users.users_list.append(self)
    def _init_(self,user_name,password):
        '''
        initializing the variables
        '''
        self.user_name = user_name
        self.password = password    
    def view_password(self):
        '''
        view password
        '''
        Users.users_list.append(self)

    @classmethod
    def view_password(cls):
     '''
     creating a method that displays users passwords
     '''
     for password in cls.users_list:
        if password.user_name == name:
            if password.password == name:
                return password
       