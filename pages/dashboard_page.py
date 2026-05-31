from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # ---- STATIC OBJECT LOCATOR ----
        self.url_dashboard_admin = "https://dashboard.portal-sekolah.com/"
        self.txt_dashboard_admin = page.get_by_text("Admin", exact=True)


    # ---- DYNAMIC OBJECT LOCATOR ----


    # ---- ACTION / METHOD ----
    def navigate(self):
        self.page.goto(self.url_dashboard_admin)

    def verify_dashboard_admin(self):
        expect(self.txt_dashboard_admin).to_be_visible()