#!/usr/bin/env py
# -*- coding: utf-8 -*-
__author__ = 'inna'

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class wta(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst): 
        inst.driver = webdriver.Chrome('/path/to/your/Selenium/chromedriver')  
        inst.main_page = inst.driver.current_window_handle
        inst.driver.maximize_window()
        inst.driver.get('https://wta-with-se34-webdriver.info/')

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

    def test_a_checkbox_summary(self): 
        link = self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[3]/td/a")
        link.click()
        for new_window in self.driver.window_handles:
            if new_window != self.main_page:
                self.new_window_ind = new_window
                break
        self.driver.switch_to.window(self.new_window_ind)
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"iFrame4")))
        element = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[2]/td[1]/input")
        element.click()
        self.assertEqual('true', element.get_attribute("checked"))
        
    def test_b_text_summary(self):
        text = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[2]/td[3]/input")
        text.clear()
        text.send_keys("15");
        self.assertEqual('15', text.get_attribute("value"))

    def test_c_text_summary(self):
        text = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[2]/td[4]/input")
        text.clear()
        text.send_keys("2020");
        self.assertEqual('2020', text.get_attribute("value"))

    def test_d_dropDownByXPath(self):
        element = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[2]/td[5]/select[@name='select-skill']/option[text()='Advanced']")
        element.click()
        self.assertEqual('Advanced', element.get_attribute("value"))

    def test_e_radioButton(self):
        element = self.driver.find_element_by_xpath("/html/body/div[1]/form/table[2]/tbody/tr[2]/td[6]/input[2]")
        element.click()
        value = element.get_attribute("value")
        self.assertEqual('Update', value)

    def test_f_checkbox_summary(self): 
        element = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[4]/td[1]/input")
        element.click()
        self.assertEqual('true', element.get_attribute("checked"))

    def test_g_text_summary(self):
        text = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[4]/td[3]/input")
        text.clear()
        text.send_keys("1");
        self.assertEqual('1', text.get_attribute("value"))

    def test_h_text_summary(self):
        text = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[4]/td[4]/input")
        text.clear()
        text.send_keys("2020");
        self.assertEqual('2020', text.get_attribute("value"))

    def test_i_dropDownByXPath(self):
        element = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[4]/td[5]/select[@name='select-skill']/option[text()='Novice']")
        element.click()
        self.assertEqual('Novice', element.get_attribute("value"))

    def test_j_radioButton(self):
        element = self.driver.find_element_by_xpath("/html/body/div[1]/form/table[2]/tbody/tr[4]/td[6]/input[2]")
        element.click()
        value = element.get_attribute("value")
        self.assertEqual('Update', value)
        self.driver.switch_to.default_content()

    def test_k_findElementInTable(self):
        text = self.find_cell_style_border()
        self.assertEqual('Selenium', text)
        self.driver.switch_to.default_content()
        self.driver.close()
        self.driver.switch_to.window(self.main_page)

    def test_l_click_checkbox(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[2]/a")
        link.click()  
        self.switch_to_new_window() 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/table/tbody/tr[2]/td/label/span")))     
        element = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr[2]/td/label/span")
        element.click()
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_m_click_radio_button(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[3]/a")
        link.click()  
        self.switch_to_new_window() 
        element = self.driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td/label/span")
        element.click()
        element = self.driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td/label/span")
        element.click()
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_n_populate_textbox(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[4]/a")
        link.click()  
        self.switch_to_new_window() 
        text = self.driver.find_element_by_id("first_name_2")
        text.clear()
        text.send_keys("Bee")
        self.assertEqual('Bee', text.get_attribute("value"))
        text = self.driver.find_element_by_id("last_name")
        text.clear()
        text.send_keys("Awake");
        self.assertEqual('Awake', text.get_attribute("value"))
        text = self.driver.find_element_by_id("email_id")
        text.clear()
        text.send_keys("your-email@yahoo.com");
        self.assertEqual('your-email@yahoo.com', text.get_attribute("value"))
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_o_select_from_dropdown(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[5]/a")
        link.click()  
        self.switch_to_new_window()         
        element = self.driver.find_element_by_xpath("//*[@id='skill-level']/option[3]")
        element.click()
        self.assertEqual('Advanced', element.get_attribute("value")) 
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_p_click_submit_with_alert(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[6]/a")
        link.click()  
        self.switch_to_new_window()     
        element = self.driver.find_element_by_xpath("//*[@id=\"submit_it\"] ")
        self.driver.execute_script("arguments[0].click();", element); 
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        self.assertEqual("Don't forget to test alert!!", alert.text)   
        alert.accept()
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_r_findElementInTable(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[7]/a")
        link.click()  
        self.switch_to_new_window()
        text = self.find_cell_style_border()
        self.assertEqual('Selenium', text)
        self.driver.switch_to.default_content()
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
        
    def test_s_click_link(self):
        link = self.driver.find_element_by_xpath("//*[@id=\"exploring\"]/ul/li[8]/a")
        link.click()  
        self.switch_to_new_window()
        link = self.driver.find_element_by_xpath("/html/body/div[2]/h3[2]/a")
        self.driver.close()
        self.driver.switch_to.window(self.main_page)
     
    def find_cell_style_border(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"iFrame5")))
        table = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody")
        rowsCltn = table.find_elements_by_xpath("//*[@id=\"skills\"]/tbody/tr")
        if len(rowsCltn) > 0:
            i=2;
            while i <= len(rowsCltn):
                text = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[" +str(i) +"]/td[1]").text;
                if(text == "Selenium"):
                    element = self.driver.find_element_by_xpath("//*[@id=\"skills\"]/tbody/tr[" +str(i) +"]/td[1]")
                    self.driver.execute_script("arguments[0].scrollIntoView();", element);
                    self.driver.execute_script("arguments[0].style.border='3px solid red'", element);
                    break               
                i +=1; 
        return text    
                   
    def switch_to_new_window(self):
        for new_window in self.driver.window_handles:
            if new_window != self.main_page:
                self.new_window_ind = new_window
                break
        self.driver.switch_to.window(self.new_window_ind)
        
if __name__ == "__main__":
        unittest.main()
