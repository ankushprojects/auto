import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_update():
    extension_1_path = "mughex1.zip"  
    extension_2_path = "mughex2.zip" 
    extension_3_path = "royal1.zip"  
    extension_4_path = "Royal2.zip"
    extension_5_path = "azadseo1.zip"
    extension_6_path = "azadseo2.zip"

    driver = None
    try:
        # Set Chrome binary to the exact path
        chrome_binary = "/opt/google/chrome/google-chrome"
        
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--remote-debugging-port=9222')
        options.binary_location = chrome_binary
        
        print(f"Using Chrome binary at: {chrome_binary}")
        
        # Add extensions
        for ext in [extension_1_path, extension_2_path, extension_3_path, 
                   extension_4_path, extension_5_path, extension_6_path]:
            if os.path.exists(ext):
                options.add_extension(ext)
            else:
                print(f"Warning: Extension {ext} not found")

        # Create driver with explicit service
        service = Service('/usr/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
        print("Chrome driver created successfully")

        # Create cookies_save directory if it doesn't exist
        os.makedirs("cookies_save", exist_ok=True)

        # Rest of your original code remains the same...
        tools_mughal = {"semrush":"https://session.mughalseotools.com/semrushfull/semrushfull.php",
                 "grammarly":"https://session.mughalseotools.com/grammarly/grammarly.php",
                 "moz":"https://session.mughalseotools.com/moz/moz.php",
                 "ubersuggest":"https://session.mughalseotools.com/ubersuggest/ubersuggest.php"}
        
        tools_royal = {"semrush2":"https://sem1.royalseotools.com/projects",
                 "semrush3":"https://sem2.royalseotools.com/",
                 "seoptimer":"https://session.royalseotools.com/seoptimer/seoptimer.php",
                 "spyfu":"https://session.royalseotools.com/spyfu%20ex/spyfu%20ex.php",
                 "scribd":"https://session.royalseotools.com/Scribd/Scribd.php",
                 "storyblocks":"https://session.royalseotools.com/storyblock%20ex/storyblock%20ex.php",
                 "vectezzy":"https://session.royalseotools.com/vecteezy%20Ext/vecteezy%20Ext.php",
                 "skillshare":"https://session.royalseotools.com/skillshare%20ex/skillshare%20ex.php",
                 "wordtune":"https://session.royalseotools.com/wordtune/wordtune.php",
                 "creaitor":"https://session.royalseotools.com/creatorai/creatorai.php",
                 "linkdinlearning":"https://session.royalseotools.com/Linkedin%20Learning/Linkedin%20Learning.php",
                 "closerscopy":"https://session.royalseotools.com/closerscopy/closerscopy.php"}

        tools_Azad = {"semrush4":"https://smr.azadseo.com/analytics/overview/",
                 "semrush5":"https://smr2.azadseo.com/analytics/overview/?searchType=domain",
                 "grammer2":"https://members.azadseo.com/accessTool?tool=grammarly", 
                 "wordai":"https://wai.azadseo.com/home",
                 "indexification":"https://ixn.azadseo.com/members/index.php",
                 "envato":"https://ee2.azadseo.com/all-items",
                 "Moz2":"https://members.azadseo.com/accessTool/?tool=moz3"}

        # ---------------------------- MUGHAL COPY COOKIES ------------------------------------------
        url = "https://app.mughalseotools.com/login" 
        driver.get(url)
        time.sleep(3)
        username = "rockanks"  
        password = "rockanks12"  

        username_field = driver.find_element(By.ID, "amember-login") 
        password_field = driver.find_element(By.ID, "amember-pass")  

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  

        time.sleep(5)

            for key, value in tools_dict.items():
                try:
                    driver.get(value)
                    time.sleep(5)

                    # Switch to the correct window
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        if value in driver.current_url:
                            break

                    # Get and save cookies
                    cookies = driver.get_cookies()
                    enriched_cookies = [
                        {
                            **cookie,
                            "url": f"https://{cookie['domain'].lstrip('.')}"
                        }
                        for cookie in cookies
                    ]

                    with open(f"cookies_save/{key}.json", "w") as file:
                        json.dump(enriched_cookies, file, indent=4)
                    print(f"{key} Cookies have been saved")
                
                except Exception as e:
                    print(f"Error processing {key}: {str(e)}")

        # Process Mughal SEO
        login_and_get_cookies(
            "https://app.mughalseotools.com/login",
            "rockanks",
            "rockanks12",
            tools_mughal
        )

        # Process Royal SEO
        login_and_get_cookies(
            "https://app.royalseotools.com/member",
            "rockanks",
            "rockanks",
            tools_royal
        )

        # Process Azad SEO
        login_and_get_cookies(
            "https://members.azadseo.com/login",
            "rockanks",
            "rockanks12",
            tools_Azad
        )

        # ---------------------------- UPDATE COOKIES ------------------------------------------
        url = "https://cloud.rainyclouds.in/member"
        driver.get(url)

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "amember-login"))
        )
        password_field = driver.find_element(By.ID, "amember-pass")

        username_field.send_keys("accupdate")
        password_field.send_keys("AccUp@11054")
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        for file_name in os.listdir("cookies_save"):
            try:
                i = os.path.splitext(file_name)[0]
                url_sem = f"https://portal.rainyclouds.in/{i}.php"
                driver.get(url_sem)

                cookies_file = f"cookies_save/{i}.json"
                with open(cookies_file, "r") as file:
                    cookies = json.load(file)

                cookies_str = json.dumps(cookies, indent=4)

                text_area = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "inputSuccess"))
                )

                driver.execute_script("arguments[0].value = arguments[1];", text_area, cookies_str)

                button = driver.find_element(By.ID, "SubBtn")
                button.click()

                if os.path.exists(cookies_file):
                    os.remove(cookies_file)
                    print(f"{cookies_file} has been deleted.")

                print(f"Cookies updated for {i}")
                time.sleep(2)

            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error closing driver: {str(e)}")

