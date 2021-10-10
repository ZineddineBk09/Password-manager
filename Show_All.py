import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()

sqlFormulaShowALL = "select * from passwords "


def showAll():
    mycursor.execute(sqlFormulaShowALL)
    results = mycursor.fetchall()
    for result in results:
        print("***************************")
        print()
        for field in result:
            print(field)
        print()
        print("***************************")

