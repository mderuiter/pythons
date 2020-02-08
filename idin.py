import re
import time
import pyqrcode
from selenium import webdriver

# Setup Driver
driver = webdriver.Chrome("/Users/milan/Projects/Python/chromedriver")

# Go to BKR website
driver.get('https://mijnkredietoverzicht.bkr.nl/inloggen/idin/');

# Select ABN from select
driver.find_element_by_xpath("//*[@id='SelectedIssuer']/optgroup/option[1]").click()

# Press submit button
driver.find_element_by_xpath("//*[@id='submit']").click()

# Get current url
url = driver.current_url

# Create deeplink URL
queries = re.split("\?random=", url)[1]
random = re.split("\&trxid=", queries)[0]
trxid = re.split("\&trxid=", queries)[1]
deeplink = "nl.abnamro.idin://?random={}&trxid={}".format(random, trxid)

# Quits browser
driver.quit()

# qr deeplink
qr = pyqrcode.create(deeplink)
qr.png('url.png', scale=5)
print(qr.terminal())