import unittest
from selenium import webdriver
import datetime
import time
class BaiduTestCase(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例：')
        url = 'https://www.baidu.com'
        self.driver = webdriver.Ie()  # 选择谷歌浏览器
        self.driver.get(url)  # 打开百度页面

    def test_bubutton(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('软件测试')  # 搜索框输入内容
        self.driver.find_element_by_id('su').click()  # 点击百度按钮
        time.sleep(2)
        #now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        now_time =time.strftime("%Y/%m/%d-%H_%M_%S", time.localtime())
        print(str('D:/Screenshot/'+now_time+'.png'))
        self.driver.save_screenshot('D:/Screenshot/'+now_time+'.png')  # 截图

    def tearDown(self):
        print('一条用例执行完成。')
        self.driver.quit()  # 退出浏览器
