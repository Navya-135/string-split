#Split/splitlines/partition/rpartition
#split

#syntax:variableName.split(char/string)

fName="Rajesh"
middleName="Rana Pratap"
lName="Varma"
print(middleName.split(" "))

#splitlines

#syntax:variableName.splitlines( )

address=""" 4-111,
Budawada,
Gurazala,
Guntur
"""
print(address.splitlines())

#partition

#syntax:variableName.partition(string/char)

name="Rajesh123rana pratap@varma"
print(name.partition("123"))
print(name.partition("@"))

#rpartition

#syntax:variableName.rpartition(string/char)

name="Rajesh123rana pratap@varma"
print(name.partition("123"))
print(name.partition("@"))
