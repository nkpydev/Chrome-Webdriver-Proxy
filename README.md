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

Clean up sequence added as feature, so that once your work with proxies is done, the unnecessary '.zip' extension files should be removed from the 'utility' folder.

This feature is added to pass a singal to the imported cleanup class that whatever work was - it is done for extensions, and now we can remove them.

```python
from utility.extension_clean_up import cleanUp

. # code start
.
.
.
. # code ends
cleanUp(True).clean_extensions()
```


### To Do:
- ~~Add extension cleanup~~
- Any features ? Lets think on this!

### Issues:
- <del>Extension wont work unless either all tabs are refreshed or unless we visit: "http://reload.extensions"</del>

### Author:
[nkpydev](https://github.com/nkpydev)

#### LICENSE:
[MIT](https://github.com/nkpydev/Selenium_Helper_Class/blob/master/LICENSE)
