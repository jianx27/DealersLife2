import pyautogui
import time

# 定义颜色值
target_color1 = (221, 221, 221)
target_color2 = (167, 129, 66)
target_color3 = (242, 235, 206)
target_color4 = (243, 237, 215)
# 等待一段时间，确保你可以切换到正确的窗口或应用程序
time.sleep(3)

for i in range(100):
    pixel_color1 = pyautogui.pixel(2330, 540)#查看物品叉号位置
    #print(pixel_color1)
    pixel_color2 = pyautogui.pixel(333, 666)#开始营业位置
    #print(pixel_color2)
    pixel_color3 = pyautogui.pixel(80, 850)#不感兴趣
    print(pixel_color3)
    print(i)
    #time.sleep(0.1)
    # 检查颜色是否与目标颜色相同
    if pixel_color1 == target_color1:
        pyautogui.click(2330, 540)      
        #取消X
    elif pixel_color2 == target_color2:
        pyautogui.click(333,666)
        #print("begin a day!")
    elif pixel_color3 == target_color3:
        pyautogui.click(60, 850)
    elif pixel_color3 == target_color4:
        pyautogui.click(60, 850)
        #任何人来都不感兴趣
    else:
       pyautogui.click(60, 700)