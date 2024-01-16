'''
Las tuplas son inmutables
()
'''

tuplas=("uno", "dos", "tres")
print(tuplas)
print(type(tuplas))

tuplaVariosDatos=(12,True,23.6,"Nombre", 12+3j)

print(tuplaVariosDatos)

tuplascontuplas=(1,2,3,4,(1,2,3))
print(tuplascontuplas)

print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

a,b,c=tuplas

print(a)
print(b)
print(c)