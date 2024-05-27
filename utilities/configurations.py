from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import configparser


def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def get_api_config():
    config = configparser.ConfigParser()
    config.read('utilities/api_properties.ini')
    return config
