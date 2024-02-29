import os
import time
from lib2to3.pgen2 import driver

import pytest as pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.get(url)
    # driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def pytest_html_report_title(report):
#     report.title = "RCV Academy Automation Report"


    # driver = webdriver.Chrome()
    # # wait = WebDriverWait(driver, 10)
    # driver.get("https://www.yatra.com/")
    # driver.maximize_window()
    # request.cls.driver = driver
    # # request.cls.wait = wait
    # yield
    # driver.close()
