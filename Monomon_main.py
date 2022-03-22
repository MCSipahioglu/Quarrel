#Selenium Locators: https://www.toolsqa.com/selenium-webdriver/selenium-locators/#:~:text=Selenium%20supports%208%20different%20types,fast%20methods%20of%20element%20recognition.
#importu görmemesi iki Python yüklü olduğu ve yanlışının vscode da interpreter olarak seçili olduğu içinmiş.

import Monomon_solver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys     #For pressing keys on the keyboard
from selenium.webdriver.common.by import By         #For explicit wait, allowss for waits until the main tag becomes present
import time                                         #For delays
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])   #Options to turn off stupid USB, Bluetooth errors.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)         #Engage browser with its driver (automatic detection via webdriver_manager) using your options.


driver.get("https://squabble.me/")      #Access the Site First
print("Site Accessed.")

button_SquabbleRoyale=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]")))   #Squaable Royale button                                 #The button is found very fast but takes time to be clickable, wait for it.
button_SquabbleRoyale.click()                  #Click Squabble Royale by XPath
print("Squabble Royale Selected.")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/input")))    #Wait until Join Game has spawned (i.e. Next page has loaded)
time.sleep(1)

button_FindGame      =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]")))   #Find Game button
button_FindGame.click() #Click Find Game
print("Find Game Initiated.")

input=WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[9]/input")))    #Wait until specific input region has spawned (i.e. Game Has Started) up to 5 minutes
time.sleep(1)
print("Game Started!")


#Burdan alcan her tur için

possible_words=Monomon_solver.possible_words



guess= Monomon_solver.bestWord(possible_words, Monomon_solver.letterFreq(possible_words))
input.send_keys(guess)        #to the search element send the string by typing it with keys
input.send_keys(Keys.RETURN)    #Press enter at the search element
print(f'Guess={guess.upper()}')
time.sleep(1)   #Allow the result to be updated.

row=3
result=""
for i in range (1,6):
    letter_element=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[1]/div[{row}]/div[{i}]/div[2]")
    letter_class=letter_element.get_attribute("class")
    if(letter_class=="MuiBox-root css-18037ny"):
        result+="w"
    elif(letter_class=="MuiBox-root css-tim17a"):
        result+="y"
    else:
        result+="g"
print(f'Result={result.upper()}')
row+=1


while result != "ggggg":
    possible_words = Monomon_solver.word_remover(result, guess, possible_words)
    #print(possible_words)
    if len(possible_words) == 0:
        break

    #Guess
    guess = Monomon_solver.bestWord(possible_words, Monomon_solver.letterFreq(possible_words))
    input.send_keys(guess)        #to the search element send the string by typing it with keys
    input.send_keys(Keys.RETURN)    #Press enter at the search element
    print(f'Guess={guess.upper()}')
    time.sleep(1)   #Allow the result to be updated.

    #Result
    result=""
    for i in range (1,6):
        letter_element=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[1]/div[{row}]/div[{i}]/div[2]")
        letter_class=letter_element.get_attribute("class")
        if(letter_class=="MuiBox-root css-18037ny"):
            result+="w"
        elif(letter_class=="MuiBox-root css-tim17a"):
            result+="y"
        else:
            result+="g"
    print(f'Result={result.upper()}')
    row+=1

time.sleep(1000)



#Do for second loop as well.
#Counter da koyucaz 6 yanlıştan sonra canın varsa sonrakine geçiyor.
#Export Python as exe
#Auto exitliyor bitince, o olmamalı. Exit you win olunca olmalı 10 saniye filan da delay verip. Bitince spawnlanan: /html/body/div[2]. Bu spawnlanmadığı sürece oyna.

#parent : <div class="letter MuiBox-root css-ohwg9z"><div class="MuiBox-root css-mq7g1t"></div><div class="MuiBox-root css-18037ny" style="position: absolute; inset: 0px;">a</div></div>

