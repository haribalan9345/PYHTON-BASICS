'''#Ex:1
hari=1
cnt=0
while hari < cnt:
  print("Hey")
  hari+=1

print("GOOD JOB,THANKYOU")


#break and continue
#else after loop exhaustion
for n in range(2,10):
  for x in range(2,n):
    if n % x == 0:
      print n, 'equals',x, '*',n/x
      break
    else:
      print n , 'is prime'
      
#Ex 2
i=1
while i <= 8:
  print(i)
  i+=1


#CONTINUE (IT SKIPS FROM THE LOOP)
i=0
while i < 6:
  i+=1
  if i == 3:
    continue
  print(i)

#BREAK (IT BREAK THE LOOP)
i=0
while i < 6:
  i +=1
  if i==4:
    break
  print(i)

#for loop
f = ["Apple", "Banana", "Cheery"]
for x in f:
  print(x)


#for - continue
for x in 'PYTHON':
  if x=='H':
    continue
  print(x)'''

#for-else
for i in range(1,4):
  print(i)
  break
else:
  print("No break")










  

