import time
import os
import unittest
from XTestRunner import HTMLTestRunner
from email_manage import EmailManage

"""This script is aim to 
1)run the test cases under class TestEcshop
2)send email with report.html to QQ email from 163 mail
PS)Should enable service->IMAP/SMTP in the 163 mail"""
class TestEcshop(unittest.TestCase):

    def test_01_case1(self):
        print('test case1')

    def test_02_case2(self):
        print('test case2')

    def test_03_case3(self):
        print('test case3')

if __name__ == '__main__':
    current_path = os.getcwd()
    # print("current_path is: " + current_path) # for debug
    suite = unittest.defaultTestLoader.discover(current_path, '*.py')
    abs_file = current_path + '\\' + r'report.html'
    # print("abs_file is: " + abs_file) # for debug
    files = open(abs_file, 'wb')
    runner = HTMLTestRunner(stream=files, title='CodeSend2Mails', description='AllTestCasesResults')
    runner.run(suite)
    files.close() # 在发动之前一定要把文件流关闭
    # 发送邮件
    time.sleep(3) # should give some minutes to wait generating report then can send successfully
    EmailManage().send_email(files.name)