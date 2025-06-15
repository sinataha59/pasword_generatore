password_item ={"number":True,"charecter":True,"lower_case":True,"upper_case":True , "lenth":8 }
user_opttion=[]

import random
import string

def intro():
    #this function intrduce the app to user
    print("---"*10)
    print("this program for generate password!!\nyou can make your unik password.")

def user_length():
    #this function input length_pass , it must be a number and bigger than 8.
        while True:
            print("--"*5)
            try:
                length =int(input("how long would you want be your password?"))
                if int(length) < 8:
                    print(" your len must be longer than 8")    
                else:
                    
                    password_item["lenth"] = int(length)
                    
                    break
            except ValueError:
                print("your pass must be a number!!!!!")      
    
def unic_maker():
    #this function make a list from user order(number , lower , upper , charecrtor , lenth)
    for i in password_item:
        print("---"*3)
        if i != "lenth" :
            user_custom = input(f"do you want {i} in your password ? y-> yes  n-> no :")
            while True:
                if user_custom in ["y","n"]:
                    if user_custom == "y":
                        user_opttion.append(i)
                        break
                    elif user_custom == "n":
                        break
                else:
                    print("pleas choose y or n .")
                    user_custom = input(f"do you want {i} in your password ? y-> yes  n-> no :")
        else:
            user_length()
    print(f"your password incluod {user_opttion} and it take {password_item['lenth']} long .")

def chinesh():
    pass_situation = []
    for i in range(password_item["lenth"]):
        pass_situation+= random.choices(user_opttion)
    
    return(pass_situation)

def generate(item):
    final_password=""
    
    if item == "number":
        final_password += random.choice(string.digits)
    elif item =="upper_case"  :
        final_password +=random.choice(string.ascii_uppercase)  
    elif item =="lower_case"  :
        final_password += random.choice(string.ascii_lowercase)  
    elif item =="charecter"  :
        final_password += random.choice("!@#$%^&*()_+")  
    return final_password
with open("password.txt", "a") as f:
    

    def run ():
        intro()
        unic_maker()
        result = (list(map(generate,chinesh())))
        user_password = "".join(map(str,result))
        print("--"*5)
        print(f"this is your unic password :   {user_password}")
        while True:
            user_sugestion = input(f"is {user_password} ok ? :  ")
            if user_sugestion  in ["y","n"] :
                if user_sugestion == "y":
                    print("-----"*5)
                    f.write(f"your password :  {user_password}\n")
                    print("good luck")
                    break
                else:
                    print("we try again")
                    result = (list(map(generate,chinesh())))
                    user_password = "".join(map(str,result))
                    print("--"*5)
                    print(f"this is your unic password :   {user_password}")
            else:
                print("--"*3) 
                print("pleas answer with y , n .")
    run()

