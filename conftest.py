import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(params=["chrome"], scope="function")
def browser(request):
    global driver
    print("Browser name - - - - ")
    # invoke driver object
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()
    request.instance.driver = driver

    yield driver

    def teardown():
        print('Function Tear down - - - - ')
        driver.close()

    request.addfinalizer(teardown)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    print("In make report ")
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever tests fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir + '/screenshots/')
    if report.when == 'call' or report.when == "setup":
        file_name = report.nodeid.replace("::", "_") + ".png"
        file_name = file_name.replace('tests/', '')
        _capture_screenshot(file_name)
        if file_name:
            html = file_path + file_name
            extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir + '/screenshots/')
    driver.get_screenshot_as_file(file_name + name)
