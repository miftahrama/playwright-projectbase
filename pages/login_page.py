"""
Login page object.
Locators defined as properties for lazy evaluation.
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for login page."""

    def __init__(self, page: Page, base_url: str = None):
        super().__init__(page)
        self._base_url = base_url

    @property
    def url(self) -> str:
        """Get login page URL."""
        return self._base_url or "https://portal-sekolah.com"

    # === LOCATORS (properties for lazy evaluation) ===

    @property
    def btn_masuk_awal(self) -> Locator:
        return self.page.get_by_role("button", name="Masuk").first

    @property
    def dropdown_sekolah(self) -> Locator:
        return self.page.get_by_role("combobox", name="Sekolah")

    @property
    def input_username(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username")

    @property
    def input_password(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def btn_masuk(self) -> Locator:
        return self.page.get_by_role("button", name="Masuk", exact=True)

    @property
    def txt_dashboard_admin(self) -> Locator:
        return self.page.get_by_text("Admin", exact=True)

    def get_pilihan_sekolah_locator(self, nama_sekolah: str) -> Locator:
        """Get locator for school option by name."""
        return self.page.get_by_text(nama_sekolah)

    # === ACTIONS ===

    def navigate(self) -> None:
        """Navigate to login page."""
        self.page.goto(self.url)

    def select_school(self, search_text: str, school_name: str) -> None:
        """Select school from dropdown."""
        self.dropdown_sekolah.click()
        self.dropdown_sekolah.fill(search_text)
        self.get_pilihan_sekolah_locator(school_name).click()

    def login(self, username: str, password: str) -> None:
        """Fill login form and submit."""
        self.btn_masuk_awal.click()
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.btn_masuk.click()

    def verify_error_message(self) -> None:
        """Verify error message is visible (for failed login)."""
        error_locator = self.page.get_by_text("Error")
        self.assert_visible(error_locator)