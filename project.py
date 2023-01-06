import app
import datetime
import re 
def createproject():
 while True:
    title=input("please enter the title of your project :")
    if  title.isalpha():
        details=input("please enter some details : ")
        totaltarget=input("Please set a total target: ")
        if totaltarget.isnumeric():
            startdate=input("please enter the start date in the form of dd/mm/yy :")
            r1 = re.compile('.*/.*/.*')
            if r1.match(startdate) is not None:
                day1,month1,year1=startdate.split('/')
                validstartdate=True
                try:
                  datetime.datetime(int(year1),int(month1),int(day1))
                except ValueError :
                 validstartdate=False
                if(validstartdate):
                    enddate=input("please enter the end date in the form of dd/mm/yy :")
                    r2 = re.compile('.*/.*/.*')
                    if r2.match(enddate) is not None:
                      day2,month2,year2=enddate.split('/')
                      validenddate=True
                      try:
                        datetime.datetime(int(year2),int(month2),int(day2))
                      except ValueError :
                           validenddate=False
                      if(validenddate):
                        
                        def id():
                          with open(r"project.txt", 'r') as id:
                           x = len(id.readlines())
                           global project_id
                           project_id=x+1
                           return project_id
                        print("Your project is created successfully")
                        print (f"your project id is {id()}")
                        projectdetails=(f"{id()}:{title}:{details}:{totaltarget}:{startdate}:{enddate}\n")
                        try:
                         fileproject=open("project.txt","a")
                        except Exception as e:
                          print(e)
                        else:
                          fileproject.write(projectdetails)
                          fileproject.close()
                          break
                      else:
                       print("notvalid")
                       continue
                    else:
                        print("Not valid format")
                else:
                  print("notvalid")
                  continue
            else:
                print ("Not a valid format")
                continue
        else:
            print("Not a valid number ")
            continue
    else:
        print("Not valid name")
        continue
def view():
  try:
    fileproject=open("project.txt","r")
  except Exception as e :
    print(e)
  else:
    projects=fileproject.read()
    print(projects)

def delete():
    with open("project.txt", 'r') as filedata:
      inputFilelines = filedata.readlines()
      projname=input("please enter your project name: ")
      projid=input("please enter your project id : ")
      for i in inputFilelines:
        info=i.strip("\n")
        info=i.split(":")
        if (info[0]==projid and info[1]==projname):
          inputFilelines.remove(i)
          break
      with open("project.txt", 'w') as filedata:
       filedata.writelines(inputFilelines)
       filedata.close()

def edit():
  with open("project.txt", 'r') as filedata:
      inputFilelines = filedata.readlines()
      projname=input("please enter your project name: ")
      projid=input("please enter your project id : ")
      for i in inputFilelines:
        info=i.strip("\n")
        info=i.split(":")
        if (info[0]==projid and info[1]==projname):
          inputFilelines.remove(i)
          break 
      with open("project.txt", 'w') as filedata:
       filedata.writelines(inputFilelines)
       filedata.close()
      while True:
       title=input("please enter the title of your project :")
       if title.isalpha():
        details=input("please enter some details : ")
        totaltarget=input("Please set a total target: ")
        if totaltarget.isnumeric():
            startdate=input("please enter the start date in the form of dd/mm/yy :")
            r1 = re.compile('.*/.*/.*')
            if r1.match(startdate) is not None:
                day1,month1,year1=startdate.split('/')
                validstartdate=True
                try:
                  datetime.datetime(int(year1),int(month1),int(day1))
                except ValueError :
                 validstartdate=False
                if(validstartdate):
                    enddate=input("please enter the end date in the form of dd/mm/yy :")
                    r2 = re.compile('.*/.*/.*')
                    if r2.match(enddate) is not None:
                      day2,month2,year2=enddate.split('/')
                      validenddate=True
                      try:
                        datetime.datetime(int(year2),int(month2),int(day2))
                      except ValueError :
                           validenddate=False
                      if(validenddate):
                        
                        def id():
                          with open(r"project.txt", 'r') as id:
                           x = len(id.readlines())
                           global project_id
                           project_id=x+1
                           return project_id
                        print("Your project is edited successfully")
                        print (f"your new project id is {id()}")
                        projectdetails=(f"{id()}:{title}:{details}:{totaltarget}:{startdate}:{enddate}\n")
                        try:
                         fileproject=open("project.txt","a")
                        except Exception as e:
                          print(e)
                        else:
                          fileproject.write(projectdetails)
                          fileproject.close()
                          break
                      else:
                       print("notvalid")
                       continue
                    else:
                        print("Not valid format")
                else:
                  print("notvalid")
                  continue
            else:
                print ("Not a valid format")
                continue
        else:
            print("Not a valid number ")
            continue
       else:
        print("Not valid name")
        continue
      #createproject()   
                
        
         
          
        
    


while True:       
 ans=input("please enter \n 1)create project \n 2)view projects \n 3)delete project \n 4)Edit project \n")
 if ans=="1":
    createproject()
    continue
 elif ans=="2":
    view()
    continue
 elif ans=="3":
    delete()
    continue
 elif ans=="4":
  edit()
  continue
 else:
    print ("invalid input") 
    continue