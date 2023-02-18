import json
import re
import os


class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email



class UserRepo:
    def __init__(self):
        self.users = []
        self.isloggedin = False
        self.currentuser = {}

        # load users from .json file
        self.loadUsers() 
    
    def loadUsers(self):
        if os.path.exists("loginsystem.json"):
            with open("loginsystem.json","r",encoding = "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"],password = user["password"],email=user["email"])
                    self.users.append(newUser)
            

    def register(self,user:User):
        self.users.append(user)
        self.savetofile()
        print("User have been created.")
    
    def login(self,username,password):
        if self.isloggedin:
            print("you have already logged in")
        else:
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isloggedin = True
                    self.currentuser = user
                    print("logged in.")
                    break
                else:
                    print("not logged in. try again.")
                    break
    
    def logout(self):
        self.isloggedin = False
        self.currenuser = {}
        print("logged out")
    
    def identity(self):
        if self.isloggedin:
            print(f"username: {self.currentuser.username}")
        else:
            print("not logged in")
    
    def savetofile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) 
        
        with open("loginsystem.json","w") as file:
            json.dump(list,file)
    

def createpassword(str):
    while True:
       str = input("password: ")
       if (len(re.findall("[a-z]",str)) >= 1) and (len(re.findall("[A-Z]",str)) >= 1) and (len(re.findall("[0-9]",str)) >= 1) and len(str) >= 8 and (len(re.findall(" ",str)) == 0) and (len(re.findall("[+@,*.$,]",str)) >= 1) and str != "12345678":
        return str
        
       else:
        print("Password wasn't created")
        if len(str) < 8:
            print("Password must be at least 8 character.")
        if len(re.findall("[a-z]",str)) == 0 or len(re.findall("[A-Z]",str)) == 0:
            print("In password, there must be at least 1 lowercase and 1 uppercase letter.")
        if len(re.findall("[0-9]",str)) == 0:
            print("In password, there must be at least 1 number.")
        if len(re.findall(" ",str)) > 0:
            print("In password, there must not be space character.")
        if len(re.findall("[+@,*.$,]",str)) == 0:
            print("(+@,*.$,) It is needed to add at least one special character in the parantheses.")
        if str == "12345678":
            print("Password must not be easily predictable.")


repository = UserRepo()

while True:
    print("Menu".center(50,"*"))
    choose = input("1-Sign up\n2-Log in\n3-Log out\n4-Display\n5-Exit\nChoose:")

    if choose == "1":
        username = input("username: ")
        password = "" 
        password = createpassword(password)
        email = input("email: ")
    
  
        user = User(username = username,password = password,email=email)
        repository.register(user)

    elif choose == "2":
        if repository.isloggedin:
            print("you have already logged in")
        else:
            username = input("username: ")
            password = input("password: ")
            repository.login(username,password)
    elif choose == "3":
        repository.logout()
    elif choose == "4":
        repository.identity()
    elif choose == "5":
        break
    else:
        print("Wrong chice.Try again please")