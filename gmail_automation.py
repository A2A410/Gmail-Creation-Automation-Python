# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from unidecode import unidecode
# My additions
import subprocess
import os
import random
import string

# Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# WebDriver service
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)

french_first_names = [
    "Aldous", "Basilio", "Cassian", "Dacian", "Elidor", "Faelan", "Garrick", "Hadriel", "Icarus", "Jorvik",
"Kaius", "Lorien", "Merrick", "Nestor", "Orpheus", "Peregrine", "Quillon", "Roderic", "Sylvan", "Torian",
"Ulysses", "Vireo", "Wystan", "Xerxes", "Ywain", "Zephiran", "Alaric", "Bael", "Cyran", "Draven",
"Evander", "Fenwick", "Gaius", "Halcyon", "Isidore", "Jovian", "Kaelith", "Lucan", "Magnus", "Nerian",
"Octavian", "Phineas", "Quintus", "Rael", "Sirius", "Thorne", "Ulric", "Vasilis", "Wolfram", "Zorion", "Aisling", "Bellatrix", "Calista", "Damaris", "Elowen", "Fiora", "Gwyneira", "Hesper", "Isolde", "Jocasta",
"Keturah", "Lyra", "Melisande", "Nerissa", "Ondine", "Phaedra", "Queniva", "Rhiannon", "Selene", "Tirzah",
"Undine", "Vespera", "Wynn", "Xanthe", "Ysabeau", "Zephyrine", "Althea", "Briseis", "Cassiopeia", "Delphine",
"Evadne", "Freesia", "Galadriel", "Helisent", "Ione", "Jessamine", "Kallista", "Lirael", "Maelis", "Nyx",
"Opheliane", "Persephone", "Queralt", "Rosmerta", "Sybil", "Thalassa", "Urielle", "Verena", "Wrenna", "Zuleika" 
]

french_last_names = [
    "Abermont", "Beaumont", "Carrington", "Davenport", "Everhart", "Falkenrath", "Godfrey", "Haverford", "Ingram", "Jourdain",
"Kensington", "Loxley", "Montclair", "Norwood", "Ormsby", "Pembroke", "Quinlan", "Ravensdale", "Sterling", "Thornecroft",
"Ullswater", "Valmont", "Wetherby", "Xavier", "Yorke", "Zephyrion", "Alderridge", "Blackwood", "Chamberlain", "Darnell",
"Ellsworth", "Fitzroy", "Granville", "Holloway", "Islington", "Juliard", "Kingswell", "Lutherford", "Marchand", "Northcott",
"Oberon", "Pendragon", "Quillbourne", "Rosendale", "Strathmore", "Tremontaine", "Vanderlyn", "Westerveld", "Yardleigh", "Zeraphine", "Astoria", "Beauchamp", "Clairmont", "Devereux", "Ellington", "Fitzalan", "Gisborne", "Hawthorne", "Iverson", "Juliette",
"Kensington", "Lavoisier", "Montfort", "Nightingale", "Opaline", "Parlowe", "Quenelle", "Rousseau", "Sinclaire", "Trémaux",
"Uverelle", "Valliere", "Whitmore", "Xanthippe", "Yverdon", "Zephyrine", "Aurelian", "Bellerose", "Châtelaine", "D’Orsay",
"Esclarmonde", "Fontenelle", "Gascoyne", "Halewyn", "Isabeaux", "Jardine", "Kallistrate", "Lorentzia", "Miremont", "Nocturne",
"Ondine", "Prévost", "Quispe", "Rosamonde", "Seraphion", "Thessaly", "Ulverston", "Viremont", "Westerdale", "Zaffre" 
]

# Randomly select a first name and a last name
your_first_name = random.choice(french_first_names)
your_last_name = random.choice(french_last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()


your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"


your_birthday = "02 3 1989" #dd m yyyy exp : 24 11 2003
your_gender = "3" # 1:F 2:M 3:Not say 4:Custom
your_password = "n...16839jylwbk"

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in name fields
        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(your_first_name)
        last_name.clear()
        last_name.send_keys(your_last_name)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        print("full name fields filled successfully")

        # Wait for birthday fields to be visible
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        # Fill in birthday
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        print("Birthday filled successfully")

        
       # Create custom email
        time.sleep(2)
        if driver.find_elements(By.CLASS_NAME, "uxXgMe"):
            create_own_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[jsname='CeL6Qc']")))
            create_own_option.click()
        
        wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(your_username)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()
        


        # Enter and confirm password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        # Locate the parent div element with the ID "confirm-passwd"
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
         #Find the input field inside the parent div
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()


        # Check if the phone number is needed
        time.sleep(2)
        if driver.find_elements(By.ID, "phoneNumberId"):
            wait.until(EC.element_to_be_clickable((By.ID, "phoneNumberId")))
            phonenumber_field = driver.find_element(By.ID, "phoneNumberId")
            phonenumber_field.clear()
            phonenumber_field.send_keys("+2126"+str(random.randint(10000000,99999999)))
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
            next_button.click()
            time.sleep(2)
            ok = ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
            while not ok:
                try:
                    phonenumber_field.clear()
                    phonenumber_field.send_keys("+2126"+str(random.randint(10000000,99999999)))
                    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
                    next_button.click()
                    time.sleep(2)
                    ok = ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
                    ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
                except:
                    pass
        else:
            # Skip phone number and recovery email steps
            skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            for button in skip_buttons:
                button.click()

        # Agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()


        print(f"Your Gmail:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")

    except Exception as e:
        print("Failed, Sorry")
        print(e)
    finally:
        driver.quit()

# Execute the function to fill out the form
fill_form(driver)

# My Additions 2

def random_suffix(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

log_file = "accounts.txt"
if os.path.exists(log_file):
    log_file = f"accounts_{random_suffix()}.txt"  

with open(log_file, "w") as f:  
    process = subprocess.run(["python", "gmail_automation.py"], stdout=f, stderr=f, text=True)

print(f"Output logged to: {log_file}")
