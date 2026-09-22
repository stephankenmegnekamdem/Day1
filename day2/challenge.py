list = []
for i in range(20):
  list.append(i+1)
ans=1
for j in range(20):
 for l in range(20):
  flag=0
  for k in range(20):
    if list[k]  % (j+1) == 0:
       flag=1
       list[k]=list[k]//(j+1)
  if flag==1:
    ans= ans*(j+1)
  
print("The LCM of all numbers from 1 to 20 is:", ans)

ist = []
for i in range(200):
  list.append(i+1)
ans=1       
for j in range(200):
 for l in range(200):
  flag=0
  for k in range(200):
    if list[k]  % (j+1) == 0:
       flag=1
       list[k]=list[k]//(j+1)
  if flag==1:
    ans= ans*(j+1)
    
print("The LCM of all numbers from 1 to 200 is:", ans)

ist = []
for i in range(2000):
  list.append(i+1)
ans=1       
for j in range(2000):
 for l in range(2000):
  flag=0
  for k in range(2000):
    if list[k]  % (j+1) == 0:
       flag=1
       list[k]=list[k]//(j+1)
  if flag==1:
    ans= ans*(j+1)
    
print("The LCM of all numbers from 1 to 2000 is:", ans)
