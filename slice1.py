#slice operator

s ='digipodium'
slice1 = s[0:4]
print(slice1)


#getting slice

s ='digipodium'
slice1 = s[0:-4]
slice2 = s[:4]  # without zero also means same
print(slice1)
print(slice2)

#using len to get podium

s = 'digipodium'
slice1 = s[4:len(s)]
slice2 = s[4:]
print(slice1)
print(slice2)