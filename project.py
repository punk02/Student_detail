import math
import mysql.connector as mq

def space():
  for s in range(15):
    print()



def add_student():
    conn = mq.connect(
        host='localhost', database='project', user='root', password='123456')
    cursor = conn.cursor()
    space()

    print("Add student detail")
    roll_num = int(input("Enter student Roll number :"))
    Name = input("Enter student Name :")
    Email = input("Enter student Email :")

    sql ='insert into student values(%s,%s,%s)'
    data = [roll_num,Name,Email]
    cursor.execute(sql,data)
    conn.commit()

    print("New student add successfully....")


def add_marks():
    conn = mq.connect(
        host='localhost', database='project', user='root', password='123456')
    cursor = conn.cursor()
    space()

    print("Add student detail")
    roll_num = int(input("Enter student Roll number :"))
    math = input("Enter mathamestics marks:")
    hindi = int(input("Enter hindi marks :"))
    eng = int(input("Enter english marks :"))
    phy= int(input("Enter physics :"))
    chem= int(input("Enter chemistry marks :"))


    sql ='insert into marks values(%s,%s,%s,%s,%s,%s)'
    data = [roll_num,math,hindi,eng,phy,chem]
    cursor.execute(sql,data)
    conn.commit()

    print("Marks add successfully....")


def st_mf():
    conn = mq.connect(
    host='localhost', database='project', user='root', password='123456')
    cursor = conn.cursor()
    space()
    print('Modify Student Information')
    Roll_number = input("Enter roll number :")
    print('''\tenter 1 for changing name
             enter 2 for changing Email''')
    field = ''
    choice = int(input("enter a choice"))
    if choice==1:
        field='Name'
    if choice==2:
        field='Email'
         

    value= input("enter a value :")
    sql= 'UPDATE student SET '+field+'="'+value+'" where Roll_number='+Roll_number+';'
    cursor.execute(sql)
    conn.commit()

def display_single_report():
    conn = mq.connect(
    host='localhost', database='project', user='root', password='123456')
    cursor = conn.cursor()
    space()
    print(' Student Information...')
    Roll_number = input("Enter roll number :")
    sql ='select s.roll_num,Name,Email,math,hindi,phy,eng,chem from student s,marks m where s.roll_num = m.roll_num and s.roll_num ='+Roll_number+';'
    cursor.execute(sql)
    data = cursor.fetchone()
    print('Roll_number :',data[0],'Name :',data[1],'Email :',data[2])
    print('Subject',' Max marks','min marks','obtained marks')
    print('math','     100    ' , '   33        ', data[3])
    print('hindi','    100    ' , '   33        ', data[4])
    print('physics','  100    ' , '   33        ', data[5])
    print('English','  100    ' , '   33        ', data[6])
    print('chemisrty','100    ' , '   33        ', data[7])
    if int(data[3])>=33 and int(data[4])>=33 and int(data[5])>=33 and int(data[6])>=33 and int(data[7])>=33:
        print("The result of the sutdent is Pass")
    else:
        print("The result of the sutdent is Fail")
   
    conn.close()
    hold = input()

from prettytable import PrettyTable


def display_all():
    conn = mq.connect(
    host='localhost', database='project', user='root', password='123456')
    cursor = conn.cursor()
    print(' Student Information...')

    Roll_number = input("Enter roll number :")
    sql ='select s.roll_num,Name,Email,math,hindi,phy,eng,chem from  \
        student s,marks m where s.roll_num = m.roll_num and s.roll_num ='+Roll_number+' ORDER BY roll_num ASC;'
    cursor.execute(sql)
    data = cursor.fetchall()
    
    t = PrettyTable(['roll_num', 'Name', 'Email', 'math', 'hindi', 'phy','eng','chem','total'])

    for Idr, Name, Email, math, hindi, phy,eng,chem in data:
        total=int(math)+hindi+phy+eng+chem

        t.add_row([Idr, Name, Email, math, hindi, phy,eng,chem,total])
    print(t)
    conn.close()


def main_menu():
    while True:
      space()
      print('  STUDENT INFORMATION ')
      print("\n  1.  Add Student details")
      print('\n  2.  Add student marks')
      print('\n  3.  Modify Student data')
      print('\n  4.  show single student marks')
      print('\n  5.  show all student detail')
      print('\n  6.  exit ')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_student()
      if choice == 2:
        add_marks()
      if choice == 3:
        st_mf()
      if choice == 4:
        display_single_report()
      if choice == 5:
        display_all()
        
      if choice == 6:
        break

if __name__ =="__main__":
    main_menu()