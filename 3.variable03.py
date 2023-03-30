# escape sequence
x=' Nasir \n Uddin'
y="Nasir \t Uddin"
z='Nasir\'s Uddin'
print(x,y,z)

# global variable
x="Good Boy"
def func():
    print('Nasir is a ' + x)
func()

def myfunc():
    global x
    x="Bad Boy"
myfunc()
print('Nasir is Not a ' + x)