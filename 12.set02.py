s1={1,2,3,4,5}
s2={4,5,6,7}
s3={5,6,9,8}
s4=s1.intersection(s2)
s5=s1.intersection(s2,s3)
s6=s1.difference(s2)
s7=s1.symmetric_difference(s2)
print(s4)
print(s5)
print(s6)
print(s7)

set1={1,2,3,4,5,6,1,2,3}
set2={6,7,8,9} 
result=set(set1) #remove duplicate value
result=set(set1).difference(set2)
result=set(set2).difference(set1)
result=list(set(set1)) #show list data type 
print(result)