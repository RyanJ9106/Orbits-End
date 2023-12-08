import time
import sys

def typewriter_print(text, delay=0.03, skip_typewriter=False):
    if skip_typewriter:
        print(text)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

class CosmicEscapeGame:
    def __init__(self):
        self.skip_typewriter = False  # Flag to control the typewriter feature
        self.rooms = {
            "Entrance Hall": {
                "description": "You're in the Entrance Hall. Doors lead in multiple directions.",
                "exits": {"north": "Galley", "east": "Medical Bay", "south": "Engineering"},
                "items": [],
                "trap": False
            },
            "Galley": {
                "description": "You're in the Galley. There's a smell of old food.",
                "exits": {"south": "Entrance Hall", "east": "Storage Room", "west": "Observation Deck"},
                "items": ["food supplies"],
                "trap": False
            },
            "Medical Bay": {
                "description": "You're in the Medical Bay. Shelves of medical supplies line the walls.",
                "exits": {"west": "Entrance Hall", "north": "Storage Room"},
                "items": ["medkit"],
                "trap": False
            },
            "Engineering": {
                "description": "You've entered Engineering. The heart of the ship's operations.",
                "exits": {"north": "Entrance Hall", "east": "Observation Deck"},
                "items": ["engine parts"],
                "trap": True,
                "trap_item": "wrench"
            },
            "Storage Room": {
                "description": "This is the Storage Room. Various items are scattered around.",
                "exits": {"south": "Medical Bay", "west": "Galley"},
                "items": ["wrench"],
                "trap": False
            },
            "Observation Deck": {
                "description": "You're on the Observation Deck. The view of space is breathtaking.",
                "exits": {"east": "Galley", "west": "Engineering"},
                "items": ["star map"],
                "trap": False
            }
        }
        self.reset_game()

    def reset_game(self):
        self.current_room = "Entrance Hall"
        self.inventory = []
        self.game_over = False
        self.has_won = False
        self.timer = 600

    def describe_current_room(self):
        room = self.rooms[self.current_room]
        typewriter_print(room['description'], skip_typewriter=self.skip_typewriter)
        if room["items"]:
            typewriter_print("Items here: " + ", ".join(room["items"]), skip_typewriter=self.skip_typewriter)
        typewriter_print("Exits: " + ", ".join(room["exits"].keys()), skip_typewriter=self.skip_typewriter)
        print("-" * 30)

    def move(self, direction):
        if direction in self.rooms[self.current_room]["exits"]:
            self.current_room = self.rooms[self.current_room]["exits"][direction]
            if self.rooms[self.current_room]["trap"]:
                self.trigger_trap()
            else:
                self.describe_current_room()
        else:
            typewriter_print("No exit in that direction.", skip_typewriter=self.skip_typewriter)

    def trigger_trap(self):
        trap_item_required = self.rooms[self.current_room].get("trap_item", None)
        if trap_item_required and trap_item_required in self.inventory:
            typewriter_print("You use the " + trap_item_required + " to neutralize the trap.", skip_typewriter=self.skip_typewriter)
            self.describe_current_room()
        else:
            typewriter_print("You've triggered a trap! Game over.", skip_typewriter=self.skip_typewriter)
            self.game_over = True

    def take_item(self, item):
        if item in self.rooms[self.current_room]["items"]:
            self.inventory.append(item)
            self.rooms[self.current_room]["items"].remove(item)
            typewriter_print("You have taken the " + item + ".", skip_typewriter=self.skip_typewriter)
        else:
            typewriter_print("There is no " + item + " in this room.", skip_typewriter=self.skip_typewriter)

    def show_tutorial(self):
        typewriter_print("\n--- TUTORIAL ---", skip_typewriter=self.skip_typewriter)
        typewriter_print("1. Movement: Use 'north', 'south', 'east', 'west' to move between rooms.", skip_typewriter=self.skip_typewriter)
        typewriter_print("2. Picking Items: Type 'take [item]' to collect items you find.", skip_typewriter=self.skip_typewriter)
        typewriter_print("3. Using Items: Some items are needed to avoid traps or unlock paths.", skip_typewriter=self.skip_typewriter)
        typewriter_print("4. Objective: Navigate the station, avoid traps, and collect useful items.", skip_typewriter=self.skip_typewriter)
        typewriter_print("5. Time Limit: You have 10 minutes to escape.", skip_typewriter=self.skip_typewriter)
        typewriter_print("6. Map: Type 'map' to view the station layout.", skip_typewriter=self.skip_typewriter)
        typewriter_print("7. Quitting: Type 'quit' to exit the game.", skip_typewriter=self.skip_typewriter)
        typewriter_print("8. Typewriter Feature: Type 'skip' to toggle on/off the typewriter text effect.", skip_typewriter=self.skip_typewriter)
        typewriter_print("Enjoy exploring and be cautious on your journey through the space station!", skip_typewriter=self.skip_typewriter)
        input("\nPress Enter to confirm you have read the tutorial and start the game.\n")

    def show_map(self):
        typewriter_print("""
+------------------+   +------------------+   +------------------+
| Observation Deck |---|     Galley       |---|  Storage Room    |
+------------------+   +------------------+   +------------------+
         |                      |                     |
+------------------+   +------------------+   +------------------+
|    Engineering   |---|   Entrance Hall  |---|    Medical Bay   |
+------------------+   +------------------+   +------------------+

        """, skip_typewriter=self.skip_typewriter)

    def start_game(self):
        self.show_tutorial()
        start_time = time.time()
        self.describe_current_room()

        while not self.game_over and not self.has_won and time.time() - start_time < self.timer:
            command = input("YOUR COMMAND > ").lower().split()
            if command:
                action = command[0]
                if action in ["north", "south", "east", "west"]:
                    self.move(action)
                elif action == "take" and len(command) > 1:
                    self.take_item(" ".join(command[1:]))
                elif action == "map":
                    self.show_map()
                elif action == "skip":
                    self.skip_typewriter = not self.skip_typewriter
                    typewriter_print("Typewriter text feature toggled.", skip_typewriter=self.skip_typewriter)
                elif action == "quit":
                    typewriter_print("Quitting game.", skip_typewriter=self.skip_typewriter)
                    break
                else:
                    typewriter_print("Invalid command.", skip_typewriter=self.skip_typewriter)
            else:
                typewriter_print("Enter a command.", skip_typewriter=self.skip_typewriter)

            if self.current_room == "Control Center" and "keycard" in self.inventory:
                self.has_won = True
                typewriter_print("Using the keycard, you initiate the escape sequence. Congratulations, you've escaped the station!", skip_typewriter=self.skip_typewriter)

        if not self.game_over and time.time() - start_time >= self.timer:
            typewriter_print("Time's up! The station explodes with you in it. Game over.", skip_typewriter=self.skip_typewriter)

        if self.has_won:
            typewriter_print("You've successfully escaped the station. Well done!", skip_typewriter=self.skip_typewriter)

        return self.game_over or self.has_won

def game_loop():
    game = CosmicEscapeGame()
    while True:
        game_end = game.start_game()
        if game_end:
            retry = input("Try again? (yes/no): ").lower()
            if retry != "yes":
                typewriter_print("Thank you for playing!", skip_typewriter=game.skip_typewriter)
                break
            game.reset_game()

game_loop()
