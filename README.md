# Automate-PUBLIC-WIFI-Login
This is a tool made to ease your access to public wifi.


If you have got any improvement in this then it is highly appreciable.

Here I will explain the implementation of this tool: -

First I downloaded python and added it to the path of my os (Path can be found in environment variables).Then I used a code editor like VS Code for writing my code. 
In this whole process my first approach was how I can control the web browser programmatically because then only i would be able to understand the further step. So for
this we used "Selenium". Selenium is a library in python which gives you the control to control your web browser like web scrapping, data extraction, automating tasks etc.

To use this library I downloaded it using the command "pip install selenium"

From the selenium library i imported webdriver module.

Then I downloaded the webdriver file of my browser. If you are using chromium based browser you can download chromedriver.exe from https://chromedriver.chromium.org/downloads
and for Microsoft edge browser you can download from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/. (Note:- Do check your browser version before downloading)

After this I start importing respective modules from the library based on the browser i use.

Here you can enter the Website link of your authentication page and your credentials.


![image](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/0d3bd3e2-23f1-4eeb-ab76-b5f34487da82)


Now on your authentication page you can click on inspect to see the html of the website. Now hover over the username, password and submit key to check for the element name.

![ProntoAuthenticationand1morepage-Personal-MicrosoftEdge2024-03-2400-03-39-ezgif com-video-to-gif-converter](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/213b4463-e7d6-46eb-ab3b-ec535f7b641d)

Now you add the path to your browser executeble file and then customize the browser behaviour while running through selenium. Let me add a bit details to this.

options.add_argument('--allow-insecure-localhost') ->  instructs the browser to allow connections to insecure localhost addresses.

options.add_experimental_option("detach", True) -> allows the browser window to remain open even after the WebDriver object is destroyed

options.add_argument("--acceptInsecureCerts") -> instructs the browser to accept insecure SSL certificates

--no-sandbox: disables the sandbox mode, which may be necessary when running the browser in certain environments.

--disable-dev-shm-usage: Disables the use of /dev/shm in shared memory, which can reduce memory consumption.

--start-maximized: Starts the browser in maximized mode, ensuring that the window fills the entire screen.

 and many more like these...........

 Now everything is done. You just need to configure the code with the browser option and redirect it to the link provided.After this you can provide the instructions to be performed and everything is done.
 Turn on your wifi, select the wifi you want to connect and run the code. You will be able to successfully automate your wifi login.

 We can do this for any type of website which requires authentication everytime. e.g facebook. 

 If you want to directly run from your desktop without opening the code file then you can do that also.

 Run pip install pyinstaller

 after successful installation run pyinstaller --onefile <yourfile.py> (Replace yourfile with the main source file).

 After this you will see a folder named dist. Open that folder and pin that application to desktop shortcuts. Now whenever you want to connect to wifi just open the wifi and click on that application.

 Thank You...
