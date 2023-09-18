# my_module.py

def say_hello():
    print("Hello from my_module!")

# This code will be executed when the module is imported or run as a script
print("This line always gets executed.")

# Use the __name__ variable to check if the module is being run as a script
if __name__ == "__main__":
    print("This code runs only when my_module is executed as a script.")
