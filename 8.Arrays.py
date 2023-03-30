from array import*
salary=array('i',[3000,4000,5000,6000])  #i=signed int(I,l,L,q,Q,f,d,h,H,b,B=type code)
print(salary) #O/P all
print(salary[2]) #O/P index number

#loop in array
from array import*
salary=array('f',[4500.50,5000.50,6000.60,7000.800]) #f=float
for f in range(4):
    print(salary[f])

# Functionality in array
from array import*
salary=array('i',[20000,30000,40000,50000])
print(salary.buffer_info()) #address and value search
print(salary.append(60000)) #add value
print(salary)
print(salary.remove(20000)) #remove value
print(salary)
print(salary.reverse())
print(salary)