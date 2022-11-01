from selenium.webdriver.common.by import By

class LoginPageLoc:

    el_username = (By.XPATH, '//*[@id="email"]')
    el_password = (By.XPATH, '//*[@id="passwd"]')
    el_login = (By.XPATH, '//*[@id="SubmitLogin"]')