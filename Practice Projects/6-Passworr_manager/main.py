from cryptography.fernet import Fernet

def load_key() :
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
master_pwd = input("What is the Master Password? :")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

mode = input("Would you like to add a new password or view existing ones ? (view,add) or press q to quit").lower()

# def write_key() :
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

# write_key()()
def view():
     with open('password.txt' , 'r'  ) as f:
        for line in f.readlines():
            data = line.strip()
            user , passw = data.split("|")
            print("User :",user, "Password : ", str(fer.decrypt(passw.encode())))


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt' , 'a'  ) as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")
while True:

    if mode == "q":
        break

    if mode == "view":
        view()
        break
    elif mode == "add":
        add()
        break
    else:
        print("Ivalid mode")
        break