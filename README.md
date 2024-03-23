# Automate-VIT-WIFI-Login
This is a tool made to ease your access to vit wifi.


If you have got any improvement in this then it is highly appreciable.

Here I will explain the implementation of this tool: -

First I downloaded python and added it to the path of my os (Path can be found in environment variables).Then I used a code editor like VS Code for writing my code. 
In this whole process my first approach was how I can control the web browser programmatically because then only i would be able to understand the further step. So for
this we used "Selenium". Selenium is a library in python which gives you the control to control your web browser like web scrapping, data extraction, automating tasks etc.

To use this library I downloaded it using the command "pip install selenium"

From the selenium library i imported webdriver module.

Then I downloaded the webdriver file of my browser. If you are using chromium based browser you can download chromedriver.exe from https://chromedriver.chromium.org/downloads
and for Microsoft edge browser you can download from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/.

After this I start importing respective modules from the library based on the browser i use.

Here you can enter the Website link of your authentication page and your credentials.


![image](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/0d3bd3e2-23f1-4eeb-ab76-b5f34487da82)

Now you add the path to your browser executeble file and then customize the browser behaviour while running through selenium. Let me add details to this.


Now on your authentication page you can click on inspect to see the html of the website. Now hover over the username, password and submit key to check for the element name.

![ProntoAuthenticationand1morepage-Personal-MicrosoftEdge2024-03-2400-03-39-ezgif com-video-to-gif-converter](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/213b4463-e7d6-46eb-ab3b-ec535f7b641d)

