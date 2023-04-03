student={1:{'name':'nasir',"age":24,'sex':'male'},
        2:{'name':'nazim',"age":18,'sex':'male'},
        3:{'name':'imran',"age":16,'sex':'male'}
         }
print(student)
print(student[1]) #O/P main key
print(student[2]['name']) #O/P nested key

#add key
student[4]={}
student[4]['name']='riya'
student[4]['age']='22'
student[4]['sex']='Female'
print(student[4])
print(student)

#delete
del student[3]
print(student)