import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_update():
    try:
        # Chrome options configuration
        options = webdriver.ChromeOptions()
        
        # Basic Chrome settings
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        
        # Extension handling
        extension_paths = [
            '/app/mughex1.zip',
            '/app/mughex2.zip',
            '/app/royal1.zip',
            '/app/Royal2.zip',
            '/app/azadseo1.zip',
            '/app/azadseo2.zip'
        ]
        
        # Properly handle extension loading
        options.add_argument('--disable-extensions-except=' + ','.join(extension_paths))
        options.add_argument('--load-extension=' + ','.join(extension_paths))
        
        # Additional settings for stability
        options.add_argument('--disable-web-security')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        
        # Initialize webdriver with extended timeout
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        
        # Create cookies directory if it doesn't exist
        os.makedirs('cookies_save', exist_ok=True)

        # Your existing tool dictionaries
        tools_mughal = {
            "semrush": "https://session.mughalseotools.com/semrushfull/semrushfull.php",
            "grammarly": "https://session.mughalseotools.com/grammarly/grammarly.php",
            "moz": "https://session.mughalseotools.com/moz/moz.php",
            "ubersuggest": "https://session.mughalseotools.com/ubersuggest/ubersuggest.php"
        }
        
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
                 "closerscopy":"https://session.royalseotools.com/closerscopy/closerscopy.php",
                
                }

        tools_Azad = {"semrush4":"https://smr.azadseo.com/analytics/overview/",
                 "semrush5":"https://smr2.azadseo.com/analytics/overview/?searchType=domain",
                 "grammer2":"https://members.azadseo.com/accessTool?tool=grammarly", 
                 "wordai":"https://wai.azadseo.com/home",
                 "indexification":"https://ixn.azadseo.com/members/index.php",
                 "envato":"https://ee2.azadseo.com/all-items",
                 "Moz2":"https://members.azadseo.com/accessTool/?tool=moz3"
                }
        

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox') 
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument('--remote-debugging-port=9222')  
        options.add_extension(extension_1_path)
        options.add_extension(extension_2_path)
        options.add_extension(extension_3_path)
        options.add_extension(extension_4_path)
        options.add_extension(extension_5_path)
        options.add_extension(extension_6_path)
        # options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=options)

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

        for key, value in tools_mughal.items():
            # url_sem = "https://sem.mughalseotools.com/projects"  
            driver.get(value)

            # button = driver.find_element(By.CLASS_NAME, 'button1')

            # button.click()
            time.sleep(5)

            window_handles = driver.window_handles
            for handle in window_handles:
                driver.switch_to.window(handle)
                if value in driver.current_url:
                    break

            # Get cookies and add the `url` field
            cookies = driver.get_cookies()

            enriched_cookies = [
                {
                    **cookie,
                    "url": f"https://{cookie['domain'].lstrip('.')}"
                }
                for cookie in cookies
            ]

            # Save cookies in JSON format
            with open(f"cookies_save/{key}.json", "w") as file:
                json.dump(enriched_cookies, file, indent=4)
            print(f"{key} Cookies have been saved")

#<< ------------------------ ROYAL SEO COOKIES DOWNLOAD ------------------------------- >>

        url = "https://app.royalseotools.com/member" 
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

        for key, value in tools_royal.items():
            driver.get(value)
            if key == "CloserCopy":
                time.sleep(20)
            else: time.sleep(10)
            
            window_handles = driver.window_handles
            for handle in window_handles:
                driver.switch_to.window(handle)
                if value in driver.current_url:
                    break

            # Get cookies and add the `url` field
            cookies = driver.get_cookies()

            enriched_cookies = [
                {
                    **cookie,
                    "url": f"https://{cookie['domain'].lstrip('.')}"
                }
                for cookie in cookies
            ]

            # Save cookies in JSON format
            with open(f"cookies_save/{key}.json", "w") as file:
                json.dump(enriched_cookies, file, indent=4)
            print(f"{key} Cookies have been saved")



# --------------------- AZAD SEO COOKIES DOWNLOAD  ------------------------------------

        url = "https://members.azadseo.com/login" 
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

        for key, value in tools_Azad.items():
            driver.get(value)
            time.sleep(10)
            
            window_handles = driver.window_handles
            for handle in window_handles:
                driver.switch_to.window(handle)
                if value in driver.current_url:
                    break

            # Get cookies and add the `url` field
            cookies = driver.get_cookies()

            enriched_cookies = [
                {
                    **cookie,
                    "url": f"https://{cookie['domain'].lstrip('.')}"
                }
                for cookie in cookies
            ]

            # Save cookies in JSON format
            with open(f"cookies_save/{key}.json", "w") as file:
                json.dump(enriched_cookies, file, indent=4)
            print(f"{key} Cookies have been saved")




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


        for file_name in os.listdir("cookies_save"):
            i = os.path.splitext(file_name)[0]
            
            url_sem = f"https://portal.rainyclouds.in/{i}.php" 
            driver.get(url_sem)

            cookies_file = f"cookies_save/{i}.json"
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




    except Exception as e:
        print(f"Error during execution: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            try:
                driver.quit()
            except Exception as e:
                print(f"Error while closing driver: {str(e)}")
