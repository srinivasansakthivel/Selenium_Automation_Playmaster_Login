import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--url", action="store", default="staging"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Softwares\\ChromeDriver\\chromedriver_win32_91version\\chromedriver.exe", options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Softwares\\GeckoDriver\\geckodriver.exe", options=firefox_options)
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\Softwares\\IEDriver\\IEDriverServer.exe")
    if url == 'staging':
        url = "https://stg-skillmaster-web.np.logitech.io/"
    elif url == 'production':
        url = "https://playmaster.gg/"
    driver.maximize_window()
    driver.get(url)
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
