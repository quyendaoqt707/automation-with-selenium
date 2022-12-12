# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 15)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        # self.driver = webdriver.Firefox()
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        f = open("log.txt", "w")
        f.close()
        f = open("log.txt", "a")
        driver = self.driver
        driver.get("https://sandbox.moodledemo.net/")
        # driver.find_element("id","page").click()
        # driver.find_element_by_link_text("Log in").click()
        # driver.find_element("link text", u"Log in").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span/a").click()

        driver.find_element("id","username").click()
        driver.find_element("id","username").clear()
        driver.find_element("id","username").send_keys("teacher")
        driver.find_element("id","password").click()
        driver.find_element("id","password").clear()
        driver.find_element("id","password").send_keys("sandbox")
        driver.find_element("id","loginbtn").click()
        driver.find_element("link text","My first course").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/nav/div[2]/form/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='coursecontentcollapse0']/button/span[2]").click()

        #Select Assignment
        f.write("Assignment\n")
        driver.implicitly_wait(1)
        # driver.find_element(By.XPATH,"//body[1]/div[8]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]").click()
        try:
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"//html[1]/body[1]/div[9]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]")))
        finally:
            f.write("Assignment found\n")
        
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[9]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
        
        
        driver.implicitly_wait(1)
        
        driver.find_element("id","id_name").click()
        driver.find_element("id","id_name").clear()
        driver.find_element("id","id_name").send_keys("test")
        driver.find_element("id","id_assignsubmission_file_maxfiles").click()
        Select(driver.find_element("id","id_assignsubmission_file_maxfiles")).select_by_visible_text("2")

        driver.find_element(By.XPATH,"//*[@id='fitem_fgroup_id_assignsubmission_file_filetypes']/div[2]/fieldset/div/span/input").click()
        driver.implicitly_wait(1)

        #Choose button
        f.write("Choose button\n")
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH,"//body[1]/div[5]/div[5]/div[1]/div[3]/div[1]/section[1]/div[1]/form[1]/fieldset[3]/div[2]/div[5]/div[2]/fieldset[1]/div[1]/span[1]/input[1]").click()
        wait_for_ajax(driver)
        #Expand document:
        f.write("Expand document:\n")
        driver.implicitly_wait(2)
        try:
            wait_for_ajax(driver)
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"//div[@data-filetypesbrowserkey='document'][1]/small[1]/a")))
            driver.find_element(By.XPATH,"//div[@data-filetypesbrowserkey='document'][1]/small[1]/a").click()
            time.sleep(5)
        finally:
            f.write("   Expanded document\n")

        wait_for_ajax(driver)


        #Select .pdf
        f.write("Select .pdf\n")
        driver.implicitly_wait(2)
        cssSelector ="body.format-topics.limitedwidth.path-mod.path-mod-assign.chrome.dir-ltr.lang-en.yui-skin-sam.yui3-skin-sam.sandbox-moodledemo-net.pagelayout-admin.course-2.context-18.category-1.editing.uses-drawers.drawer-open-index.jsenabled.scrolled.vsc-initialized.has-region-side-pre.empty-region-side-pre.modal-open.dndsupported:nth-child(5) div.modal.moodle-has-zindex.show:nth-child(2) div.modal-dialog.modal-dialog-scrollable div.modal-content div.modal-body div:nth-child(6) ul.unstyled.list-unstyled:nth-child(4) li:nth-child(6) label:nth-child(1) > input:nth-child(1)"

        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,cssSelector)))
            driver.find_element(By.CSS_SELECTOR,cssSelector).click()
            f.write("  checked\n")
        finally:
            pass
        # driver.find_element("id","id_submitbutton").click()
    
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
