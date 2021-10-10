import mysql.connector
import bcrypt  # to hash the password
import pyperclip  # to copy text(new password) to clipboard


mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()

sqlFormulaSearchpassword = (
    "select password from passwords where passwords.app_name like %s")


def findPassword():
    row = input(" *Enter the app or site name : ")
    mycursor.execute(sqlFormulaSearchpassword % ("'%"+row+"%'"))
    results = mycursor.fetchall()
    pyperclip.copy(results[0][0])
    print(results[0][0], "  (copied to clipboard)")
