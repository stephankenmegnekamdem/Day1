ans1=1+11+111+1111+11111+111111+1111111+11111111+111111111
print(ans1)
for k in range(6):
    if k == 0:
       print()
    else: 
       print(pow(ans1,k))
ans2=1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111 
for l in range(6):
    if l == 0:
       print()
    else:
       print(pow(ans2,l))
ans3=1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111+11111111111
for m in range(6):
    if m == 0:
       print()
    else:
       print(pow(ans3,m))

num1 = 0
for i in range(10):
     for j in range(i):
        print (num1)
        num1=num1+pow(10,j)
        print (num1)
    
   
print (num1)
