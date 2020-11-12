from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.expedia.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a/span').click()

driver.find_element(By.XPATH, '//*[@id="location-field-leg1-origin-menu"]/div[1]/button').send_keys("SFO")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button/div/div[1]/span/strong').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[1]/button').send_keys("NYC")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button/div/div[2]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stops-0"]')))
driver.quit()

