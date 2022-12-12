# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script

        # options = Options()
        # options.add_experimental_option("detach", True)
        # self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver


        driver.get("https://sandbox.moodledemo.net/")
        # driver.find_element("id","page").click()
        # driver.find_element_by_link_text("Log in").click()
        # driver.find_element("link text", u"Log in").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span/a").click()

        driver.find_element("id","username").click()
        driver.find_element("id","username").clear()
        driver.find_element("id","username").send_keys("student")
        driver.find_element("id","password").click()
        driver.find_element("id","password").clear()
        driver.find_element("id","password").send_keys("sandbox")
        driver.find_element("id","loginbtn").click()

        driver.get("https://sandbox.moodledemo.net/mod/assign/view.php?id=4&action=editsubmission")
        # dragdrop = driver.find_element_by_xpath('paste-the-full-xpath-here')
        self.driver.implicitly_wait(15)
        try:
            # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,".fm-empty-container")))
            # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,".dndupload-target")))
            # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".dndupload-target")))
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".fm-empty-container")))



            # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div/form/fieldset/div[2]/div/div[2]/fieldset/div[1]/div[4]/div[1]/div[2]")))
            dragdrop = driver.find_element(By.CSS_SELECTOR,".dndupload-target")
            dragdrop.send_keys(os.path.abspath("D:\\PROJECTS\\automationTesting\\a.py"))
        finally:
            pass
        # dragdrop = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div/form/fieldset/div[2]/div/div[2]/fieldset/div[1]/div[4]/div[1]/div[2]')
        self.driver.implicitly_wait(5)
        # dragdrop.send_keys('a.py')
        # driver.quit()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
