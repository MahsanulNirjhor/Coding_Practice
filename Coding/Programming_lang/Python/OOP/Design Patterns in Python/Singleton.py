class Singleton:
    # __instanse is a class variable
    # It will keep track of the instance variable
    __instance = None

    # By using @staticmethod I have made
    # getInstance() method static that means 
    # it is related to the class not to a particular class
    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self) -> None:
        if Singleton.__instance != None:
            raise Exception("Singleton Instance Already Exists!!!! ^-^")
        else:
            Singleton.__instance = self



# Client Code

s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
# To verify if there is an already existing instance
# s3 = Singleton()
# print(s3)

