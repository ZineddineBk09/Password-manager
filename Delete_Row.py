import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()


def deleteRow():
    response = input("Are you shure? (Y/N) : ")
    if(response.lower() == 'y'):
        pw = getpass("Enter password for PW manager app : ")
        if(pw == "pw@1209"):
            row = input("Enter app name : ")
            sqlFormulaDeleteRow = "delete from passwords where app_name like %s"
            mycursor.execute(sqlFormulaDeleteRow % ("'%"+row+"%'"))
        else:
            print("\nX wrong password X\n")

    else:
        return
