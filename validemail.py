import re
email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
user_input=input("ENTER YOUR EMAIL: ")
if re.search(email_condition, user_input):
    print("valid email")
else:
    print("invalid email")

