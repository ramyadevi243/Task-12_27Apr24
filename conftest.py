import pytest
from selenium import webdriver


# Fixture is created and destroyed once per session.
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
