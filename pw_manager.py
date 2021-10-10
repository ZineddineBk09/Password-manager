import mysql.connector
from decouple import config  # for os variables
import bcrypt  # to hash the password
import pyperclip  # to copy text(new password) to clipboard
from getpass import getpass
from Create_New_Password import newPassword
from Show_All import showAll
from Search_Apps_Associated_To_Email import searchAppsAssociated
from Find_Password import findPassword
from Delete_All import deleteAll
from Delete_Row import deleteRow


mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="mysql@1209", database="PWM"
)

mycursor = mydb.cursor()


APP_PASSWORD = config("PM_password")
USERINPUT = ""
CHECK_PASS = ""

while(CHECK_PASS != APP_PASSWORD):
    CHECK_PASS = getpass("Enter password for PW manager app : ")
    print()

while(USERINPUT.lower() != "q"):
    print("_________________________________________________\n_____________________MENU________________________:")
    print("1.Create a new password \n2.Find all apps connected to an email \n3.Find a password for a site or an app\n4.Delete an App\n5.Show All \n6.Delete All \nQ.Quit")
    print("_________________________________________________")
    USERINPUT = input(">")
    if(USERINPUT == "1"):
        newPassword()

    elif(USERINPUT == "2"):
        searchAppsAssociated()

    elif(USERINPUT == "3"):
        findPassword()
    elif(USERINPUT == "4"):
        deleteRow()
    elif(USERINPUT == "5"):
        showAll()
    elif(USERINPUT == "6"):
        deleteAll()
    elif(USERINPUT.lower() != "q"):
        print("Wrong Input !! (try again)")
