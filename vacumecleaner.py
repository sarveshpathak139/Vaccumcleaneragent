import time
print ("\nVacume cleaner agent\n")
room1 = [1,3,5,7,9,11,13]
room2 = [2,4,6,8,10,12,14]
vacume = []
while True:
  
    print ("\n========================================= \n")
    print ("\n\t ***************  Menu  ****************\n")
    print ("\n\t\t 1. Automatically ")
    print ("\n\t\t 2. Manualy ")
    print ("\n\t\t 3. Exit ")
    print ("\n==================================================================================== \n")
    choice2 = input("\nEnter your Choice ==>  ")
    if choice2 == 1:
        while True:
            print ("\n ******* Garbage Present in room and vacume cleaner ********\n")
            print ("\n Room 1 ==>",room1,"\n")
            print ("\n Room 2 ==>",room2,"\n")
            print ("\n Vacume Cleaner ==>",vacume,"\n" )
            print ("\n==================================================================================== \n" )
            if len(room1) == len(room2):
                time.sleep(1)
                if len(room1) != 0:
                    popg = room1.pop()
                    vacume.append(popg)
                else:
                    vacume = []
                    print ("\n ******* Garbage Present in room and vacume cleaner ********\n")
                    print ("\n Room 1 ==>",room1,"\n")
                    print ("\n Room 2 ==>",room2,"\n")
                    print ("\n Vacume Cleaner ==>",vacume,"\n" )
                    print ("\n============================ \n" )
                    print("\nRoom 1 is Cleaned")
                    print("\nRoom 2 is Cleaned")
                    print ("\nVacume Cleaner is empty \n")
                    break
            elif len(room1) != len(room2):
                time.sleep(1)
                if len(room2) != 0:                
                    popg = room2.pop()
                    vacume.append(popg)
            elif len(room1) == 0 and len(room2) == 0:
                time.sleep(2)
                break              
    elif choice2 == 2:
        room1 = [1,3,5,7,9,11,13,15]
        room2 = [2,4,6,8,10,12,14,16]
        vacume = []
        while True:
            print ("\n ******* Garbage Present in room and vacume cleaner ********\n")
            print ("\n Room 1 ==>",room1,"\n")
            print ("\n Room 2 ==>",room2,"\n")
            print ("\n Vacume Cleaner ==>",vacume,"\n" )
            print ("\n==================================================================================== \n")
            print ("\n *******  Menu  ********\n")
            print ("\n 1. Clean the Garbage using vacume cleaner\n")
            print ("\n 2. Empty the vacume Cleaner \n")
            print ("\n 3. Exit \n")
            print ("\n==================================================================================== \n")
            choice = input("\nEnter your Choice ==>  ")
            if choice == 1 and len(room1) == len(room2):
                if len(room1) != 0:
                    popg = room1.pop()
                    vacume.append(popg)
                else:
                    vacume = []
                    print ("\n ******* Garbage Present in room and vacume cleaner ********\n")
                    print ("\n Room 1 ==>",room1,"\n")
                    print ("\n Room 2 ==>",room2,"\n")
                    print ("\n Vacume Cleaner ==>",vacume,"\n" )
                    print ("\n==================================================================================== \n" )
                    print("\nRoom 1 is Cleaned")
                    print("\nRoom 2 is Cleaned")
                    print ("\nVacume Cleaner is empty \n")
                    break
            elif choice == 1 and len(room1) != len(room2):
                popg = room2.pop()
                vacume.append(popg)
            if choice == 2:
                vacume = []
                print ("\nvacume is empty \n")
            if choice > 2:
                break
    else:
        exit()
    