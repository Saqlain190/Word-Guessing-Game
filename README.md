**Guessing Game: Animals and Vegetables**
This is a simple Python guessing game where users can select a category (animals or vegetables) and attempt to guess the correct name based on a hint provided by the system.

**Features:**
The game has two categories: Animals and Vegetables.
Users are provided with a hint for the selected category.
Users are allowed a maximum of 4 attempts to guess the correct answer.
The game checks if the user's guess matches the correct answer and provides feedback.
Game Flow:
User Input:

The user selects a category by entering 1 for Animals or 2 for Vegetables.
Hint:

After selecting the category, a hint will be shown to help the user guess the name of an animal or vegetable.
**Guessing:**

The user will input their guess for the name of the selected item. They have up to 4 attempts to get it correct.
If the guess is correct, the user wins, and the game ends.
If the guess is incorrect, the system will prompt them to try again.
After 4 incorrect attempts, the game will display a "Game Loss" message.
How to Run:
Clone the repository or download the script file.
Open the terminal or command prompt.
Navigate to the folder containing the Python script.
**Run the script by typing:**
bash
Copy code
python guessing_game.py
Follow the on-screen instructions to select a category and make guesses.
**Code Explanation:**
guessing(list_name) function:

The function takes a dictionary (animals or vegetables) and randomly selects an item.
The user is given a hint, and they have up to 4 chances to guess the correct name.
animals() function:

Contains a dictionary of animal names with associated hints.
Calls the guessing() function to start the game for animals.
vegetables() function:

Contains a dictionary of vegetable names with associated hints.
Calls the guessing() function to start the game for vegetables.
Example Output:
bash
Copy code
Select the Category you want to guess 
1.  Animals
2.  Vegetables
Enter your choice (1/2): 1
Your hint is: A loyal pet.
Enter the Name: dog
Hurray Correct Guess: Won
