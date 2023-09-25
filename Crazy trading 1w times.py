import pyautogui
import time

# 定义颜色值
target_color = (242, 235, 206) #我们交易吧框内白区(600,700)颜色
target_color2 = (140, 203, 118) #交易亮色绿按钮(1850,1290)颜色
target_color3 = (167, 129, 66) #开始交易黄色区(333,666)颜色
target_color4 = (221, 221, 221) #查看物品叉号(2330,540)颜色
target_color5 = (143, 167, 213) #庄园领主特供“我有一些物品”，位置(60,700)颜色
# 等待一段时间，确保你可以切换到正确的窗口或应用程序
time.sleep(3)

for i in range(100):#修改循环次数
    pixel_color = pyautogui.pixel(600, 700)#位置1及颜色
    #print(pixel_color)
    pixel_color2 = pyautogui.pixel(1850, 1290)#位置2及颜色
    #print(pixel_color2)
    pixel_color3 = pyautogui.pixel(333,666)#位置3及颜色
    #print(pixel_color3)
    pixel_color4 = pyautogui.pixel(2330, 540)#位置4及颜色
    #print(pixel_color4)
    pixel_color5 = pyautogui.pixel(60, 700)#位置5及颜色
    #print(pixel_color5)
    print(i)
    #time.sleep(0.1)
    # 先检查屏幕上是否有叉号，有则单击
    if pixel_color4 == target_color4:
        pyautogui.click(2330, 540)      
    elif pixel_color2 == target_color2:
        # 如果颜色相同，单击两次交易√，后面两项操作x是应对报价为0的情况
        pyautogui.click(1850, 1290, clicks=2)
        pyautogui.click(2170, 1350, clicks=1)#位置6
        pyautogui.click(2180, 1330, clicks=1)#位置7
        #print("deal")
    elif pixel_color3 == target_color3:
        # 开始营业
        pyautogui.click(333,666)
        #print("begin a day!")
    elif pixel_color5 == target_color5:
        pyautogui.click(80, 850, clicks=2)#位置8
    else:
        # 不属于以上任一种情况，单击此处
        pyautogui.click(500, 700, clicks=2)#位置9
        #print("see")



