from selenium import webdriver
from utility.chrome_proxy_driver_setup import ChromeProxySetup as CPS
import time

b = CPS() # No Proxy
c = CPS('127.0.0.1',5000,'auth_user','auth_pwd') # With Proxy
driver1 = b.set_proxy() 
driver1.maximize_window()
driver1.get('http://yahoo.com')
time.sleep(5)
driver1.close()
driver2 = c.set_proxy()
driver2.maximize_window()
driver2.get('http://google.com')
time.sleep(5)
driver2.close()