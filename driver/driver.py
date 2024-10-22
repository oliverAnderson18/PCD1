# from selenium.webdriver import Firefox
from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service

from config import PROXY_URL

Driver = Chrome
Options = ChromeOptions


def create_webdriver_options(
        is_headless=True
) -> Options:
    options = Options()
    if is_headless:
        options.add_argument("--headless")

    options.add_argument(f"--proxy-url={PROXY_URL}")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options


def create_webdriver(
        options: Options | None = None,
) -> Driver:
    if options is None:
        options = create_webdriver_options()
    driver = Driver(
        options=options,
        service=Service(executable_path="C:/Users/oliga/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"),
    )
    return driver


