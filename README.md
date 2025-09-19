# 🌐 Automate Public WiFi Login

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium-python.readthedocs.io/)
[![Chrome](https://img.shields.io/badge/Chrome-WebDriver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://chromedriver.chromium.org/)
[![Edge](https://img.shields.io/badge/Edge-WebDriver-0078D4?style=for-the-badge&logo=microsoftedge&logoColor=white)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

**⚡ Automate your public WiFi authentication with ease!**

[Installation](#️-installation--setup) • [Features](#-features) • [Usage](#-usage) • [Configuration](#️-configuration) • [Contributing](#-contributing)

</div>

---

## 🚀 Overview

**Automate Public WiFi Login** is a Python-based automation tool designed to streamline your access to public WiFi networks. No more manual authentication every time you connect! This tool uses Selenium WebDriver to programmatically handle WiFi captive portals and authentication pages.

Whether you're at a university, cafe, airport, or any public space with captive portal authentication, this tool saves you time and effort by automating the entire login process.

### ✨ Why This Tool?

- **⏰ Save Time:** No more repetitive manual logins
- **🔄 Seamless Connection:** Automatic authentication on network connection
- **🎯 Universal:** Works with any captive portal-based WiFi system
- **🖥️ Desktop Integration:** Create shortcuts for one-click WiFi connection
- **🛠️ Customizable:** Easy to configure for different networks and portals

---

## 🎯 Features

- **🌐 Universal WiFi Support:** Compatible with any captive portal system
- **🤖 Selenium-Powered:** Robust browser automation using WebDriver
- **🔧 Multi-Browser Support:** Works with Chrome, Chromium, and Microsoft Edge
- **⚙️ Configurable Options:** Customize browser behavior and authentication details
- **📱 Desktop App Creation:** Convert to executable for easy desktop access
- **🔒 Secure Handling:** Supports insecure certificates and localhost connections
- **📋 Element Detection:** Intelligent form field recognition
- **🎨 Headless Mode Support:** Run without visible browser window

---

## ⚙️ Installation & Setup

### 📋 Prerequisites

- **Python 3.7+** installed and added to system PATH
- **pip** package manager
- **Web Browser** (Chrome/Chromium/Edge)
- **Code Editor** (VS Code, PyCharm, etc.) - Optional

### 🔧 Step-by-Step Installation

#### 1. 📦 Install Required Packages

```bash
# Install Selenium WebDriver
pip install selenium

# Optional: For creating executable files
pip install pyinstaller
```

#### 2. 🌐 Download WebDriver

Choose based on your browser:

**For Chrome/Chromium:**
- Download from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
- ⚠️ **Important:** Match your browser version with the driver version

**For Microsoft Edge:**
- Download from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

#### 3. 📁 Setup Project Structure

```
automate-wifi-login/
├── auto.py                # Main automation script
├── chromedriver.exe       # Chrome WebDriver (place in same folder)
├── msedgedriver.exe       # Edge WebDriver (place in same folder)
└── README.md
```

---

## 🛠️ Configuration

### 🔍 Finding Authentication Elements

<div align="center">

![Authentication Page Inspection](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/0d3bd3e2-23f1-4eeb-ab76-b5f34487da82)
*Locate your WiFi authentication page elements*

</div>

1. **🌐 Open Authentication Page:** Navigate to your WiFi login portal
2. **🔍 Inspect Elements:** Right-click → "Inspect" or press `F12`
3. **📝 Identify Fields:** Hover over username, password, and submit elements
4. **📋 Note Element Names/IDs:** Copy the `name`, `id`, or `class` attributes

<div align="center">

![Element Inspection Demo](https://github.com/prateekpurohit13/Automate-VIT-WIFI-Login/assets/145431826/213b4463-e7d6-46eb-ab3b-ec535f7b641d)
*Visual guide to element inspection*

</div>

### ⚙️ Browser Configuration Options

```python
# Essential browser options explained
options.add_argument('--allow-insecure-localhost')  # Allow insecure localhost connections
options.add_experimental_option("detach", True)     # Keep browser open after script ends
options.add_argument("--acceptInsecureCerts")       # Accept insecure SSL certificates
options.add_argument("--no-sandbox")                # Disable sandbox (for certain environments)
options.add_argument("--disable-dev-shm-usage")     # Reduce memory consumption
options.add_argument("--start-maximized")           # Start browser in maximized mode
```

### 📝 Configuration in auto.py

```python
# Example configuration within your auto.py file
WIFI_AUTH_URL = "http://your-wifi-portal.com/login"
USERNAME = "your_username"
PASSWORD = "your_password"
USERNAME_FIELD = "username"  # HTML element name/id
PASSWORD_FIELD = "password"  # HTML element name/id
SUBMIT_BUTTON = "submit"     # HTML element name/id
WEBDRIVER_PATH = "./chromedriver.exe"  # Place driver in same folder as auto.py
```

---

## 🚀 Usage

### 🎯 Basic Usage

1. **📶 Connect to WiFi:** Select your target WiFi network
2. **▶️ Run Script:** Execute the automation script
3. **✅ Automatic Login:** Sit back and watch the magic happen!

```bash
# Run the automation script
python auto.py
```

### 🖥️ Creating Desktop Executable

Transform your script into a convenient desktop application:

```bash
# Install PyInstaller (if not already installed)
pip install pyinstaller

# Create executable from auto.py
pyinstaller --onefile auto.py

# Find your executable in the 'dist' folder
# Pin to desktop for quick access!
```

**🎉 Result:** Double-click the executable whenever you need to connect to WiFi!

---

## 💡 Advanced Features

### 🎭 Multiple Network Support

Configure different authentication profiles for various networks:

```python
NETWORKS = {
    "University_WiFi": {
        "auth_url": "http://university-portal.edu/login",
        "credentials": {"username": "student_id", "password": "password"}
    },
    "Cafe_WiFi": {
        "auth_url": "http://cafe-wifi.com/auth",
        "credentials": {"email": "user@email.com", "password": "password"}
    }
}
```

### 🔄 Auto-Detection

Implement network auto-detection to automatically select the right configuration:

- Detect current network SSID
- Load appropriate authentication profile
- Execute login sequence

### 🛡️ Error Handling

- **Connection timeouts**
- **Element not found errors**  
- **Authentication failures**
- **Network connectivity issues**

---

## 🌟 Use Cases

- **🏫 Educational Institutions:** University/school WiFi portals
- **☕ Public Spaces:** Cafes, restaurants, airports
- **🏨 Hospitality:** Hotels, conferences, events  
- **🏢 Corporate:** Guest networks, temporary access
- **🚌 Transportation:** Public transport WiFi systems

---

## 🤝 Contributing

<div align="center">

**🌟 Contributions are highly appreciated! 🌟**

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

</div>

### 🛠️ How to Contribute

1. **🍴 Fork** the repository
2. **🌿 Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **💾 Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **📤 Push** to the branch (`git push origin feature/AmazingFeature`)
5. **🔄 Open** a Pull Request

### 💭 Ideas for Improvement

- [ ] **🤖 AI-powered element detection**
- [ ] **📱 Mobile app integration**
- [ ] **🔧 GUI configuration interface**
- [ ] **📊 Connection analytics and logging**
- [ ] **🔐 Enhanced security features**
- [ ] **🌍 Multi-language support**
- [ ] **⚡ Speed optimizations**
- [ ] **🔔 Notification system**

---

## ⚠️ Important Notes

> **🔒 Security:** Keep your credentials secure and never commit them to version control
> 
> **⚖️ Legal:** Ensure you comply with the WiFi network's terms of service
> 
> **🔧 Compatibility:** Always match WebDriver versions with your browser version
> 
> **🌐 Network Policy:** Some networks may have restrictions on automated access

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| 🚫 WebDriver not found | Ensure WebDriver is in PATH or specify full path |
| ❌ Element not found | Verify element selectors using browser inspector |
| 🔒 SSL Certificate errors | Add `--ignore-ssl-errors` browser argument |
| 🐌 Page loading timeout | Increase implicit wait time in script |
| 🖥️ Browser won't start | Check WebDriver and browser version compatibility |

---

## 🙏 Acknowledgments

- **Selenium WebDriver** team for the amazing automation framework
- **Python Community** for continuous support and development
- **Contributors** who help improve this tool

---

<div align="center">

**Made with ❤️ for easier WiFi connectivity**

[![GitHub stars](https://img.shields.io/github/stars/prateekpurohit13/automate-public-wifi-login?style=social)](https://github.com/prateekpurohit13/automate-public-wifi-login/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/prateekpurohit13/automate-public-wifi-login?style=social)](https://github.com/prateekpurohit13/automate-public-wifi-login/network/members)

[⬆ Back to top](#-automate-public-wifi-login)

</div>
