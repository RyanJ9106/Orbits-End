import time

key = False
flashlight = False

#########################################################################################################################################################

def sroomS():
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou wake up in a bare metal room lit by only a single red siren light, as your hearing comes back your start to hear a siren noise screaching.")
    choice1 = input("You see two doors both closed but seem unlocked where shall you go? (1 or 2): ")

    if choice1 == "1":
        print("\nYou approach the door on the right, it makes a loud hissing noise and then slowly opens revealing the next room.")
        time.sleep(5)
        room1()

    if choice1 == "2":
        print("\nYou creep over to the door on the right, smoke floods from around it a loud beep noise echos around the room, you enter into the next room.")
        time.sleep(5)
        room2()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        sroomS()

#########################################################################################################################################################

def sroom():
    global flashlight

    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou are back where you started, this cycle doesnt seem to end...")
    choice1 = input("You see two doors again both closed but seem unlocked (1 or 2). You come back into the room with the flashlight on and see the room goes deeper.... (3): ")

    if choice1 == "1":
            print("\nYou approach the door on the right and it makes a loud hissing noise and then slowly opens revealing the next room.")
            time.sleep(5)
            room1()

    if choice1 == "2":
        print("\nYou creep over to the door on the right, smoke floods from around it a loud beep noise echos around the room, you enter into the next room.")
        time.sleep(5)
        room2()

    if choice1 == "3":
        print("\nNo flashlight")
        time.sleep(5)
        sroom()


    if choice1 == "3" and flashlight == True:
        print("\nYou search deeper into the darkness of this room you have seen plenty of times now using your flashlight, its weird, it always seems to lead back to this room...........\nYou keep seaching to find a lever of some kind.")
        time.sleep(5)
        sroom()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        sroom()

#########################################################################################################################################################

def room1():
    global flashlight
    global key

    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou enter the cluttered storage room, sharp nails, cockroaches and dust create a disgusting layer that covers the ground.")
    choice1 = input("There seems to be 2 door ways that lead to other rooms both seem unlocked, where shall you go(2 or 3) or shall you keep searching this room(4)? (go back (1)): ")

    if choice1 == "1":
        print("\nYou go back to the room you awoke in.")
        time.sleep(5)
        sroom()
    
    if choice1 == "2":
        print("\nYou turn left and go towards the door, you reach for the handle and open the door nothing happens......")
        time.sleep(5)
        room2()
    
    if choice1 == "3":
        print("\nYou look straight on and approach the other door and theres no handle but as you approach it just seem to open by its self.... weird.....")
        time.sleep(5)
        room3()

    if choice1 == "4":
        print("\nYou dive deeper into the room but its too dark to see, you turn around and go back.")
        time.sleep(5)
        room1()
    
    if choice1 == "4" and flashlight == True:
        print("\nYou dive deeper into the room but its too dark to see, you turn on your flashlight and find a key.")
        key = True
        time.sleep(5)
        room1()
    
    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room1()

#########################################################################################################################################################
    
def room2():
    global flashlight
    
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou enter a room the lights flicker on, a huge window reveals its self displaying earth in a ruined state....")
    choice1 = input("You see multiple doors one leading to the area you awoke in(1), a door leading into a room on the right(2) and another door straight ahead(3), where shall you go, or shall you keep looking around?(4): ")

    if choice1 == "1":
        print("\nYou go back to the room you awoke in.")
        time.sleep(5)
        sroom()
    
    if choice1 == "2":
        print("\nYou go towards the door and it makes an odd noise as you get closer, the noise builds and builds.... you open the door and nothing is there how odd.......")
        time.sleep(5)
        room1()

    if choice1 == "3":
        print("\nYou approach the huge door, as it towers over you, you hear a deafening bang on the other side...... \nthe door continues to open you cathc a glimpse of something scuttle away")
        time.sleep(5)
        room4()
    
    if choice1 == "4":
        print("\nYou stay in the room and with the light pouring through the giant domed window, you manage to find a flashlight hidden below a box.")
        flashlight == True
        time.sleep(5)
        room2()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room2()

#########################################################################################################################################################

print("Hello and welcome to Orbit's End to begin please enter your name below")
Name = input("Name: ")

input(f"\nWelcome {Name} please press enter to wake up: ")
sroomS()
