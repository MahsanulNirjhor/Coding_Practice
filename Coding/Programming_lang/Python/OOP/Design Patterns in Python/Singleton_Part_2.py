# Most people are comfortable with
# Singleton() rather than Singleton.getInstance()

class Singleton:
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(Singleton,cls).__new__(cls)
        
        return cls.__instance


# Client Code
s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
