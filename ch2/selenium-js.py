from selenium.webdriver import Firefox, FirefoxOptions

# Firefoxを起動
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# 適当なWebサイトを開く
browser.get("https://google.com")

# JavaScriptを実行
r = browser.execute_script("return 100 + 50")
print(r)
