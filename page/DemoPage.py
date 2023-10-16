from selenium.webdriver.common.by import By


class DemoPage:
    def __init__(self, driver):
        self.driver = driver

    def textbox(self, testdata):
        # Click Text box tab
        self.driver.find_element(By.XPATH, "//label[text() = 'Textbox']").click()
        # Enter the text in to the text box
        self.driver.find_element(By.XPATH, "(//input[@id='editabletext'])[1]").send_keys(testdata)

    def login(self, testdata):
        # Click Text box tab
        self.driver.find_element(By.XPATH, "//label[text() = 'Scrolling']").click()
        # Enter the text in to the text box
        self.driver.find_element(By.ID, "username").send_keys(testdata)
