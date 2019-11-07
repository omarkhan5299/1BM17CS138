import sqlite3
connection = sqlite3.connect("myfile.db")
cursor = connection.cursor()
#cursor.execute("""CREATE TABLE INFO_S
#               ( name varchar,
#                 usn varchar,
#                 dob varchar,
#                 sem varchar);""")"""

def fdisplay():
    
    print("\n\nName\t Usn\tDOB\tSem")
    print("---------------------------")
    tup = cursor.execute("SELECT * FROM INFO_S;")
    for t in tup:
        print(t[0],'\t',t[1],'\t',t[2],'\t',t[3])
    

def finsert():
    name = input("Enter the name:")
    usn = input("Enter the usn:")
    dob = input("Enter the dob:")
    sem = input("Enter the sem:")
    v = [name,usn,dob,sem]
    cursor.execute("INSERT INTO INFO_S VALUES(?,?,?,?)",v)

def fsearch():
    flag = 0
    usn = str(input("Enter the usn of the student to search:"))
    cursor.execute("SELECT USN FROM INFO_S;")
    usn_q = cursor.fetchall()
    for i in usn_q:
        for j in i:
            if j==usn:
                flag =1 
                ind = usn_q.index(i)
                
   
    if flag == 1:
        cursor.execute("SELECT *FROM INFO_S")
        f = cursor.fetchall()
        print("\n\nName\t Usn\tDOB\tSem")
        print("---------------------------")
        print(f[ind][0],'\t',f[ind][1],'\t',f[ind][2],'\t',f[ind][3])
    elif flag == 0:
        print("\nThe USN provided is not present!")

def fupdate():
    flag = 0
    usn = str(input("Enter the usn of the student to search:"))
    cursor.execute("SELECT USN FROM INFO_S;")
    usn_q = cursor.fetchall()
    for i in usn_q:
        for j in i:
            if j==usn:
                flag =1 
                ind = usn_q.index(i)
    
    if flag == 1:
         
         name = input("re-Enter the name:")
         dob = input("re-Enter the dob:")
         sem = input("re-Enter the sem:")
         lst = [name,dob,sem,usn]
         cursor.execute("UPDATE INFO_S SET name=?,dob=?,sem=? where usn=?",lst)
         print("Updated!!")        
    
def fdelete():
    flag = 0
    usn = str(input("Enter the usn of the student to search:"))
    cursor.execute("SELECT USN FROM INFO_S;")
    usn_q = cursor.fetchall()
    for i in usn_q:
        for j in i:
            if j==usn:
                flag =1 
                ind = usn_q.index(i)
    if flag ==1:
        lst = [usn]
        cursor.execute("DELETE FROM INFO_S WHERE usn=?",lst)
        print("Entry deleted!!")
    


l = 'y'
while(l == 'y'):
    print("""****************
1.Display
2.Insert
3.Search(usn)
4.Update(usn)
5.Delete(usn)""")
    ch = int(input("\nEnter your choice:"))

    if ch == 1:
             fdisplay()
    elif ch == 2:
             finsert()
    elif ch == 3:
            fsearch()
    elif ch ==4:
            fupdate()
    elif ch == 5:
            fdelete()
    else:
        print("\nIncorrect choice. Please try again!\n")
    
        
    l = input("\nContinue? (y/n)")
    print("\n\n\n\n")
    


             
    
