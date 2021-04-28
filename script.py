import subprocess
import sys


with open("dic.txt","r",encoding='ISO.8859.1') as fs:
    var= fs.read().splitlines()
for li in var:
    var1= li
    result= subprocess.getoutput("echo %s | ./beroot"%var1)
    print("testing password "+ var1)
    if "wrong password!!!" not in str(result):
        print(result)
        print("the password is: "+ var1)
        sys.exit(0)

