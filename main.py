from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import Tk
import time
import random
import string

login = "lessie32@10minut.xyz"  # lessie32@10minut.xyz  schuyler62@10minut.xyz
haslo = "?^2H,3$]-bo]a)_vhT2xYj,*%wqf+A"

def find_xpath(xpath):  # definiujemy se funcjkę , gdzie podajemy xpatha w "" i nam znajduje
    try:
        global browse
        try:  # po tym czasie rezygnuje
            element = WebDriverWait(browse, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        finally:  # zwraca nam element przeglądarkowy, dopisujemy kropkę i tyle
            return browse.find_element(By.XPATH, xpath)  # takie coś: find_xpath("xpath_elementu") .click()
    except:
        print('wywalilo się')

global browse
browse = webdriver.Firefox()  # przeglądarka, wiadomo

def my_setup():
    browse.get("https://seekfindinput.sfi.pl/input/")
    # handle1 = browse.current_window_handle  # handle pierwszej strony ()
    time.sleep(random.randint(2, 5))
    find_xpath('//*[@id="username"]').send_keys(login) #email
    find_xpath('//*[@id="password"]').send_keys(haslo)
    time.sleep(random.randint(2, 5))
    find_xpath('//*[@id="rememberMe"]').click()
    time.sleep(random.randint(2, 5))
    find_xpath('//*[@id="kc-login"]').click()

##########################################################################
#                               PROGRAM                                  #
##########################################################################

my_setup();

alphabet = string.ascii_letters + string.digits  # alfabet łaciński i cyfry
length = 13  # długość kombinacji

for i in range(0, 50):
    #combination = "6c2a1fcfc19b"
    #print(combination)

    combination = ''.join(random.choice(alphabet) for _ in range(length))
    find_xpath('//*[@id="id_code"]').send_keys(combination)
    time.sleep(random.randint(2, 5))
    find_xpath('/html/body/main/div/div/div[2]/section/form/button').click()


    komunikat = find_xpath('/html/body/main/div/div/div[2]/section/div').text

    print(komunikat)

    if komunikat.startswith("Dostępne nowe zasoby"):
        print("udalo sie")
        plik = open("kody_dobre.txt", 'a')
        plik.write(combination + '\n')
        plik.close()
        time.sleep(20)
    else:
        print("no niesety się nie udało")
        time.sleep(random.randint(2, 10))

