print(r"""
   /$ /$   /$$      /$$ /$$$$$$$$ /$$$$$$$        /$$   /$$ /$$$$$$ /$$     /$$ /$$$$$$  /$$   /$$
  |_/|_/  | $$$    /$$$| $$_____/| $$__  $$      | $$  /$$/|_  $$_/|  $$   /$$//$$__  $$| $$  /$$/
  /$$$$$$ | $$$$  /$$$$| $$      | $$  \ $$      | $$ /$$/   | $$   \  $$ /$$/| $$  \ $$| $$ /$$/ 
 /$$__  $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/      | $$$$$/    | $$    \  $$$$/ | $$$$$$$$| $$$$$/  
| $$  \ $$| $$  $$$| $$| $$__/   | $$__  $$      | $$  $$    | $$     \  $$/  | $$__  $$| $$  $$  
| $$  | $$| $$\  $ | $$| $$      | $$  \ $$      | $$\  $$   | $$      | $$   | $$  | $$| $$\  $$ 
|  $$$$$$/| $$ \/  | $$| $$$$$$$$| $$  | $$      | $$ \  $$ /$$$$$$    | $$   | $$  | $$| $$ \  $$
 \______/ |__/     |__/|________/|__/  |__/      |__/  \__/|______/    |__/   |__/  |__/|__/  \__/
                                                                                                  
                                                                                                  
                                                                                                  
 """)
print("\n***************************************************************** *")
print("\n* Copyright of Ömer KIYAK, 2023                                 * *")
print("\n* https://www.instagram.com/omer_x_kiyak/                       * *")
print("\n*  https://github.com/omer-X-kiyak/                             * *")
print("\n***************************************************************** *\n \n")

#Kütüphaneler
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Driver yolu giris
browser = webdriver.Edge('msedgedriver.exe')

#Site giris
browser.get("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")
time.sleep(2)

liste = browser.find_elements(By.ID, 'video-title')

with open('sonuç.txt', 'w', encoding='utf-8') as f:
    for elem in liste:
        print(elem.text)
        f.write(elem.text + '\n\n')
