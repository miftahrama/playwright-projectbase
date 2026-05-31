from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # ---- STATIC OBJECT LOCATOR ----
        self.url_login = "https://portal-sekolah.com"
        self.btn_masuk_awal = page.get_by_role("button", name="Masuk").first
        self.dropdown_sekolah = page.get_by_role("combobox", name="Sekolah")
        self.input_username = page.get_by_role("textbox", name="Username")
        self.input_password = page.get_by_role("textbox", name="Password")
        self.btn_masuk = page.get_by_role("button", name="Masuk", exact=True)
        self.txt_dashboard_admin = page.get_by_text("Admin", exact=True)

    # ---- DYNAMIC OBJECT LOCATOR ----
    def get_pilihan_sekolah_locator(self, nama_sekolah: str):
        return self.page.get_by_text(nama_sekolah)

    # ---- ACTION / METHOD ----
    def navigate(self):
        self.page.goto(self.url_login)

    def pilih_sekolah(self, teks_pencarian: str, nama_sekolah_pilihan: str):
        self.dropdown_sekolah.click()
        self.dropdown_sekolah.fill(teks_pencarian)
        self.get_pilihan_sekolah_locator(nama_sekolah_pilihan).click()

    def login_user(self, username: str, password: str):
        self.btn_masuk_awal.click()
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.btn_masuk.click()

