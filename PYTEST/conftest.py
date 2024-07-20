#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

driver = None

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver_path = "D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
        service_object = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service_object)
    elif browser_name == "firefox":
        driver_path = "D:\\Selenium_Training\\drivers\\geckodriver-v0.34.0-win-aarch64 (1)\\geckodriver.exe"
        service_object = Service(executable_path=driver_path)
        driver = webdriver.Firefox(service=service_object)
    else:
        driver_path = "D:\\Selenium_Training\\drivers\\msedgedriver.exe"
        service_object = Service(executable_path=driver_path)
        driver = webdriver.Edge(service=service_object)

    driver.implicitly_wait(5)
    url = "https://rahulshettyacademy.com/angularpractice/"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


#--------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



