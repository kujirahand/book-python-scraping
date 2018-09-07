from selenium.webdriver import Firefox, FirefoxOptions

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# Firefoxをヘッドレスモードを有効にする --- (※1)
options = FirefoxOptions()
options.add_argument('-headless')

# Firefoxを起動する --- (※2)
browser = Firefox(options=options)

# URLを読み込む --- (※3)
browser.get(url)

# 画面をキャプチャしてファイルに保存 --- (※4)
browser.save_screenshot("website.png")
# ブラウザを終了 --- (※5)
browser.quit()

