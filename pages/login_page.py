from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Locator Creation Guidelines:

    - Do Not create locator under __init__ constructor method (for ram optimize purpose)
    - Create locator with basic python method(without @property decorator) if your locator needs dynamic parameters.
    - Create locator with lazy evaluation locator style(basic python method + @property decorator) if your locator no need dynamic parameters.

    """

    # === CONSTRUCTOR ===
    def __init__(self, page: Page, base_url):
        super().__init__(page)
        self.login_url = f'{base_url}/login'

    # === PAGE LOCATORS ===
    @property
    def btn_masuk_landing_page(self) -> Locator:
        return self.page.get_by_role("button", name="Masuk").first

    @property
    def school_dropdown(self) -> Locator:
        return self.page.get_by_role("combobox", name="Sekolah")

    def school_option_list(self, nama_sekolah: str) -> Locator:
        """Get locator for school option by school name."""
        return self.page.get_by_text(nama_sekolah)

    @property
    def username_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username")

    @property
    def password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def btn_masuk(self) -> Locator:
        return self.page.get_by_role("button", name="Masuk", exact=True)

    # === PAGE ACTIONS(METHOD) ===
    def navigate(self):
        """Navigate to login page."""
        self.page.goto(self.login_url)

    def select_school(self, school_name):
        """Select school from dropdown."""
        self.school_dropdown.fill(school_name)
        self.school_option_list(school_name).click()

    def user_login(self, schoolname, username, password):
        self.btn_masuk_landing_page.click()
        self.school_dropdown.click()
        self.press_backspace(self.school_dropdown)
        self.select_school(schoolname)
        # self.school_dropdown.fill(schoolname)
        # self.school_option_list(schoolname).click()
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.btn_masuk.click()