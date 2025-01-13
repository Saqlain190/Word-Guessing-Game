import random

animals_name = {}
vegetables_name = {}
user_input = ""
system_choice = ""

def animals():
    global animals_name , user_input, system_choice
    animals_name = {
    "Dog": "A loyal pet.",
    "Cat": "A playful pet that purrs.",
    "Cow": "Gives milk on farms.",
    "Horse": "Used for riding.",
    "Sheep": "Gives us wool.",
    "Goat": "Loves to climb and gives milk.",
    "Fish": "Lives in water.",
    "Mouse": "Small Size and Naughty Acts",
    "Rabbit": "Hops and eats carrots.",
    "Duck": "Quacks and swims."}

    print(animals_name)

    
    system_choice  = random.choice(list(animals_name.keys()))
    hint = animals_name[system_choice]
    print(f"Your hint is :  {hint}")
    print(system_choice)
    count = 0
    while count < 4:
          count += 1
          user_input = input(" Enter the Animal Name ") 
          if user_input.lower()== system_choice.lower():
              print("Hurray Correct Guess : Won  ")
              break
             
          elif user_input.lower() != system_choice.lower():
              print(" Incorrect Guess Try Again")


    
        





    
    


   
def vegetables():
    global vegetables_name , user_input
    vegetables_name = {
    "Carrot": "Orange and crunchy.",
    "Potato": "Used to make fries.",
    "Tomato": "Red and juicy, often in salads.",
    "Onion": "Makes you cry when cut.",
    "Garlic": "Used to add flavor, has cloves.",
    "Cucumber": "Green and refreshing.",
    "Broccoli": "Looks like a small tree.",
    "Spinach": "Leafy and rich in iron.",
    "Peas": "Small and green in pods.",
    "Capsicum": "Bell-shaped, comes in many colors."}
    print(vegetables_name)
    user_input = input(" Enter the Word ")
 

user_choice = int(input("""Select the Category you want to guess 
                        1.  Animals
                        2.  Vegetables    """))


if user_choice == 1:
  animals()
  
  if user_input.lower() != system_choice.lower():
      print("Game Loss")
elif user_choice == 2:
  vegetables()


