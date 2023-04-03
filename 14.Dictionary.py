d1={'Name':'Nasir','age':24,'DOB':'09-09-2000'} #key always unique(name,age,dob ect)
d2={'Name': 'Nasir Uddin',10:5,10.5:20,(4,5):76} #any dta type input
print(d1)
print(d2)
d3=d1.copy() #copy variable
print(d3)
print(d1['DOB']) #O/P single key
d1['varsity']=('BUBT') #add key 
print(d1)
d1.pop('varsity') #remove key
print(d1)
d2.clear() #revome all key
print(d2)
d4=len(d2)
print(d2)