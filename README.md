# Chrome Proxy Setup

A utility developed to add Proxy to Chromedriver when utilizing through Selenium.

Proxy will be set as an extension to the Chrome WebDriver.

_Setting Proxy is **Optional**, so the program will work even if you dont specify any Proxy details._

- [x]  Works without Proxy
- [x]  Works with Non-Authenticated Proxy
- [x]  Works with Authenticated Proxy

## Usage:

Import chrome_proxy_driver_setup into your program like:

```python
from utility.chrome_proxy_driver_setup import ChromeProxySetup as CPS
b = CPS() # if you dont want to use proxy
b = CPS('127.0.0.1',5000) # Non-Authenticated Proxy
b = CPS('127.0.0.1', 5000, 'proxy_auth_user', 'proxy_auth_pwd') # 
'ip','port','auth_user','auth_pwd' # Authenticated Proxy
```

### To Do:
- Add extension cleanup

### Author:
[nkpydev](https://github.com/nkpydev)

#### LICENSE:
[MIT](https://github.com/nkpydev/Selenium_Helper_Class/blob/master/LICENSE)