#Selenium Locators: https://www.toolsqa.com/selenium-webdriver/selenium-locators/#:~:text=Selenium%20supports%208%20different%20types,fast%20methods%20of%20element%20recognition.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys     #For pressing keys on the keyboard
from selenium.webdriver.common.by import By         #For explicit wait, allowss for waits until the main tag becomes present
import time                                         #For delays
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"       
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])   #Options to turn off stupid USB, Bluetooth errors.
driver = webdriver.Chrome(service=Service(PATH),options=op)         #Engage browser with its driver using your options.


driver.get("https://squabble.me/")      #Access the Site First
print("Site Accessed.")

button_SquabbleRoyale=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]")))   #Squaable Royale button                                 #The button is found very fast but takes time to be clickable, wait for it.
button_SquabbleRoyale.click()                  #Click Squabble Royale by XPath
print("Squabble Royale Selected")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/input")))    #Wait until Join Game has spawned (i.e. Next page has loaded)
time.sleep(1)

button_FindGame      =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]")))   #Find Game button
button_FindGame.click() #Click Find Game
print("Find Game Initiated")

input=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[9]/input")))    #Wait until specific input has spawned (i.e. Game Has Started) up to 2 minutes
time.sleep(1)
print("Game Started!")


input.send_keys("adept")        #to the search element send the string "test" by typing it with keys
input.send_keys(Keys.RETURN)    #Press enter at the search element
time.sleep(1)

input.send_keys("clamp")        #to the search element send the string "test" by typing it with keys
input.send_keys(Keys.RETURN)    #Press enter at the search element
time.sleep(1)

input.send_keys("plaid")        #to the search element send the string "test" by typing it with keys
input.send_keys(Keys.RETURN)    #Press enter at the search element

#Now the word logic!
#What to send
#How to get feedback
#How to translate feedback to next guess
#Export Python as exe







