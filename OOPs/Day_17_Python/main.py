class User:
    #pass # Just tells compiler to continue to next line of code
    def __init__(self, user_name, user_id): # This is a constructor. 
        # The 'self' parameter lets the method know the object it got called from.
        # This function is called every time an object is created out of this class
        """Constructor, which can be used to initilize user information"""
        self.name = user_name
        self.id   = user_id
        self.follower = 0
        self.following = 0


    def print_data(self): # This self is a local veriable in this calss and
        # can only be accessed in this class only
        """Prints the data initilized in this class"""
        print(f"User ID : {self.id}")
        print(f"User Name : {self.name}")
        print(f"User Follower : {self.follower}")
        print(f"User Following : {self.following}")

    def follow(self, user): # Here we are taking object as a parameter and updating it's value
        user.follower += 1
        self.following += 1


# PascalCase : All beginning letter of the words to be capital letter
# All class names shall be following this "PascalCase" WoC (Way of Code)
# Camel case is first letter of first word to be 
#              lower case and reset of the first letter of all words to be capital.
# Snake case is all to be in smaller case and each words are seperated by underscore '_'

# Generally snake case and PascalCase are used in programming


# Constructor : It specify what should happen when an object is constructed out of calss. 
#              Also known as initilizing 

# This constructing or initilizing is done by special function "def __init__()"

# Here 2 object of same class is created and data for each user is stored seperately. 
# It can be accesses individually useing respective class.
user_1 = User("vivek", "A471479") # () is used to intilize the class.
user_2 = User("Deepak", "A470777")
user_1.print_data()
user_2.print_data()
user_1.follow(user_2)
user_2.follow(user_1)
user_1.print_data()
user_2.print_data()

