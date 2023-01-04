import csv
import os
import datetime


def FirstDate(CsvFileName):
    date = '01-01-2023'
    endDate = datetime.datetime.now().strftime("%d-%m-%Y")
    with open(CsvFileName, 'w', newline='') as f:
        fieldnames = ['Date', 'Important', 'ImportantComplete', 'Primary',
                      'PrimaryComplete', 'Secondary', 'SecondaryComplete', 'Score']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()
        while (date != endDate):
            thewriter.writerow({'Date': date, 'Important': 0, 'ImportantComplete': 0, 'Primary': 0,
                               'PrimaryComplete': 0, 'Secondary': 0, 'SecondaryComplete': 0, 'Score': 0})
            date = datetime.datetime.strptime(date, '%d-%m-%Y')
            date = date + datetime.timedelta(days=1)
            date = date.strftime("%d-%m-%Y")
        f.close()
    with open('Important.txt', 'w', newline='') as f:
        f.close()
    with open('ImportantComplete.txt', 'w', newline='') as f:
        f.close()
    with open('Primary.txt', 'w', newline='') as f:
        f.close()
    with open('PrimaryComplete.txt', 'w', newline='') as f:
        f.close()
    with open('Secondary.txt', 'w', newline='') as f:
        f.close()
    with open('SecondaryComplete.txt', 'w', newline='') as f:
        f.close()


def Re_createFile():
    os.remove('Important.txt')
    os.remove('ImportantComplete.txt')
    os.remove('Primary.txt')
    os.remove('PrimaryComplete.txt')
    os.remove('Secondary.txt')
    os.remove('SecondaryComplete.txt')
    with open('Important.txt', 'w', newline='') as f:
        f.close()
    with open('ImportantComplete.txt', 'w', newline='') as f:
        f.close()
    with open('Primary.txt', 'w', newline='') as f:
        f.close()
    with open('PrimaryComplete.txt', 'w', newline='') as f:
        f.close()
    with open('Secondary.txt', 'w', newline='') as f:
        f.close()
    with open('SecondaryComplete.txt', 'w', newline='') as f:
        f.close()


def IsDate(CsvFileName):
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    csvFile = csv.reader(open(CsvFileName, 'r'))
    for row in csvFile:
        if today == row[0]:
            return True 
        else:
            return False

def AddTask():
    flag1 = 1
    while flag1 == 1:
        print("Whick type of task you want to assign:\n1. Importnt\n2. Primary\n3.Secondry\nor press 4.to exit add task windo:  ")
        type = int(input())
        if type==1:
            flag = 1
            while flag == 1:
                print("Important task")
                task = input("Enter the task:  ")
                with open('Important.txt', 'a', newline='') as f:
                    f.write(task + "\n")
                    f.close()
                choice = int(input("want to add another Important task:\n1. yes\n2. no\n:  "))
                if choice == 2:
                    flag = 0
        if type==2:
            flag = 1
            while flag == 1:
                print("Primary task")
                task = input("Enter the task:  ")
                with open('Primary.txt', 'a', newline='') as f:
                    f.write(task + "\n")
                    f.close()
                choice = int(input("want to add another Primary task:\n1. yes\n2. no\n:  "))
                if choice == 2:
                    flag = 0
        if type==3:
            flag = 1
            while flag == 1:
                print("Secondary task")
                task = input("Enter the task:  ")
                with open('Secondary.txt', 'a', newline='') as f:
                    f.write(task + "\n")
                    f.close()
                choice = int(input("want to add another Secondary task:\n1. yes\n2. no\n:  "))
                if choice == 2:
                    flag = 0
        if type==4:
            flag1 = 0


def RemoveTask():
    pass


def CheckTask():
    pass


def ViewPerformance():
    pass


def HomePage():
    while True:
        print("1.Add Task\n2.Remove Task\n3. Check Task\n4. View Performance\n:  ")
        choice = int(input())
        if choice==1:
            AddTask()
        if choice==2:
            RemoveTask()
        if choice==3:
            CheckTask()
        if choice==4:
            ViewPerformance()


def StartWorking():
    year = datetime.datetime.now().strftime('%Y')
    CsvFileName = year + '.csv'

    if (not os.path.isfile(CsvFileName)):
        FirstDate(CsvFileName)
    else:
        if (not IsDate(CsvFileName)):
            Re_createFile()
            AddTask()
        else:
            HomePage()


StartWorking()
