#if-else
x=int(input("Enter the X value:"))
y=int(input("Enter the Y value:"))
if x>y:
  print("x is greater")
else:
  print("y is greater")

#nested if
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if a>b:
  if a>c:
    print("a  value is biggest value")
  else:
    print("c  value is biggest value")
elif b>c:
  print("b value is biggest value")
else:
  print("c value is biggest value")

#if-elif-else
x=int(input("Enter the X value:"))
y=int(input("Enter the Y value:"))
if x==y:
  print("both are equal")
elif x>y:
  print("x is greater")
else:
  print("y is greater")


#pass
num = [1,2,4,6,8,9,23,64,79]
for x in num:
  if x%2==0:
    pass # pass statement is null statement
  else:
    print(x)#it prints the null statement

