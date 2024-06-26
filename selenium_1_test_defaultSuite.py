# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test11(self):
    self.driver.get("https://www.alx.pl/pl/kurs-devops/")
    self.driver.set_window_size(1343, 819)
    self.driver.find_element(By.CSS_SELECTOR, ".lp-zapisz-btn > a").click()
    self.driver.find_element(By.ID, "id_imie_nazwisko").click()
    self.driver.find_element(By.ID, "id_imie_nazwisko").send_keys("Janusz")
    self.driver.find_element(By.ID, "id_osoba_do_kontaktu").send_keys("Testowy1@test.com")
    self.driver.find_element(By.ID, "id_imie_nazwisko").click()
    self.driver.find_element(By.ID, "id_imie_nazwisko").send_keys("Janusz Testowy")
    self.driver.find_element(By.ID, "id_email").click()
    self.driver.find_element(By.ID, "id_email").send_keys("janusz@test.com")
    self.driver.find_element(By.ID, "id_email_ksiegowosc").send_keys("t.kaniecki@email.com")
    self.driver.find_element(By.ID, "id_telefon").send_keys("123-456-789")
    self.driver.find_element(By.ID, "id_adres").send_keys("długa 20")
    self.driver.find_element(By.ID, "id_miejscowosc_kod").send_keys("Warszawa 02-897")
    self.driver.find_element(By.CSS_SELECTOR, ".required:nth-child(25)").click()
    self.driver.find_element(By.XPATH, "TODO:JS tutaj podaj xpath np. div[2]/div[1]").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".required:nth-child(25)").click()
    self.driver.find_element(By.ID, "id_za_kurs_zaplace_0").click()
  
