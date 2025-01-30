# The comments are represented by hashtag(#) and these are ignored by the computer

#operations using numbers
print(120+120)
print(120-120)
print(120*120)
print(120/120)
print(120//120)
print(120**120)

#operations using variables
uday=50
sai=100
print(uday+sai)
print(uday-sai)
print(uday*sai)
print(uday/sai)
print(uday//sai)
print(uday**sai)

#using strings
print("saalar")
print('kgf-1')
print("kgf-2")

#using length
print(len("saalar"))
hello="world"
print(len(hello))
hello="earth"
print(len(hello))

# using type operator
poorna="999.999"
print(type(uday))  #shows the type #

# using index 
index_var="The Dark Knight is one of the best Batman movies for a reason"
print(index_var[5])
print(index_var[18])

# using index with range (slicing)
print(index_var[10:30])    #displays the range of that dialouge from 10 to 30


#NUMERICS#

# slicing using strings with positive indexing
str1="veerashankarreddy, mokke kadha ani pikesthe peeka kostha"
print(str1[7: ])
print(str1[7: 23])
print(str1[24])
print(str1[23: 7: -1])
print(str1[23: 7])

# slicing using strings with negative indexing
print(str1[-24: -7])
print(str1[-7:-24: -1])
print(str1[-4: -30: -3])

# to know the address value assigned in memory block for a particular variable
str1='hello'
print(id(str1))
str2='hello'
print(id(str2))
str3='hello'
print(id(str3))
str4='world'
print(id(str4))
str5='world'
print(id(str5))
str6='world'
print(id(str6))

# ..................few datatypes in python.......................
# int(example:2,56,12345, and so on)
2
print(type(2))
# float(example:21.23,5.6,12345.33333, and so on)
5.6
print(type(5.6))
# complex(example:2+3j,6+7j, and so on)
6+7j
print(type(6+7j))
# string(example:'hey',"there", and so on)
str1='hey'
print(type(str1))


# strings are immutable as their sub strings cannot be changed once declared but we can re-assign the entire string to avoid ambiguity in python
str2='Hey There!! How you doing..'
print(str2[12]) 
#now lets try to change a specific index value
str2[12]='p'
print(str2[12])  #it throws an error as strings are immutable and connot be changed but can be re-assigned (the entire string should be changed).

# an alternative is re-assigning it.
str2='Hey There!! pow you doing..'
print(str[12])