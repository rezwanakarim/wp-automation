# WP Automation Test Suite

This repository contains an automation test suite designed to test the functionality of the WP Dark Mode plugin for WordPress. The suite is written in Python using Selenium and can be run locally or through GitHub Actions.

## Table of Contents
1. [Overview](#overview)
2. [Test Scenarios](#test-scenarios)
3. [Requirements](#requirements)
4. [Setup Instructions](#setup-instructions)
   1. [Installing Laragon](#1-install-laragon)
   2. [Setting up WordPress](#2-set-up-wordpress)
   3. [Clone Repository](#3-clone-the-repository)
   4. [Install Dependencies](#4-install-dependencies)
   5. [Configure Environment Variables](#5-configure-environment-variables)
   6. [Run Test Suite](#6-run-test-suite)

---

## Overview

This test suite automates the validation of the WP Dark Mode plugin in WordPress. It covers critical functions like plugin activation, dark mode settings, floating switch customization, and more.

## Test Scenarios

The suite includes the following tests:
1. **Log in to WordPress**: Automate the login process for the WordPress admin panel.
2. **Check Plugin Status**: Verify and activate the WP Dark Mode plugin if needed.
3. **Enable Admin Dashboard Dark Mode**: Turn on dark mode in the admin panel.
4. **Validate Admin Dashboard Dark Mode**: Confirm that dark mode is applied in the admin panel.
5. **Customize Floating Switch**: Adjust style, size, and position of the floating switch.
6. **Disable Keyboard Shortcut**: Disable the dark mode keyboard shortcut in settings.
7. **Enable Page-Transition Animation**: Activate and customize page-transition animations.
8. **Validate Frontend Dark Mode**: Ensure dark mode is applied on the frontend.

---

## Requirements
Before you begin, ensure you have the following installed:
- **Python 3.x**
- **Selenium WebDriver**
- **ChromeDriver**
- **Laragon** (for local WordPress environment)
- **WordPress with WP Dark Mode plugin installed**

---

## Setup Instructions

### 1. Install Laragon

1. **Download Laragon**: [Download here](https://laragon.org/download/).
2. **Install Laragon**:
   - Run the installer and follow the installation steps.
   - After installation, open Laragon.
3. **Start Laragon**: Click “Start All” to launch the services (Apache, MySQL, etc.).

### 2. Set Up WordPress

1. **Create a New Site**:
   - In Laragon, click on **Menu** > **Quick app** > **WordPress**.
   - Name the site `wppool`, and Laragon will automatically set up WordPress for you.
     
2. **Install WP Dark Mode Plugin**:
   - Log in to your WordPress admin dashboard.
   - Navigate to **Plugins** > **Add New**.
   - Search for “WP Dark Mode” and click **Install Now**, then **Activate**.

### 3. Clone the Repository
   - Open the terminal, clone this repository, and navigate to the project directory:

   ```bash
   git clone https://github.com/rezwanakarim/wp-automation.git
   cd wp-automation
   ```

### 4. Install Dependencies
   ```bash
   pip install selenium
   pip install python-dotenv
   ```

### 5. Configure Environment Variables

1. Rename `.env.example` to `.env`:

   ```bash
   mv .env.example .env
   ```
2. Open `.env` and configure the required variables::
   ```bash
   WP_USERNAME=your_username_here
   WP_PASSWORD=your_password_here
   CHROMEDRIVER_PATH=path/to/your/chromedriver
   ```
### 6. Run Test Suite
   - Execute the test suite using Python:
   ```bash
   python test_suite.py
   ```
