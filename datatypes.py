#DATA TYPES#

str1="Rebulic day"
print(id(str1[0]))
print(id(str1[1]))
print(id(str1[2]))
print(id(str1[3]))
print(id(str1[4]))
print(id(str1[5]))
print(id(str1[6]))
print(id(str1[7]))
# why index start with zero
a=[1,2,3,4,5]
print(id(list[0]))
print(id(a[1]))
print(id(list[2]))
print(id(list[3]))
print(id(list[4]))
#RANGE
print(list(range(100,0,-1)))
print(list(range(0,100,-1)))#empty
print(list(range(0,100,3)))
print(list(range(0,5)))
print(list(range(100,45,-1)))
list1=[1,2,3,6,99]
for i in list1:
    print(len(list1))
    for i in range(0, len(list1)):
     print(i,list[i])
     num1=10
     for j in range(0,num1):
        print(j)
#DICTIONARY
#it indicates {}
#key values pairs
dict1={1:'apple',2:'bananna',3:'cherry',4:'draganfruit',5:'mango'}
print(dict1)
print(dict1[1])
dict1[3]='kalki'
print(dict1)
dict1['key1']='value1'
print(dict1)
dict1['key1']='updatedvalue'
print(dict1)
#SET-collection of elements-unique,unorderd,finite
set={1,2,3,1,2,3,3,3,3,}
print(set)
set1={35872,549687,74569238,63436,63436,63436,'vani1','vani2'}
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
#we can re-run the code order is change
set2={1,1,2,2,3,3,4,4,5,5}
print(set2)
#NONE
#there is no memory value it is a data type
num1=5
num1=None
print(num1)
print(type(num1))
print(id(num1))
#take user inputs
# input('enter a number')#string
# print(input('enter a number'))
# a=input("enter a number1")
# b=input("enter another number2")
# print(a+b)
a=int(input("enter a number1"))
b=int(input("enter another number2"))
print(type(a))
print(a+b)

#boolean
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#set
x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 


