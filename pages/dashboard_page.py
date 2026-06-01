"""
Dashboard page object.
Locators defined as properties for lazy evaluation.
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page object for admin dashboard page."""

    def __init__(self, page: Page, dashboard_url: str = None):
        super().__init__(page)
        self._dashboard_url = dashboard_url

    @property
    def url(self) -> str:
        """Get dashboard URL."""
        return self._dashboard_url or "https://dashboard.portal-sekolah.com/"

    # === LOCATORS (properties for lazy evaluation) ===

    @property
    def txt_dashboard_admin(self) -> Locator:
        return self.page.get_by_text("Admin", exact=True)

    # === ACTIONS ===

    def navigate(self) -> None:
        """Navigate directly to dashboard page."""
        self.page.goto(self.url)

    def verify_admin_dashboard(self) -> None:
        """Verify admin dashboard is visible."""
        self.assert_visible(self.txt_dashboard_admin)

    def get_current_url(self) -> str:
        """Get current dashboard URL."""
        return super().get_current_url()