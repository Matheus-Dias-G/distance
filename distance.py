ax = int(input('input the Ax value: '))
ay = int(input('iput the Ay value: '))
bx = int(input('input the Bx value: '))
by = int(input('iput the By value: '))
#1th way
val_1 = (bx-ax)**2
val_2 = (by-ay)**2
dsum = val_1 + val_2
droot = dsum**0.5

print('distance of A to B is:', droot)

#2th way
#resp = (((bx-ax)**2)+((by-ay)**2))**0.5

#print('distance of A to B is:', resp)

