# SupremeBot

Using Python 3(.6)

This basically automates the process of purchasing. I.e. selecting the item and filling out the formula...
Due to the captcha the user has to do the last step on its own. Selenium will open a new chrome window, so one can fill 
out the given captcha.

![Example](https://i.imgur.com/ENN0YzM.png)
![Settings](https://i.imgur.com/rpEFf7X.png)

## Features
+ Refresh items and browser by clicking on kivy icon (top left)
+ Set your own credentials in the settings (like specific sizes, address, etc.)

##### The project can be executed by running the main with python 3.6 or higher.

Due to the chromedriver it cannot by build into an apk anymore.
After some changes one can build an apk with the following steps:

    using buildozer to build
    
    ```buildozer android debug```
    ```buildozer android release```
    
    android debugging via adb logcat
    
    ```adb logcat```

compiling/packaging to exe on windows

``` python -m PyInstaller --name supremeapp ...\SupremeBot\app\main.py ```

or via the .spec file
