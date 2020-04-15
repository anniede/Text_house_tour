#Intro
def title():
    print("     ")
    print("     ")
    print("     ")
    print("**********************************")
    print("THE BEACH COTTAGE")
    print("**********************************")
    print("     ")
    print("     ")
    print("     ")

def intro():
    print("     ")
    print("     ")
    print("     ")
    print("**********************************")
    print("INTRODUCTION:")
    print("**********************************")
    print("     ")
    print("""This is a text tour of a small home.  I made this as a way to practice with Python's if / while statements.
I hope you enjoy this tour.  If you see an issue with this little program or have a tip to help me learn Python, 
please feel free to contact me at the email below.

Anita Keller
anniede at gmail.com""")
    print("     ")
    print("     ")
    print("     ")

def instructions():
    print("     ")
    print("     ")
    print("     ")
    print("**********************************")
    print("INSTRUCTIONS:")
    print("**********************************")
    print("     ")
    print("""This is a text-based adventure through a beach house. If you've ever read a \"Choose your own adventure\" book, 
then you will be familiar with this format. Your job is to read through the text and make decisions. Choices are made by
typing in the UPPERCASE word(s) of the choice you want to do.""")
    print("     ")
    print("     ")
    print("     ")


#different rooms and locations
def sidewalk():
    print("**********************************")
    print("SIDEWALK")
    print("**********************************")
    print("     ")
    print("""You are standing on the sidewalk in front of a small beach cottage clad in white siding and topped 
with black shingles.  A white picket fence surrounds the well-manacured yard.  

You can hear the waves crashing onto the shore behind the house. 

You have 2 choices:  
    Enter the FRONT yard through the front gate
    Follow the fenceline around to the BEACH behind the house.""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "front" and answer != "beach":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "beach":
        beach()
    elif answer == "front":
        front_yard()

def beach():
    print("**********************************")
    print("BEACH")
    print("**********************************")
    print("     ")
    print("""The beach is a beautiful expanse of white that stretches out to the right and left of the house. Waves
crash on the shore.  Big puffy clouds hang in the sky but the sun feels warm and welcoming on your skin.  

The beach cottage sits at the edge of the sand.  The same white picket fence you saw in the front of the house surrounds
the back yard too.   

You have 2 choices:
     Go to the SIDEWALK in front of the house
     Enter the BACK yard""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "back" and answer != "sidewalk":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "sidwalk":
        sidewalk()
    elif answer == "back":
        back_yard()


def front_yard():
    print("**********************************")
    print("FRONT YARD")
    print("**********************************")
    print("     ")
    print("""The front yard is meticulously maintained with an assortment of flowers, bushes, and grass.  The front 
porch is just step up from the ground and has no railing.  Two chairs sit on the porch, with a small table in between.  
A red front door beckons to you. 

You have 2 choices:
     ENTER the house through the front door 
     Go back to the SIDEWALK""")

    # answer
    answer = input("What is your choice: ").lower().strip()

    # choices_path
    while answer != "enter" and answer != "sidewalk":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "enter":
        living_room()
    elif answer == "sidewalk":
        sidewalk()

def living_room():
    print("**********************************")
    print("LIVING ROOM")
    print("**********************************")
    print("     ")
    print("""You enter a small living room tastefully decorated in a bach theme.  The walls are white and the floors are 
covered with a brown carpet. A white couch with teal accent pillows sit before a small fireplace.  Two chairs and a few 
side tables are scattered throughout the room.  On the walls are paintings of seascapes and across the mantel sit 
various seashells.

You can see what looks like a dining room through one doorway.  A bedroom sits off to the side.

You have 3 choices:
     Enter the FRONT bedroom 
     Enter the DINING room
     EXIT the house""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "front" and answer != "dining" and answer != "exit":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "front":
        BR1()
    elif answer == "dining":
        dining()
    elif answer == "exit":
        front_yard()

def BR1():
    print("**********************************")
    print("FRONT BEDROOM")
    print("**********************************")
    print("     ")
    print("""You enter a bedroom which holds two twin beds.  Each bed is neatly made and decorated with pillows and 
various stuffed animals.  The walls are a light pink and the carpet is the same light brown as in the rest of the 
house.  In between the beds sits a low dresser with a lamp and a stack of books.  A small closet lines one wall,  
filled with small dresses and dainty shoes.

Through one door is what looks to be a bathroom.  Through the other is the cottage's living room.       

You have 2 choices:
     Go into the LIVING room 
     Go into the BATH""")

    # answer
    answer = input("What is your choice: ").lower().strip()

    # choices_path
    while answer != "bath" and answer != "living":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "living":
        living_room()
    elif answer == "bath":
        bath()

def bath():
    print("**********************************")
    print("BATHROOM")
    print("**********************************")
    print("     ")
    print("""The bathroom is a pass through bath with doorways leading to the 2 bedrooms in the house.  The main color
of the room is white with dark blue accents along the top, bottom and center of the tile walls.  There is a counter with 
two sinks, along one side and a shower / bathub combo and toilet on the other.  A silver medicine cabinet is set into 
the wall above the counter with a small window on either side.  A set of 4 toothbrushes in a metal holder sits on the 
counter waiting to be used.    

You have 2 choices:
     Enter the BACK bedroom 
     Enter the FRONT bedroom""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "back" and answer != "front":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "back":
        BR2()
    elif answer == "front":
        BR1()

def BR2():
    print("**********************************")
    print("BACK BEDROOM")
    print("**********************************")
    print("     ")
    print("""This bedroom looks to be the master bedroom.  A queen size bed sits in the center of the room with side
tables on either side.  Dressers sit along two of the walls, their tops cleared.  A closet lines the last wall, filled
with all sorts of clothes.

You can see a bathroom counter through one door and the dining room through another.  

You have 2 choices:
     Enter the DINING room 
     Enter the BATH""")

    # answer
    answer = input("What is your choice: ").lower().strip()

    # choices_path
    while answer != "dining" and answer != "bath":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "dining":
        dining()
    elif answer == "bath":
        bath()

def dining():
    print("**********************************")
    print("DINING ROOM")
    print("**********************************")
    print("     ")
    print("""The dining room is small with an equally small table and chairs in the center of the room.  A buffet sits
off to one side.  You peak into the cupboards of the buffet to see all the china used for the family's holiday dinners.

In one direction is a bedroom with a queen-size bed.  In another is the living room.  In the back of the room is a 
doorway which probably leads to the kitchen.     

You have 3 choices:
     Enter the LIVING room 
     Enter the BACK bedroom
     Enter the KITCHEN""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "living" and answer != "back" and answer != "kitchen":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "living":
        living_room()
    elif answer == "back":
        BR2()
    elif answer == "kitchen":
        kitchen()

def kitchen():
    print("**********************************")
    print("KITCHEN")
    print("**********************************")
    print("     ")
    print("""The kitchen is small but spotless.  White tiles and cabinets line the walls.  A black granite counter and 
dark cabinet handles offset all of the white.  A white country sink is sunk into the counter just under the window.  A 
small table with four chairs sits in one corner.

A door leads to the backyard and another leads deeper into the house to what looks like a dining room.    

You have 2 choices:
     Enter the DINING room
     Exit to the BACKYARD""")

    # answer
    answer = input("What is your choice: ").lower().strip()

    # choices_path
    while answer != "dining" and answer != "backyard":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "dining":
        dining()
    elif answer == "backyard":
        back_yard()

def back_yard():
    print("**********************************")
    print("BACKYARD")
    print("**********************************")
    print("     ")
    print("""The backyard overlooks the white sands of the beach.  A long covered porch wraps along the back of the 
house, filled chairs and hammocks that all faced the ocean.  Flowers fill the planters and large patch of grass fills 
the fenced-in area.

You have 2 choices:
     Go to the BEACH. 
     Enter the house through the BACK door""")

    #answer
    answer = input("What is your choice: ").lower().strip()

    #choices_path
    while answer != "back" and answer != "beach":
        answer = input("Try again.  What is your choice: ").lower().strip()
    if answer == "back":
        kitchen()
    elif answer == "beach":
        beach()


#main program
title()
input("Press Enter to continue...")
intro()
input("Press Enter to continue...")
instructions()
input("Press Enter to continue...")
sidewalk()