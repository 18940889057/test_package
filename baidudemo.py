# coding=utf-8
import unittest
import HTMLTestRunner

if __name__ == "__main__":
    # 测试用例保存的目录
    case_dirs = r"./"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_dirs, "baidudemo2.py")
    # 运行测试用例同时保存测试报告
    #测试github使用
    test_report_path = r"D:\report\report.html"
    with open(test_report_path, "wb") as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="华宇应用功能测试")
        runner.run(discover)