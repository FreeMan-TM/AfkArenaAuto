from pyautogui import *
import pyautogui
import time
import keyboard

# Clicking button function
def click_button(image_path, confidence=0.6, click_coordinates=None):
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            if click_coordinates:
                x, y = click_coordinates
                pyautogui.click(x, y)
                print(f"Clicked at coordinates {x}, {y} for {image_path}")
            else:
                cords = pyautogui.center(location)
                pyautogui.click(cords.x, cords.y)  # Use click with coordinates directly
                print(f"Clicked {image_path}")
            return True  # Button clicked successfully
        return False  # Button not found
    except pyautogui.ImageNotFoundException:
        return False  # Button not found

# Set the sentinel control key and FormationSet bool
sentinel_key = '1' # Hold 1 to exit while loop
FormationSet = False

# Function to get formation coordinates based on choice
def get_formation_coordinates(choice):
    formation_coordinates = {
        "1": (1103, 341),
        "2": (1103, 437),
        "3": (1103, 527),
        "4": (1103, 615),
        "5": (1103, 709),
    }
    return formation_coordinates.get(choice, (1103, 341))

# Continuously check for the various buttons until the sentinel key is pressed
while not keyboard.is_pressed(sentinel_key):
    if click_button('Begin_Boss_Button.png', confidence=0.6):
        FormationSet = True
        time.sleep(2)
        if click_button('Boss_Begin_Button.png'):
            time.sleep(2)
    elif FormationSet == True and click_button('Formations_Button.png'):
        time.sleep(2)
        pyautogui.click(1087,875) #Popular Option
        time.sleep(2)
        FormationChoice = "3"  # Hard-coded input, you can replace it with your logic
        FormationCords = get_formation_coordinates(FormationChoice)
        pyautogui.click(FormationCords[0], FormationCords[1])  # Stat Icon
        time.sleep(2)
        pyautogui.click(1035,967) #Use Button
        time.sleep(2)
        pyautogui.click(1022,673) #Confirm Formation
        time.sleep(2)
        FormationSet = False
    elif click_button('Bundle_Appeared.png', confidence=0.7, click_coordinates=(940, 860)):
        time.sleep(2)
        click_button('arrow.png', confidence=0.9)
        time.sleep(2)
        click_button('Next_Chapter_Button.png', confidence=0.9)
        time.sleep(2)
        click_button('Return_Button.png')
        time.sleep(2)
    elif click_button('Next_Stage_Button.png'):
        FormationSet = True
        time.sleep(2)
    elif click_button('Battle_Button.png'):
        time.sleep(2)
    elif click_button('Try_Again_Button.png'):
        time.sleep(2)
    else:
        time.sleep(1)
        #print("In Battle")
