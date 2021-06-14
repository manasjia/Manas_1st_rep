

def list():
    list = [1,2,3,4, "1st", "2nd"]
    print(list[4])

    #after adding values
    list.append(20)
    print(list)
def tupple1():
   x = (1,2,3,4)
   print(type(x))
   print (x[3])


print("Before Name_gaurd ")
if __name__ == '__main__':
    x = int(input("Enter 1 for list and 2 for Tupple :"))
    if x == 1:
        list()
    elif x == 2:
        tupple1()
    else :
        print(" Enter the value 1  and 2 only")

print("After name_guard")