import mysql.connector
import bcrypt  # to hash the password
import pyperclip  # to copy text(new password) to clipboard


mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()

sqlFormulaInsert = "insert into passwords (app_name,url,email,password,username) values (%s,%s,%s,%s,%s);"

def newPassword():
    app_name = input(" *Enter The App Name : ")
    print()
    url = input(" *Enter The App URL : ")
    print()
    email = input(" *Enter The Email Address : ")
    print()
    #turn our new password to bytes to hash it than copying it to clipboard
    password = input(" *Enter The App Password : ")
    password = bytes(password, encoding='utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    pyperclip.copy(password.decode("utf-8"))

    print()
    username = input(" *Enter The App Username : ")
    print()
    row = (app_name, url, email, password, username)
    mycursor.execute(sqlFormulaInsert, row)
    mydb.commit()
    print("New Password is copied to Clipboard")
