import pyautogui
import time

# 定义颜色值
target_color = (242, 235, 206)
target_color2 = (140, 203, 118)
target_color3 = (179, 184, 132)
target_color4 = (221, 221, 221)
target_color5 = (143, 167, 213)#庄园领主
# 等待一段时间，确保你可以切换到正确的窗口或应用程序
time.sleep(3)

for i in range(700):
    # 获取坐标(500, 700)处的颜色
    pixel_color = pyautogui.pixel(600, 700)
    #print(pixel_color)
    pixel_color2 = pyautogui.pixel(1850, 1290)
    #print(pixel_color2)
    pixel_color3 = pyautogui.pixel(333,1111)
    #print(pixel_color3)
    pixel_color4 = pyautogui.pixel(2330, 540)
    #print(pixel_color4)
    pixel_color5 = pyautogui.pixel(60, 700)
    #print(pixel_color5)
    print(i)
    #time.sleep(0.1)
    # 检查颜色是否与目标颜色相同
    if pixel_color4 == target_color4:
        pyautogui.click(2330, 540)      
    elif pixel_color2 == target_color2:
        # 如果颜色相同，单击两次交易,如果连击三次以上就不交易
        pyautogui.click(1850, 1290, clicks=2)
        pyautogui.click(2170, 1350, clicks=1)
        pyautogui.click(2180, 1330, clicks=1)
        #print("deal")
    elif pixel_color3 == target_color3:
        pyautogui.click(333,666)
        #print("begin a day!")
    elif pixel_color5 == target_color5:
        pyautogui.click(80, 850, clicks=2)
    else:
        pyautogui.click(500, 700, clicks=2)
        # 如果颜色相同，单击两次看看
        #print("see")



