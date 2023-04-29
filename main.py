from db_helper import Db_helper

def operations():
    db = Db_helper()
    while True:
        print("***** WELCOME *****")
        print()
        print("Press I to Insert user: ")
        print("Press F to Fetch user: ")
        print("Press D to Delete user: ")
        print("Press U to Update user:  ")
        print("Press Q to Exit ")
        print()
        try:
            choice = input().lower()
            if(choice == 'i'):
                #insert user
                uid = int(input("Enter User Id: "))
                uname = input("Enter User Name: ")
                Uphone = input("Enter Mobile Number: ")
                db.insert_user(uid,uname,Uphone)

            elif(choice == 'f'):
                #fetch user
                db.fetch_all()

            elif(choice == 'd'):
                #delete user
                uid=int(input("Enter User Id to delete: "))
                db.delete_user(uid)
            
            elif(choice == 'u'):
                #update user
                uid = int(input("Enter User Id to Update: "))
                uname = input("Enter User new Name: ")
                Uphone = input("Enter Mobile new Number: ")
                db.update_user(uid,uname,Uphone)

            elif(choice == 'q'):
                break
            else:
                print("Invalid Input! Try again")
        except Exception as e:
            print(e)
            print("Wrong Choice!")


if __name__ == '__main__':
    operations()
