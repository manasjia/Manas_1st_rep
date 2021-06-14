
import sys
import os
def squre(num):
    return num * num
def List(dir):
    filenames = os.listdir(dir)
    print(filenames)


if __name__ =="__main__":
    #user_num = int(input("Enter number "))
    #print (squre(user_num))
    print(sys.argv[0])
    List(dir)

