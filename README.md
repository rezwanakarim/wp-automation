# wp-automation
Automation test suite for the WP plugin

## Overview

This repository contains an automation test suite designed to test the functionality of the WP Dark Mode plugin for WordPress. The suite covers scenarios such as plugin activation, dark mode settings, switch customization, and more. The tests are written in Python using Selenium and are configured to run with GitHub Actions for continuous integration.

## Scenarios

The test suite includes the following scenarios:

1. **Log in to WordPress**: Automate the login process to access the WordPress admin panel.
2. **Check Plugin Status**: Verify whether the “WP Dark Mode” plugin is active. If not, activate it.
3. **Enable Admin Dashboard Dark Mode**: Navigate to the WP Dark Mode settings and enable dark mode for the admin dashboard.
4. **Validate Admin Dashboard Dark Mode**: Confirm that the dark mode is applied to the admin dashboard.
5. **Customize Floating Switch**:
    - Change the “Floating Switch Style” from the default selections.
    - Scale the “Floating Switch Size” to 220.
    - Change the “Floating Switch Position” to Left.
6. **Disable Keyboard Shortcut**: Turn off the keyboard shortcut in the Accessibility settings.
7. **Enable Page-Transition Animation**: Activate page-transition animation and change the effect.
8. **Validate Frontend Dark Mode**: Ensure that dark mode is applied on the frontend of the site.

## Requirements

- Python 3.x
- Selenium WebDriver
- ChromeDriver
- WordPress with WP Dark Mode plugin installed

## Setup Instructions
Name of the wordpress site wppool

### 1. Clone the Repository

```bash
git clone https://github.com/rezwanakarim/wp-automation.git
cd wp-automation
```

### 2. Install Dependecies
```bash
pip install selenium
pip install python-dotenv
```

### 3. Change the .env.example file to .env file (Configure Environment Variables)

```bash
WP_USERNAME=your_username_here
WP_PASSWORD=your_password_here
CHROMEDRIVER_PATH=path/to/your/chromedriver

```
### 4. Running the Test Suite
Execute the test suite using Python:

```bash
python test_suite.py

```