"""
Login test cases.
Clean and readable with minimal Allure decorators.
Steps are implicit through page object method names.
"""
import allure
import pytest

from config.settings import Settings


@allure.feature("Login")
class TestLogin:
    """Login feature test suite."""

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_admin_success(self, login_page, dashboard_page, settings: Settings):
        """
        Test successful admin login.
        Verify user can login with valid credentials and see dashboard.
        """
        login_page.navigate()
        login_page.select_school(
            settings.DEFAULT_SCHOOL_SEARCH,
            settings.DEFAULT_SCHOOL_NAME
        )
        login_page.login(settings.DEFAULT_USERNAME, settings.DEFAULT_PASSWORD)
        dashboard_page.verify_admin_dashboard()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_invalid_credentials(self, login_page):
        """
        Test login with invalid credentials.
        Verify error handling for wrong username/password.
        """
        login_page.navigate()
        login_page.select_school(
            "smp - q",
            "SMP - QA Demo School"
        )
        login_page.login("wrong_user", "wrong_password")
        login_page.verify_error_message()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_empty_fields(self, login_page):
        """
        Test login with empty fields.
        Verify validation for empty username/password.
        """
        login_page.navigate()
        login_page.select_school(
            "smp - q",
            "SMP - QA Demo School"
        )
        login_page.login("", "")
        login_page.verify_error_message()