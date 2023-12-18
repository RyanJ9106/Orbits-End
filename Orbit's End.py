import time
import sys

key = False
flashlight = False
lever = False
trap = False

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
    global lever

    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou are back where you started, this cycle doesnt seem to end...")
    

    if flashlight == True:
        choice1 = input("You see two doors again both closed but seem unlocked (1 or 2). You come back into the room with the flashlight on and see the room goes deeper.... (3): ")

        if choice1 == "3":
            print("\nYou search deeper into the darkness of this room you have seen plenty of times now using your flashlight, its weird, it always seems to lead back to this room...........\nYou keep seaching to find a lever of some kind.")
            lever == True
            time.sleep(5)
            sroom()


    if flashlight == False:
        choice1 = input("You see two doors again both closed but seem unlocked (1 or 2): ")

    if choice1 == "1":
            print("\nYou approach the door on the right and it makes a loud hissing noise and then slowly opens revealing the next room.")
            time.sleep(5)
            room1()

    if choice1 == "2":
        print("\nYou creep over to the door on the right, smoke floods from around it a loud beep noise echos around the room, you enter into the next room.")
        time.sleep(5)
        room2()

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
    choice1 = input("There seems to be a door straight on(1) and a door to your left(2), where shall you go or shall you keep searching this room(3)? (go back (4)): ")

    if choice1 == "1":
        print("\nYou look straight on and approach the other door and theres no handle but as you approach it just seem to open by its self.... weird.....")
        time.sleep(5)
        room3()

    if choice1 == "2":
        print("\nYou turn left and go towards the door, you reach for the handle and open the door nothing happens......")
        time.sleep(5)
        room2()

    if choice1 == "3" and flashlight == True:
        print("\nYou dive deeper into the room but its too dark to see, you turn on your flashlight and find a key.")
        key = True
        time.sleep(5)
        room1()

    if choice1 == "3":
        print("\nYou dive deeper into the room but its too dark to see, you turn around and go back.")
        time.sleep(5)
        room1()
    
    if choice1 == "4":
        print("\nYou go back to the room you awoke in.")
        time.sleep(5)
        sroom()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room1()

#########################################################################################################################################################
    
def room2():
    global flashlight
    global trap
    
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

    if choice1 == "3" and trap == True:
        print("\nYou approach the huge door, it appears to be stuck becuase of the blockage on the other side...")
        time.sleep(5)
        room2()

    if choice1 == "3":
        print("\nYou approach the huge door, as it towers over you, you hear a deafening bang on the other side...... \nthe door continues to open you cathc a glimpse of something scuttle away")
        time.sleep(5)
        room4()
    
    if choice1 == "4":
        print("\nYou stay in the room and with the light pouring through the giant domed window, you manage to find a flashlight hidden below a box.")
        flashlight = True
        time.sleep(5)
        room2()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room2()

#########################################################################################################################################################
        
def room3():
    global key
    
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou enter the room a stench fills the air as you realise the room your standing in is a control room, you quickly realise this key be it.... the way out....")
    choice1 = input("You can either go through the door behind you(1), the door to your left(2) or continue searching(3): ")

    if choice1 == "1":
        print("\nYou turn around and reach for the door handle, the door opens.... you get an odd shiver down your spine....")
        time.sleep(5)
        room1()
    
    if choice1 == "2":
        print("\nTurning left you go towards the door, the door starting pounding you quickly press the button to open the door and there stands...... nothing......")
        time.sleep(5)
        room4()
    
    if choice1 == "3":
        choice2 = input("\nYou start frantically looking around for some form of control pannel and there seems only to be a control pannel(1).(go back 2): ")

        if choice2 == "1" and key == True:
            print("\nYou insert the key into the control pannel, your hands trembling, the system displays a message....")
            text = f"\nHello {Name}, ACCESS GRANTED....... ESCAPE POD ACTIVE......"

            for char in text:
                print(char, end='')
                sys.stdout.flush()
                time.sleep(.25)

            time.sleep(5)            
            print("\nYou get into the escape pod, a feeling of relief covers you, the pod proceeds to set off, you turn back and see an ominous figure standing in the window of the control room.......")
            time.sleep(5)
            print("\nYou realise you have no clue where this pod is taking you so you deicde to fall asleep.......")
            time.sleep(5)
            text1 = f"\nYou wake up in a bare metal room lit by only a single red siren light, as your hearing comes back your start to hear a siren noise screaching........ 'WELCOME BACK {Name}'..............."

            for char in text1:
                print(char, end='')
                sys.stdout.flush()
                time.sleep(.25)

            time.sleep(3)

            print("\nThank You for playing Orbit's End!")
            exit()

        if choice2 == "1":
            print("\nYou quickly realise theres a key hole, you dont have a key.....")
            time.sleep(5)
            room3()

        if choice2 == "2":
            room3()
        
        else:
            print("\nYou do nothing....")
            time.sleep(3)
            room3()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room3()

#########################################################################################################################################################
        
def room4():
    global lever
    global trap

    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nYou enter the dingy room you gag as the stench of rotting fills the air.... this room seems empty i wonder where the stench is coming from..... The ceiling caves in as you enter the room blocking you from entering the room with the huge window")
    trap = True
    choice1 = input("You can either go though the door on the right(1) or continue inspecting this room(2): ")

    if choice1 == "1":
        print("You turn right and open the door expecting something to jump out at you and nothing.....")
        time.sleep(5)
        room3()
    
    if choice1 == "2":

        if lever == True:
            print(f"You continue inspecting and find a hole for a lever, you put the lever you found into the hole..... you pull the lever and you hear a whispering growling voice.....")
            time.sleep(5)
            text = f"IvE BeEen WaITinG FoR yoU {Name.upper}"

            for char in text:
                print(char, end='')
                sys.stdout.flush()
                time.sleep(.25)
            
            print("You freak out as something pulls you into this trap door you opened.... both of your legs get torn off, twisting and pulling them.... your eyes gouged out....\nYou let out a blood curdling scream and your lower jaw is unhinged and twisted....")
            time.sleep(7)
            print("\nThank You for playing Orbit's End!")
            exit()

        if lever == False:
            print(f"You continue inspecting and find a hole for a lever, you have no lever i wonder where one could be.....")
            time.sleep(5)
            room4()

        else:
            print("\nYou do nothing....")
            time.sleep(3)
            room4()

    else:
        print("\nYou do nothing....")
        time.sleep(3)
        room4()

#########################################################################################################################################################

print("Hello and welcome to Orbit's End to begin please enter your name below")
Name = input("Name: ")

input(f"\nWelcome {Name} please press enter to wake up: ")
sroomS()