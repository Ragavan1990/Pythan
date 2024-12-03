class Allfunction():
 def Subfields():
  Lists=["SubFields In AI are: ","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
  for AI in Lists:
    print(AI)
 def OddEven():
    Num=int(input("Enter the value:"))
    if(Num%2==0):
        print(Num, "is Even Number")
    else:
        print(Num,"is Odd Number")
 def ElegibilityForMarriage():
    gender=input('Your Gender:')
    age=int(input('Your age:'))
    if (gender=="Male" and age>=21):
           print(gender,"With Age of",age,"is Eligible for marriage")
    elif(gender=="Female" and age>=18):
           print(gender,"With Age of",age,"is Eligible for marriage")
    else:
           print(gender,"With Age of",age,"is Not Eligible for marriage")
 def FindPercent():
    sub1=int(input("Enter the sub1 mark:"))
    sub2=int(input("Enter the sub2 mark:"))
    sub3=int(input("Enter the sub3 mark:"))
    sub4=int(input("Enter the sub4 mark:"))
    sub5=int(input("Enter the sub5 mark:"))
    Total=sub1+sub2+sub3+sub4+sub5
    Percentage=Total/5
    print("Subject 1 Marks:",sub1)
    print("Subject 2 Marks:",sub2)
    print("Subject 3 Marks:",sub3)
    print("Subject 4 Marks:",sub4)
    print("Subject 5 Marks:",sub5)
    print("Total marks of all subject:",Total)
    print("Percentage of five marks:",Percentage)
 def triangle1():
    height=int(input("Enter the Height:"))
    breadth=int(input("Enter the breadth:"))
    print("Height:",height)
    print("Breadth:",breadth)
    print("Area Formula:Height*Breadth)/2")
    area=height*breadth/2
    print("Area of the triangle:",area)
 def triangle2():
    height1=int(input("Enter the Height1:"))
    height2=int(input("Enter the Height2:"))
    breadh2=int(input("Enter the Breadth:"))
    print("Enter the Height1:",height1)
    print("Enter the Height2:",height2)
    print("Enter the Breadth1:",breadh2)
    perimeter=height1+height2+breadh2
    print("Perimeter formula:Height1+Height2+Breadth")
    print("Perimeter of triangle:",perimeter)