import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto.application import Application
from pywinauto.keyboard import send_keys


driver = webdriver.Firefox()
driver.get('http://127.0.0.1:5173')
driver.maximize_window()
print(driver.title)
time.sleep(2)



# 模拟单张图片上传
## 上传单张图片
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div/div/div/div").click()
time.sleep(2)
#### 使用pywinauto来选择文件
app = Application()
time.sleep(2)
#### 定位到窗口
app = app.connect(class_name='#32770')
#### 在输入框输入文件位置
app['文件上传']['Edit1'].set_edit_text(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\selenium_test\test_data\000.JPG')
#### 点击打开，上传文件
time.sleep(2)
send_keys('{ENTER}')
time.sleep(5)
## 获取检测结果
result_data = []
result = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div").text
times = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div").text
rate = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div").text
result_data.append([result, times, rate])



# 模拟批量上传
## 切换至批量上传界面
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/ul/li[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/button").click()
app = Application()
app = app.connect(class_name='#32770')
#### 在输入框输入文件位置
app['文件上传']['Edit1'].set_edit_text(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\selenium_test\test_data\product_test.zip')
#### 点击打开，上传文件
time.sleep(2)
send_keys('{ENTER}')
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div/form/div/div/div").click()
time.sleep(2)
driver.switch_to.active_element.send_keys("516680918@qq.com")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button").click()



# 写入txt文件
with open(r"C:\Users\LiYanLin\Desktop\defect_product_backEnd\selenium_test\test_result.txt", "w", encoding='utf-8') as f:
    f.writelines("单张图片测试结果")
    f.writelines(str(result_data))
    f.writelines("\n")
