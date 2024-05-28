# Finding The Truth Testing Project

## Description

This project is a UI and API automated test framework written to test the 'Finding the Truth' web application created by Elucidat. It is written in Python and uses Selenium, Request library, Behave for BDD Cucumber style tests, with Allure HTML reporting.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/automation-andy101/finding-the-truth-testing`
2. Navigate to the project directory: `cd finding-the-truth-testin`
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `behave`
5. Generate Allure reports: `allure serve allure-results`. Reports are outputted to the `allure-results` project folder. 
Note:- Allure reporting tool must be installed on your machine to generate Allure reports (instructions on how to install are in a section below). 

## Configuration

Before running the project, make sure you have the following environment variables properly and packages configured:

### JAVA_HOME

`JAVA_HOME` is required to point to your Java Development Kit (JDK) installation. This is necessary for compiling and running Java code.

#### Windows

1. Open the Start Search, type in "env", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables..." button.
3. Click "New" under the "System variables" section.
4. Set `JAVA_HOME` as the variable name and the path to your JDK installation as the variable value.
   - Example value: `C:\Program Files\Java\jdk-11`

#### macOS and Linux

1. Open a terminal.
2. Open your shell profile file in a text editor. This is typically `~/.bashrc` or `~/.bash_profile` for Bash, or `~/.zshrc` for Zsh.
3. Add the following line:
   ```sh
   export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64


### Allure Reports

Install the Allure Report command-line tool, if it is not yet installed in your operating system. Note that Allure Report requires Java, see the installation instructions - https://allurereport.org/docs/install/

Download it from here:-
https://github.com/allure-framework/allure2/releases/tag/2.29.0

Unzip and install when downloaded.

Add Allure bin folder to the PATH environment variable to your machine.

Note:- If you have your IDE (e.g. PyCharm) open you will have to close and re-open the IDE after installing the Allure reporting tool, for Allure Reporting to work.

Install allure-behave into your Python project using the following command:-
`pip install allure-behave`

Now, run your tests by entering the following command in the terminal window:-
`behave`

Generate the HTML reports using the following command:-
`allure serve allure-results`


# **Install Python** ![Python]

A Quick Guide for Installing Python on Common Operating Systems

1. [Install on Windows](#windows-)
2. [Install on MacOS](#macos-)
3. [Install on Linux](#linux-)


## **Windows** ![Windows]
1. If you have not yet installed Python on your Windows OS, then download and install the latest Python3 installer from [Python Downloads Page](https://www.python.org/downloads/)
   - Make sure to check the box during installation which adds Python to PATH. Labeled something like **Add Python 3.X to PATH**

2. Once Python is installed, you should be able to open a command window, type `python`, hit ENTER, and see a Python prompt opened. Type `quit()` to exit it. You should also be able to run the command `pip` and see its options. If both of these work, then you are ready to go.
  - If you cannot run `python` or `pip` from a command prompt, you may need to add the Python installation directory path to the Windows PATH variable
    - The easiest way to do this is to find the new shortcut for Python in your start menu, right-click on the shortcut, and find the folder path for the `python.exe` file
      - For Python3, this will likely be something like `C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python37`
    - Open your Advanced System Settings window, navigate to the "Advanced" tab, and click the "Environment Variables" button
    - Create a new system variable:
      - Variable name: `PYTHON_HOME`
      - Variable value: <your_python_installation_directory>
    - Now modify the PATH system variable by appending the text `;%PYTHON_HOME%\;%PYTHON_HOME%;%PYTHON_HOME%\Scripts\` to the end of it.
    - Close out your windows, open a command window and make sure you can run the commands `python` and `pip`

## **MacOS** ![MacOS]
MacOS comes with a native version of Python. As of this writing, it comes with a version of Python2, which has been deprecated. In order to use most modern Python applications, you need to install Python3. Python2 and Python3 can coexist on the same machine without problems, and for MacOS it is in fact necessary for this to happen, since MacOS continues to rely on Python2 for some functionality.

There are a couple of ways we can install Python3 on your MacOS operating system:

### Option 1: Install the official Python release
1. Browse to the [Python Downloads Page](https://www.python.org/downloads/)
2. Click on the "Download Python 3.x.x" button on the page
3. Walk through the steps of the installer wizard to install Python3
4. Once installed, the wizard will open a Finder window with some `.command` files in it
    - Double-click the `Install Certificates.command` file and the `Update Shell Profile.command` file to run each of them
    - Close the windows once they are finished
6. Open your **Terminal** application and run the command `python3` to enter the Python interactive command line. Issue the command `quit()` to exit. Also make sure PIP (the Python package manager) is installed by issuing the command `pip3 -V`. It should display the current version of PIP as well as Python (which should be some release of Python3).
7. You're all done. Python is installed and ready to use.

### Option 2: Install with Homebrew
[Homebrew](https://brew.sh/) is a MacOS Linux-like package manager. Walk through the below steps to install Homebrew and an updated Python interpreter along with it.

1. Open your **Terminal** application and run: `xcode-select --install`. This will open a window. Click **'Get Xcode'** and install it from the app store.
2. Install Homebrew. Run: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - You can also find this command on the [Homebrew website](https://brew.sh/)
3. Install latest Python3 with `brew install python`
4. Once Python is installed, you should be able to open your **Terminal** application, type `python3`, hit ENTER, and see a Python 3.X.X prompt opened. Type `quit()` to exit it. You should also be able to run the command `pip3` and see its options. If both of these work, then you are ready to go.
  - Here are some additional resources on [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

## **Linux** ![Linux]
- **Raspberry Pi OS** may need Python and PIP
  - Install them: `sudo apt install -y python3-pip`
- **Debian (Ubuntu)** distributions may need Python and PIP
  - Update the list of available APT repos with `sudo apt update`
  - Install Python and PIP: `sudo apt install -y python3-pip`
- **RHEL (CentOS)** distributions usually need PIP
  - Install the EPEL package: `sudo yum install -y epel-release`
  - Install PIP: `sudo yum install -y python3-pip`

    

## Credits

- Created by Andrew Short
