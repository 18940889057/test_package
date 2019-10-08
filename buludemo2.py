import unittest
from selenium import webdriver
import datetime
import time
class BaiduTestCase(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例：')
        url = 'http://172.18.15.84/summer-ssoserver/login?service=http%3A%2F%2F172.18.15.84%3A8086%2Fblxt%2F&tgt=null'
        self.driver = webdriver.Ie()  # 选择IE浏览器
        self.driver.get(url)  # 打开补录系统的页面

    def test_bubutton(self):
        #输入补录系统的用户名
        username = self.driver.find_element_by_id("username")
        username.clear()
        username.send_keys("dengzhigang")
        #输入补录系统的密码
        password = self.driver.find_element_by_id("password")
        password.send_keys("")
        #点击登录按钮
        #self.driver.find_element_by_link_text("登录")
        self.driver.find_element_by_class_name("submit_btn").click()
        time.sleep(5000)
        #now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        now_time =time.strftime("%Y/%m/%d-%H_%M_%S", time.localtime())
        print(str('D:/Screenshot/'+now_time+'.png'))
        self.driver.save_screenshot('D:/Screenshot/'+now_time+'.png')  # 截图

    def tearDown1(self):
        print('一条用例执行完成。')
        self.driver.quit()  # 退出浏览器
