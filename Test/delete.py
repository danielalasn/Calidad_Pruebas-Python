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

from selenium import webdriver
from selenium.webdriver.common.by import By


class Add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        # self.add()

    def add(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element(By.NAME, "name").click()
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("alumno5")
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys("alumno5@gmail.com")
        driver.find_element(By.NAME, "age").click()
        driver.find_element(By.NAME,"age").clear()
        driver.find_element(By.NAME, "age").send_keys("30")
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Gender'])[2]/following::div[1]").click()
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Male'])[2]/following::div[1]").click()
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Woah!'])[1]/following::button[1]").click()

    def test_delete(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        rows = driver.find_elements(By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr")
        correoBorrado = rows[0].text.split(" ")[1]

        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/table/tbody/tr/td[5]/button[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,
            "/html/body/div[2]/div/div[3]/button[1]").click()
        newRows = driver.find_elements(By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr")

        for row in newRows:
            correo = row.text.split(" ")[1]
            self.assertNotEqual(correo, correoBorrado)


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