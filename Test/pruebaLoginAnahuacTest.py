# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # def test_untitled_test_case(self):
    #     driver = self.driver
    #     driver.get(
    #         "https://www.google.com/search?q=anahuac+mayab+dti&oq=anahuac+mayab+dti&aqs=chrome..69i57.3192j0j4&sourceid=chrome&ie=UTF-8")
    #     driver.find_element(By.XPATH, "//div[@id='rso']/div/div/div/div/div/div/div/div/a/h3").click()
    #     driver.get("https://dti.anahuacmayab.mx/")
    #     driver.find_element(By.XPATH,
    #         "//img[contains(@src,'https://dti.anahuacmayab.mx/wp-content/uploads/2022/06/D2L-Logo-Black-ORANGE.svg')]").click()
    #     driver.get(
    #         "https://login.microsoftonline.com/0d8d6b97-e05d-460c-b6b5-19b7d020f47a/saml2?SAMLRequest=jdE7a8MwEADgvdD%2fILTbevgVCzsQ2iWQLknboUuRZCU22JKrk0t%2ffpWGlEKXbPfg4Lu7ZrOE3u7Nx2IgoO1ji0FOo7%2fk77TjVHZcMa7LvONSUl51TK3qoig7pVYYvRoPg7Mt5inFaAuwmK2FIG2IJcqzhGYJz585F6wQBU3LKmesrN8w2gAYH%2bLsg7OwTMYfjP8ctHnZ71rchzCDIERa2S9Sp8oPpz7ALLVJtZtIx0cyzkRGPBndabDkzN6dozT2MPqaRgstXrwVTsIAwsrJgAhaHDZPOxG1YvYuOO1GvL6%2fQ6j5sftbBuVVjtdXZ1bltWSqSopjuUry2mSJKosiydhR8y5nNNPHNBgb7wL%2flvmlN%2bSCiKCG%2fH3M%2bhs%3d")
    #     driver.find_element(By.ID,"i0116").click()
    #     driver.find_element(By.ID,"i0116").clear()
    #     driver.find_element(By.ID,"i0116").send_keys("00341165@anahuac.mx")
    #     driver.find_element(By.ID,"idSIButton9").click()
    #     driver.find_element(By.ID,"i0118").clear()
    #     driver.find_element(By.ID,"i0118").send_keys("jjjjjj")
    #     time.sleep(3)
    #     driver.find_element(By.ID,"idSIButton9").click()
    #     time.sleep(3)
    #     passwordError_txt = driver.find_element(By.ID, "passwordError").text
    #     print(passwordError_txt)
    #     self.assertEqual(u"Your account or password is incorrect. If you don't remember your password, reset it now.",
    #                      passwordError_txt)
    #
    #     driver.get("https://login.microsoftonline.com/0d8d6b97-e05d-460c-b6b5-19b7d020f47a/login")

    def test_untitled_test_case2(self):
        driver = self.driver
        driver.get(
            "https://www.google.com/search?q=anahuac+mayab+dti&oq=anahuac+mayab+dti&aqs=chrome..69i57.3192j0j4&sourceid=chrome&ie=UTF-8")
        driver.find_element(By.XPATH, "//div[@id='rso']/div/div/div/div/div/div/div/div/a/h3").click()
        driver.get("https://dti.anahuacmayab.mx/")
        driver.find_element(By.XPATH,
            "//img[contains(@src,'https://dti.anahuacmayab.mx/wp-content/uploads/2022/06/D2L-Logo-Black-ORANGE.svg')]").click()
        driver.get(
            "https://login.microsoftonline.com/0d8d6b97-e05d-460c-b6b5-19b7d020f47a/saml2?SAMLRequest=jdE7a8MwEADgvdD%2fILTbevgVCzsQ2iWQLknboUuRZCU22JKrk0t%2ffpWGlEKXbPfg4Lu7ZrOE3u7Nx2IgoO1ji0FOo7%2fk77TjVHZcMa7LvONSUl51TK3qoig7pVYYvRoPg7Mt5inFaAuwmK2FIG2IJcqzhGYJz585F6wQBU3LKmesrN8w2gAYH%2bLsg7OwTMYfjP8ctHnZ71rchzCDIERa2S9Sp8oPpz7ALLVJtZtIx0cyzkRGPBndabDkzN6dozT2MPqaRgstXrwVTsIAwsrJgAhaHDZPOxG1YvYuOO1GvL6%2fQ6j5sftbBuVVjtdXZ1bltWSqSopjuUry2mSJKosiydhR8y5nNNPHNBgb7wL%2flvmlN%2bSCiKCG%2fH3M%2bhs%3d")
        driver.find_element(By.ID,"i0116").click()
        driver.find_element(By.ID,"i0116").clear()
        driver.find_element(By.ID,"i0116").send_keys("00341165@anahuac.mx")
        driver.find_element(By.ID,"idSIButton9").click()
        driver.find_element(By.ID,"i0118").clear()
        driver.find_element(By.ID,"i0118").send_keys("clave")
        time.sleep(3)
        driver.find_element(By.ID,"idSIButton9").click()
        time.sleep(3)
        personalInfo = driver.find_element(By.XPATH,"/html/body/header/nav/d2l-navigation/d2l-navigation-main-header/div[2]/div[3]/d2l-navigation-dropdown-button-custom/span/span").text
        print(personalInfo)
        self.assertEqual(u"José Daniel Alas Nuñez", personalInfo)


        driver.get("https://login.microsoftonline.com/0d8d6b97-e05d-460c-b6b5-19b7d020f47a/login")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
