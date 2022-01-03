import random
import os

def writeFile(a, b):
    file = open(b, "w") 
    file.write(a) 
    file.close()

captcha = random.randint(100000, 999999)
filecontain = '''<title>captcha code</title>
<h1>your code is : ''' + str(captcha) + '</h1>'
writeFile(filecontain, "captcha.html")
print("Hello! This app using captcha! Find the \"captcha.html\" file in program folder, and open it in browser.\nCopy-paste the number to box below:")
user = input("Your code: ")
if int(user) == captcha:
    writeFile("<h1>captcha is already solved</h1>", "captcha.html") 
    os.system('python program.py')
else:
    writeFile("<h1>captcha is already unsolved</h1>", "captcha.html")
    print("I'm sorry but the captcha is wrong.")
    input("PRESS ENTER")