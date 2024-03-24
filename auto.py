#download webdriver.exe of respective browser and keep it in the same directory where this python file is.

from selenium import webdriver

#for chromium based browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#for Microsoft Edge browser uncomment the below line..
#from msedge.selenium_tools import Edge, EdgeOptions

#Enter the website link
site = " "
#Enter your username and password
username = " "
password = " "

#Enter the element info by inspecting html of the authentication page
#look for the name assigned to username, password and submit key
username_element = " "
password_element = " "
submit_element = " "

binary_path = " "  # Adjust the path of browser as per your system
#e.g C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe is the default path for brave browser


#Customization of Browser behaviour while running through selenium
options = Options()
options.binary_location = binary_path
options.add_argument('--allow-insecure-localhost')
options.add_experimental_option("detach", True)
options.add_argument("--acceptInsecureCerts")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-web-security")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")

#configures the browser options and redirects to the specified webpage.     (Uncomment for edge browser)
service = Service(executable_path="chromedriver.exe")
#service = Service(executable_path="edgedriver.exe")

browser = webdriver.Chrome(service=service, options=options)
#browser = webdriver.Edge(service=service, options=options)

browser.get(site)

#Executes by matching the specified instructions provided
try:
    print('browser opened')
    usernameElement = browser.find_element("name", username_element)
    usernameElement.send_keys(username)

    passwordElement = browser.find_element("name", password_element)
    passwordElement.send_keys(password)

    submitButtonElement = browser.find_element("name", submit_element)
    submitButtonElement.click()

except Exception as e:
    print(e)
    browser.quit()
