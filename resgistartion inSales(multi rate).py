from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()
driver.get("https://www.insales.ru/")

def wait_for_selector(selector, fn, step):
   element = WebDriverWait(driver, 30000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
   print("Step ", step, "succsess")
   
   fn(element)

# Регистрация с главной
wait_for_selector(".text-center-md", lambda element: (element.send_keys("ads123fgffg@hkjk.sdf"), element.send_keys(Keys.RETURN)), "registartion account")
# Выбор типа магазина и подтверждение действия
wait_for_selector('.account-create-confirmation__combo .ui-radio input[type="radio"]', lambda element: element.click(), "check classic")
wait_for_selector('.v-btn__content', lambda element: element.click(), "confirm classic")
# Раскрытие списка категорий, выбор и подтверждение
wait_for_selector('.qualification-dialog__inner .ui-select div[role="button"]', lambda element: element.click(), "open categories")
wait_for_selector('.v-menu__content .v-select-list div:first-child', lambda element: element.click(), "choose category")
wait_for_selector('.qualification-dialog__inner .v-btn__content', lambda element: element.click(), "confirm classic")
# Выбор маркетплейса Ozon
wait_for_selector('.qualification-dialog__content .v-stepper__content:nth-child(2) div[step]:nth-child(2) button[value="ozon"]', lambda element: element.click(), "choose ozon")
wait_for_selector('.qualification-dialog__content .v-stepper__content:nth-child(2) .mt-md-5 .v-btn--is-elevated', lambda element: element.click(), "confirm ozon")
# Ввод ФИО и номера телефона
wait_for_selector('.qualification-dialog__content .v-stepper__content:nth-child(2) div[step]:nth-child(3) input[type="tel"]', lambda element: element.send_keys("982 034-83-92"), "Enter number")
wait_for_selector('.qualification-dialog__content .v-stepper__content:nth-child(2) div[step]:nth-child(2) input[type="text"]', lambda element: (element.send_keys("sfdsfds"), element.send_keys(Keys.RETURN)), "Enter name")
# Закрытие приветственного окна
wait_for_selector('.v-application .v-dialog__content .ui-card:nth-child(1) .ui-btn', lambda element: element.click(), "Skip onboarding")

time.sleep(20)
# driver.close()