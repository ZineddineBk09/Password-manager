import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()

sqlFormulaDeleteALL = "delete from passwords "


def deleteAll():
    print("Are you shure? (Y/N) ")
    response = input()
    if(response.lower() == 'y'):
        pw = getpass("Enter password for PW manager app : ")
        if(pw == "pw@1209"):
            mycursor.execute(sqlFormulaDeleteALL)
        else:
            print("\nX wrong password X\n")

    else:
        return
