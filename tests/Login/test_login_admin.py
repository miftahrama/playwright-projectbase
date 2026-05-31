from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utils.data_generator import generate_user_registration_data

def test_login_admin_success(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.pilih_sekolah(teks_pencarian="smp - q", nama_sekolah_pilihan="SMP - QA Demo School")
    login.login_user("adminsmp.123", "password123*")
    dashboard.verify_dashboard_admin()
