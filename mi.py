totalFloors = 10
myFloor = 5
liftPosition = 1

for floor in range(liftPosition, totalFloors+1):    
    print(">> Floor #", floor)
    if floor ==myFloor:
        print("you are arived")
        break
    
