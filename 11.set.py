#show set data type
s1=set([5,6,7])
print(s1)

s2={2,3,4,5,2,4,5} #Duplicate value not allow
s3={11,12,13}
s2.add(6) #add single value
s2.update([7,8,9,10]) #add multiple value
s2.update(s3)
s2.remove(2)
print(s2)