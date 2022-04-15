class User:
    def __init__(self, user_id, username):
        """
        Initializing function
        Called everytime this class is called
        """
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



## Object from the class
user_1 = User("001","Guilherme")
#Add attribute
# user_1.id = "001"
# user_1.username = "Guilherme"
# print(user_1.username)
# print(user_1.followers)

user_2 = User("002","Helena")
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Helena"

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


