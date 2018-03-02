
class User:
    count = 1
    #users = [{"id":1,"username": "john","password":"123","role":"normal","comments":[]}]
    def __init__(self, username, password, role, id=None):
        self.user=[]
        self.username = username
        self.password = password
        self.role = role
        self.id = User.count
        User.count+=1



class Admin(User):
    def __init__(self, username, password, role,id=None):
        super(User,self).__init__(self,id,username,password,role="admin")

    
    def create_user(self,username,password):
        new_user =dict(username=username,password=password)
        self.user.append(new_user)
        return "Created user Successfully"

    # def login(self,username, password):
    #    if self.user[username] = username:
    #         return "Login success"
    
class Moderator(User):
    pass


a = User("a","b","c")
print(a)