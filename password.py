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
    def view_password(self):
        '''
        view password
        '''
        Users.users_list.append(self)

