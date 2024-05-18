from openpyxl import load_workbook
import pytest

from orangeframework.pages import login_page
from orangeframework.utilities.excel_util import read_from_excel
from orangeframework.utilities.excel_util import write_to_excel
from orangeframework.utilities.selenium_utils import verify_if_login_success


# Parametrize is used to pass multiple sets of arguments to test function
# allowing the test to run with different input data
@pytest.mark.parametrize("test_id, username, password", read_from_excel(
    "C://Ramya//Workspace//Python//Tasks//Task-12_27Apr24//orangeframework//credential_data//test_result_orange.XLSX"))
def test_login(driver, test_id, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    login_page_instance = login_page.Login_Page(driver)
    login_successful = login_page_instance.login(username, password)


    # Result of login function is stored and returned in variable login_successful
    # and write_to_excel function is called
    test_result = "Test Passed" if login_successful else "Test Failed"
    write_to_excel(
        "C://Ramya//Workspace//Python//Tasks//Task-12_27Apr24//orangeframework//credential_data//test_result_orange.XLSX",
        [test_id, username, password], test_result)
