import random
import time


def random_list_create(num):        #generate a random list of 100000 integers from 1 to 100
    my_random_list=[]
    for i in range(num):
        gen_num=random.randint(1,100)
        my_random_list.append(gen_num)
    return(my_random_list)

num=100000
my_random_list=random_list_create(num)

start=time.time()
def quick_sort(my_list):
    freq={}   #dictionary to store the frequency of each number and the number
    for i in my_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    new_list=[]

    maxi=0
    mini=0

   #find the smallest number
    for i in freq:
        if i>maxi:
            maxi=i

   #find the biggest number
    for i in freq:
        if i<mini:
            mini=i

    for i in range(mini, maxi+1):
        if i in freq:
            new_list.append(i)



    final_list=[]
    for i in new_list:
            for k in range(freq[i]):
                final_list.append(i)

    return final_list

my_list=quick_sort(my_random_list)
print(my_random_list)
print(my_list)
print(time.time()-start)


#i could still look for the largest number, calculate frequency of each number and from 1 to that big nnumber, if in dictionary, append to newsttring