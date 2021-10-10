import mysql.connector


mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()


sqlFormulaSearchEmail = (
    "select * from passwords WHERE passwords.email LIKE %s")


def searchAppsAssociated():
    row = input(" *Enter the email : ")
    mycursor.execute(sqlFormulaSearchEmail % ("'%"+row+"%'"))
    results = mycursor.fetchall()
    for result in results:
        print("***************************")
        print()
        print(result)
        print()
        print("***************************")
