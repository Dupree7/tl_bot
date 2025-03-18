import pyautogui
from pynput.keyboard import Controller, Key
import time
import cv2
import pytesseract
from PIL import ImageGrab
import re
import threading
import signal
import random
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\cioby\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Sword and shield

shieldStrike = "shieldStrike"
counterBarrier = "counterBarrier"
strategicRush = "strategicRush"
chainHook = "chainHook"
provokingRoar = "provokingRoar"
immortalPride = "immortalPride"
shieldThrow = "shieldThrow"
stalwartBastion = "stalwartBastion"
annihilatingSlash = "annihilatingSlash"
fierceClash = "fierceClash"
wittyResort = "wittyResort"
aShotAtVictory = "aShotAtVictory"

# Greatsword

valiantBrawl = "valiantBrawl"
precisionDash = "precisionDash"
stunningBlow = "stunningBlow"
deathBlow = "deathBlow"
davincisCourage = "davincisCourage"
guillotineBlade = "guillotineBlade"
gaiaCrash = "gaiaCrash"
devastatingTorando = "devastatingTorando"
willbreaker = "willbreaker"
ascendingSlash = "ascendingSlash"
devastatingSmash = "devastatingSmash"
bloodDevotion = "bloodDevotion"

####

cooldowns = {
    shieldStrike: 5.2,
    counterBarrier: 18.1,
    strategicRush: 15.5,
    chainHook: 18.1,
    provokingRoar: 25.9,
    immortalPride: 78,
    shieldThrow: 28.5,
    stalwartBastion: 65,
    annihilatingSlash: 20.7,
    fierceClash: 19,
    wittyResort: 18.1,
    aShotAtVictory: 20.7,

    valiantBrawl: 7.8,
    precisionDash: 9.3,
    stunningBlow: 20.7,
    deathBlow: 8.8,
    davincisCourage: 38.9,
    guillotineBlade: 17.6,
    gaiaCrash: 20.7,
    devastatingTorando: 13,
    willbreaker: 20.7,
    ascendingSlash: 20.7,
    devastatingSmash: 31.1,
    bloodDevotion: 78,
}


skillSet = {
    "1": shieldStrike,
    "2": counterBarrier,
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "0": "",
    "-": "",
    "=": "",
}

####


clicking = True


sleepTable = {
    "1": 0.1,
    "2": 1,
    "3": 0.3,
    "4": 0.3,
    "5": 0.3,
    "6": 0.3,
    "7": 0.3,
    "8": 0.5,
    "9": 7,
    "0": 0.5,
    "-": 0.5,
    "=": 0.5,
}

firstTargetX = 31
firstTargetXX = 238
firstTargetY = 515
fristTargetYY = 548

spellsFirstX = 598
spellsSecondX = 1002
spellsXLength = 27  
spellsDistance = 58

spellsY = 1008
spellsYy = 1029

keyboard = Controller()

def human_like_clicker():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(random.uniform(0.5, 1.2))

def clickFirstTarget():
    x, y = random.randint(firstTargetX, firstTargetXX), random.randint(firstTargetY, fristTargetYY)
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()


def human_like_hold(key, min_hold=0.5, max_hold=1.1):
    hold_time = random.uniform(min_hold, max_hold)

    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)

def human_like_multiple_presses(key):
    choice = random.choice(["1", "1", "1", "1", "1", "1", "2", "2", "2", "3"])

    for _ in range(int(choice)):
        human_like_press(key)
        time.sleep(random.uniform(0.05, 0.16))

    print(f"Pressed '{key}' {choice} times")

def human_like_press(key):
    press_time = random.uniform(0.05, 0.2)  # Human reaction time (50-200ms)

    keyboard.press(key)
    time.sleep(press_time)
    keyboard.release(key)

    print(f"Pressed '{key}'")

def useSpell(key):
    if key == "10":
        key = "0"
    elif key == "11":
        key = "-"
    elif key == "12":
        key = "="

    if key == "1":
        human_like_hold(key)
    else:
        human_like_press(key)
    time.sleep(sleepTable[key])

def ocrSpells():
    spells = {}

    for i in range(6):
        xStart = spellsFirstX + i * spellsDistance
        region = (xStart, spellsY, xStart + spellsXLength, spellsYy)
        screenshot = ImageGrab.grab(bbox=region)
        imageName = f"screenshot{i}.png"
        screenshot.save(imageName)
        gray = cv2.cvtColor(cv2.imread(imageName), cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        text = re.sub(r'[^a-zA-Z0-9]', '', text)
        if i == 6 and text == "ind":
            text = ""
        if len(text) > 1:
            spells[f"{i + 1}"] = False
        else:
            spells[f"{i + 1}"] = True
        print(f"index: {i + 1} - text: {text} - len: {len(text)}") 

    for i in range(6):
        xStart = spellsSecondX + i * spellsDistance
        region = (xStart, spellsY, xStart + spellsXLength, spellsYy)
        screenshot = ImageGrab.grab(bbox=region)
        imageName = f"screenshot{i + 6}.png"
        screenshot.save(imageName)
        gray = cv2.cvtColor(cv2.imread(imageName), cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        text = re.sub(r'[^a-zA-Z0-9]', '', text)
        # if i == 1 and text == "TAS":
        #     text = ""
        if len(text) > 1:
            spells[f"{i + 6 + 1}"] = False
        else:
            spells[f"{i + 6 + 1}"] = True
        print(f"index: {i + 6 + 1} - text: {text} - len: {len(text)}") 

    return spells


def signal_handler(sig, frame):
    """Handles Ctrl+C or terminal close events to stop the script gracefully."""
    global clicking
    print("\nGracefully exiting...")
    clicking = False  # Stop the clicking loop
    time.sleep(0.5)  # Small delay to ensure thread exits
    sys.exit(0)  # Exit the script


def defensiveLogic(spells, left, right):
    choices = []
    for i in range(left, right + 1):
        index = str(i)
        if spells[index] == True:
            choices.append(index)

    if len(choices) > 0:
        choice = random.choice(choices)
        useSpell(choice)
        return choice
    else:
        return "-1"

def actionLogic(spells, left, right):
    choices = []
    for i in range(left, right + 1):
        index = str(i)
        if spells[index] == True:
            choices.append(index)

    if len(choices) > 0:
        choice = random.choice(choices)
        useSpell(choice)
        return choice
    else:
        return "0"

def main():
    time.sleep(2)

    # Register signal handler (Handles Ctrl+C and CMD close)
    signal.signal(signal.SIGINT, signal_handler)  # Handles Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handles CMD close

    clickFirstTarget()

    click_thread = threading.Thread(target=human_like_clicker, daemon=True)
    click_thread.start()

    while True:
        spellsStatus = ocrSpells()
        print(spellsStatus)
        
        defSpell = defensiveLogic(spellsStatus, 8, 12)
        spellsStatus[defSpell] = False

        durationTime = random.uniform(0.5, 2.3)
        startTime = time.time()

        while time.time() - startTime < durationTime:
            actSpell = actionLogic(spellsStatus, 1, 6)
            if actSpell == "-1":
                break
            spellsStatus[actSpell] = False
            time.sleep(0.05)

if __name__ == "__main__":
    main()



