from page.DemoPage import DemoPage


class TestUi:
    def test_ui(self, browser):
        browser.get("https://www.qafeast.com/demo")
        demo = DemoPage(browser)
        demo.textbox("test_data")
        demo.login("test_data")
