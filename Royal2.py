import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def perform_update():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox') 
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument('--remote-debugging-port=9222')  

        driver = webdriver.Chrome(options=options)

    #---------------------------- COPY COOKIES ------------------------------------------

        url = "https://app.royalseotools.com/login"  
        driver.get(url)
        time.sleep(3)
        
        username = "rockanks" 
        password = "rockanks" 

        username_field = driver.find_element(By.ID, "amember-login")  
        password_field = driver.find_element(By.ID, "amember-pass")  

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  

        time.sleep(5)

        url_sem = "https://sem1.royalseotools.com/projects"  
        driver.get(url_sem)

        cookies = driver.get_cookies()

        enriched_cookies = [
            {
                **cookie,
                "url": f"https://{cookie['domain'].lstrip('.')}"
            }
            for cookie in cookies
        ]

        with open("cookies1.json", "w") as file:
            json.dump(enriched_cookies, file, indent=4)
        print("Cookies have been saved to cookies.json. \n")


    #---------------------------- UPDATE COOKIES ------------------------------------------

        url = "https://cloud.rainyclouds.in/member"  
        driver.get(url)

        time.sleep(3)

        username = "accupdate"  
        password = "AccUp@11054"  

        username_field = driver.find_element(By.ID, "amember-login") 
        password_field = driver.find_element(By.ID, "amember-pass")  
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  

        time.sleep(5)

        url_sem = "https://portal.rainyclouds.in/semrush.php" 
        driver.get(url_sem)

        cookies_file = "cookies1.json"
        with open(cookies_file, "r") as file:
            cookies = json.load(file)

        if os.path.exists(cookies_file):
            os.remove(cookies_file)
            print(f"{cookies_file} has been deleted.")

        cookies_str = json.dumps(cookies, indent=4)

        text_area = driver.find_element(By.ID, "inputSuccess")

        time.sleep(2)

        driver.execute_script("arguments[0].value = arguments[1];", text_area, cookies_str)

        button = driver.find_element(By.ID, "SubBtn")
        button.click()

        print("Text has been pasted and the button has been clicked.")

    finally:
        driver.quit()

