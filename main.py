#Selenium Locators: https://www.toolsqa.com/selenium-webdriver/selenium-locators/#:~:text=Selenium%20supports%208%20different%20types,fast%20methods%20of%20element%20recognition.
#You can simply add words to list in Monomon_solver, code handles the list just a OK.

import solver

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

button_SquabbleRoyale=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]")))    #Squaable Royale button
button_SquabbleRoyale.click()                  #Click Squabble Royale by XPath
print("Squabble Royale Selected.")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/input")))                #Wait until Join Game has spawned (i.e. Next page has loaded)
time.sleep(1)

button_FindGame      =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]")))    #Find Game button
button_FindGame.click() #Click Find Game
print("Find Game Initiated.")

input=WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[9]/input")))   #Wait until specific input region has spawned (i.e. Game Has Started) up to 5 minutes
time.sleep(1)
print("Game Started!")

try:
    end=0
    while end!=1 :
        
        #if(driver.find_element(By.CSS_SELECTOR, "div[role='presentation']").size()!=0): #If end screen has spawned this XPath is valid.
        #    end=1
        
        #print(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='presentation']")))
        #role=presentation ara ve sizedan değil 1 0 döndüren bir şeyden bak.

        possible_words=solver.possible_words    #Reset possible words to all possible words
        row=3                                           #Due to html organization
        result=""                                       #Random, in order to enter the loop.
        guess_counter=0

        while result != "ggggg" and guess_counter<6:
            
            #Guess
            guess = solver.bestWord(possible_words, solver.letterFreq(possible_words))
            input.send_keys(guess)        #to the search element send the string by typing it with keys
            input.send_keys(Keys.RETURN)    #Press enter at the search element
            #print(f'Guess= {guess.upper()}')
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
            #print(f'Result={result.upper()}')
            row+=1
            guess_counter+=1

            #if len(possible_words)<10:
            #    print(f"Possible Words Left: {possible_words}")
            


            #Update Possible Words Left
            possible_words = solver.word_remover(result, guess, possible_words)
            #print(possible_words)
            if len(possible_words) == 0:
                break
except:
    print("An Error Occured")
    time.sleep(30)

#Export Python as exe (Done)
#Seleniumu headless çalıştır. (Chrome GUIsini bootlamadan)
#End condition HP olmıcak, HP random 0 olabiliyo. Onun yerine end screeni detectlemeyi öğren. 1-0 çıktı veren bir şey lazım.
#Eksik kelimeler var bizim dictionaryde bence ondan. Şöyle yapıcaz o wordle list ile başla (Büyükten başlarsan o olmayan kelimeyi deneyip deadloopa giriyo)
    #Eksik kelime olması kazanmaya engel değil. Her bitince o çıkan kelime listesini al, list yap sonra: Monomon_solver.possible_words=list(set(Monomon_solver.possible_words+This_rounds_words))
    #cast to set, add, then unique result, cast back to list and update list.