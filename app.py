def registeration():
 while True:
    fname=input("please enter your first name : ")
    lname=input  ("please enter your last name : ")
    fullname=fname+lname
    if fullname.isspace():
        print(" spaces are not allowed ")
        continue
    elif fullname.isalpha():
        user_email=input("enter your email: ")
        if (user_email.__contains__('@') and user_email.__contains__('.com')):
            password=input("please enter your password :")
            password_conf=input("please confirm your password : ")
            if (password_conf==password):
                mobile=input("please enter your mobile number : ")
                if mobile.isdigit():
                    print ("Your info is successfully registered ")
                    user_info=(f"{fullname}:{user_email}:{password}:{mobile}\n")
                    try:
                        fileobj=open("info.txt","a")
                    except Exception as e:
                        print(e)
                    else:
                        fileobj.write(user_info)
                        fileobj.close()
                        break
                    

                else:
                    print("please enter numbers only")
                    continue
                    
            else:
                print("not matching passwords")
                continue

        else:
            print("invalid email")
            continue


def login():
    try:
        fileobj=open("info.txt","r")
    except Exception as e :
        print(e)
    else:
        user_name=input("please enter your fullname: ")
        password=input("please enter your password : ")
        for i in fileobj:
            user_info=i.strip("\n")
            user_info=i.split(":")
            if (user_info[0]==user_name and user_info[2]==password):
                print("logged in successfully")
                break
        else:
            print("login failed")
            login()
            
        
        
while True:       
 x=input("please enter \n 1)register \n 2)login \n ")
 if x=="1":
    registeration()
    continue
 elif x=="2":
    login()
    break
 else:
    print ("invalid input") 
    continue     




