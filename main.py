import webbrowser
import pyautogui
import keyboard
# import time

screenWidth, screenHeight = pyautogui.size()

print(screenWidth, screenHeight)

# C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito
url = 'https://capybara-clicker.com/'
# webbrowser.register("browser", None, webbrowser.GenericBrowser(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", "%s"]), preferred=True)
webbrowser.open(url)

im = None
step = 1
countSinceLastScroll = 0
scrollCount = 0
# canUpgrade = True
while True:
    if keyboard.is_pressed("q"):
        break

    # pyautogui.click(628, 575)
    if step == 2:
        # check if you should scroll
        if (pyautogui.pixelMatchesColor(1270, 572, (247, 159, 0)) and scrollCount < 7):
            pyautogui.moveTo(1270, 355)
            pyautogui.scroll(-160)
                #time.sleep(1)
                #if pyautogui.pixelMatchesColor(1270, 572, (247, 159, 0)) and scrollCount < 100 and scrollCount > 50:
                    #pyautogui.scroll(-160)

            countSinceLastScroll = 0
            scrollCount += 1

        # for the last part of the game
        if scrollCount == 7:
            if countSinceLastScroll <= 100 and \
                    pyautogui.pixelMatchesColor(1280, 830, (247, 159, 0)):
                pyautogui.click(1280, 830)
            # hit top item
            else:
                pyautogui.click(628, 575)

            if countSinceLastScroll <= 100 and \
                    pyautogui.pixelMatchesColor(1280, 460, (247, 159, 0)):
                pyautogui.click(1280, 460)
                countSinceLastScroll += 1

            # hit top item
            else:
                pyautogui.click(628, 575)

        else:
            if countSinceLastScroll <= 100 and (pyautogui.pixelMatchesColor(1260, 370, (247, 159, 0)) or pyautogui.pixelMatchesColor(1275, 375, (247, 159, 0)) or pyautogui.pixelMatchesColor(1270, 340, (247, 159, 0))):
                pyautogui.click(1270, 355)
                countSinceLastScroll += 1

            # hit top item
            else:
                pyautogui.click(628, 575)

    elif step == 1:
        red_val = pyautogui.pixel(1804, 225)[0]

        if red_val > 250:
            pyautogui.click(1854, 175)
            step = 2

print("I now have so many capybaras")
