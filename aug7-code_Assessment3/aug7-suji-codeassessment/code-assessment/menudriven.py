import re,logging,csv,json,smtplib
try:
    """ def validations(name,rollno,admno,college,parentname,mobilenumber,emailid):
        val_name=re.search("[A-Z]{1}[a-z]{2,12}",name)
        val_rollno=re.search("[1-9]{2}",rollno)
        val_admno=re.search("[1-9]{1}[0-9]{2,4}",admno)
        val_college=re.search("[A-z]*",college)
        val_parentname=re.search("[A-z]{1}[a-z}*",parentname)
        val_mobileno=re.search("[6-9]{1}[0-9]{9}",mobilenumber)
        val_mailid=re.search("[a-zA-Z0-9]{2-15}@[A-Za-z]{2-10}\.[A-za-z]{2-8}",emailid) """
    
    studentlist=[]

    class Student:
        def student_data(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            dict_student={"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid}
            studentlist.append(dict1_student)

    class Sem1Result(Student):
        def sem_data(self,telugu,hindi,english,maths,science):
            total=telugu+hindi+english+maths+science
            per=(total/200)*100
            dict_sub={"per":per,"telugu":telugu,"hindi":hindi,"english":english,"maths":maths,"science":science}
            studentlist.append(dict_sub)

    obj1=Student()
    obj2=Sem1Result()

    while(True):
        print("1.add student:")
        print("2.generate json file and display the api :")
        print("3.based on ranking:")
        print("4.less than 50%:")
        print("5.exit")
        choice =int(input("enter the choice:"))
        if choice==1:
            name=input("enter the name:")
            rollno=int(input("enter rollno:"))
            admno=int(input("enter admno:"))
            college=input("Enter college name:")
            parentname=input("enter the name of parent:")
            mobilenumber=int(input("enter mobile number:"))
            emailid=input("enter email id:")
            telugu=int(input("enter telugu marks:"))
            hindi=int(input("enter hindi marks:"))
            english=int(input("enter english marks:"))
            maths=int(input("enter maths marks:"))
            science=int(input("enter science marks:"))
        
            """             validate=validations(val_name,val_rollno,val_admno,val_college,val_parentname,val_mobileno,val_mailid)
            if validate:
                print("validations are correct")
            else:
                 logging.error("validations are wrong")  """   
            
            obj2.sem_data(telugu,hindi,english,maths,science)
            

        if choice==2:
            print(json.dumps(studentlist))

        if choice==3:
            print(json.dumps(sorted(studentlist,key=lambda i:i["per"],reverse=True))) 

        if choice==4:
            x=list(filter(lambda i:i["per"]<50,studentlist))
            print(x)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("sujivennapusa2000@gmail.com","suji1806")
            message="marks"
            connection.sendmail("sujivennapusa2000@gmail.com","vennapusasuji463@gmail.com",x)
            print("email sent successfully")
            connection.quit()    

            


except:
    logging.error("something went wrong")        
        