"""
Login test cases.
Clean and readable with minimal Allure decorators. Only give allure severity Critical only if that critical scenario, if it's not critical do not provide any decorator.
Steps are implicit through page object method names.
"""
import allure
from config.settings import settings as td


@allure.feature("Login")
class TestLoginAdmin:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_admin_success(self, login_page, dashboard_page):
        login_page.navigate()
        login_page.user_login(schoolname=td.DEFAULT_SCHOOL_NAME, username=td.DEFAULT_USERNAME, password=td.DEFAULT_PASSWORD)
        dashboard_page.verify_admin_dashboard()