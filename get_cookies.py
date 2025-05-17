import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time# Function to get cookies from browser (as before)
def get_cookies_from_browser():
    try:
        options = Options()
        # Uncomment for headless mode
        # options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("start-maximized")
        
        driver = webdriver.Chrome(options=options)
        driver.get("https://tradingview.com")
        
        time.sleep(3)  # Give JS time to run
        cookies = driver.get_cookies()
        driver.quit()
        
        return {cookie['name']: cookie['value'] for cookie in cookies}
    except Exception as e:
        print(f"Error in get_cookies_from_browser: {e}")
        return {}

cookies = get_cookies_from_browser()
if cookies:
    print("Extracted Cookies:")
    print(cookies)
else:
    print("No cookies extracted.")


response = requests.get('https://tradingview.com',cookies=cookies)
print(response.status_code)

print("-----continue and enjoy scraping -----")
