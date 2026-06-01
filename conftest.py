"""
Root conftest.py - Browser, Page, and Page Object fixtures.
All fixtures in one place for simplicity.

Supports multiple browsers via CLI: --browser-type chromium|firefox|webkit
Supports multiple environments via CLI: --env staging|production
"""
import os
import glob
import pytest
import allure
from datetime import datetime
from playwright.sync_api import Browser, BrowserContext, Page

from config.settings import get_settings, Settings
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def _get_run_folder_name() -> str:
    """
    Generate folder name with date_counter format: DDMMYYYY_N
    e.g., 01062026_1, 01062026_2, 02062026_1
    """
    today = datetime.now().strftime("%d%m%Y")
    results_base = "allure-results"

    # Find existing folders for today
    existing = glob.glob(os.path.join(results_base, f"{today}_*"))

    # Extract counter numbers
    counters = []
    for folder in existing:
        try:
            counter = int(folder.split("_")[-1])
            counters.append(counter)
        except ValueError:
            pass

    # Next counter
    next_counter = max(counters, default=0) + 1
    return f"{today}_{next_counter}"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure allure results directory with date_counter folder.
    
    Using tryfirst=True to ensure this runs BEFORE allure-pytest's pytest_configure
    so that config.option.allure_report_dir is set when allure-pytest reads it.
    """
    run_folder = _get_run_folder_name()
    results_dir = os.path.join("allure-results", run_folder)
    os.makedirs(results_dir, exist_ok=True)
    
    # Set the correct attribute that allure-pytest reads (allure_report_dir, not alluredir)
    config.option.allure_report_dir = results_dir


def pytest_addoption(parser):
    """Custom CLI options for pytest."""
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        choices=["staging", "production"],
        help="Environment to test execution: staging, production (default: staging)"
    )
    parser.addoption(
        "--browser-type",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to use: chromium, firefox, webkit (default: chromium)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (default=False)"
    )


@pytest.fixture(scope="session")
def env_name(request) -> str:
    """Get environment name from CLI option."""
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def settings(env_name: str) -> Settings:
    """Get settings for the specified environment."""
    return get_settings(env=env_name)


@pytest.fixture(scope="session")
def browser_type_name(request) -> str:
    """Get browser type from CLI option."""
    return request.config.getoption("--browser-type")


@pytest.fixture(scope="session")
def launched_browser(playwright, browser_type_name: str, request) -> Browser:
    """Launch browser based on CLI option."""
    headless = request.config.getoption("--headless")
    browser_instance = getattr(playwright, browser_type_name)
    return browser_instance.launch(headless=headless)


@pytest.fixture(scope="function")
def browser_context_manager(launched_browser: Browser, settings: Settings) -> BrowserContext:
    """
    Browser context setup - session scope.
    Reuses browser across tests for efficiency.
    """
    context = launched_browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True,
    )
    context.set_default_timeout(settings.TIMEOUT)

    yield context

    context.close()


@pytest.fixture(scope="function")
def page(browser_context_manager) -> Page:
    """
    Page setup - function scope.
    New page for each test for isolation.
    """
    new_page = browser_context_manager.new_page()
    yield new_page
    new_page.close()

# ====================== PAGE OBJECT FIXTURES ============================
@pytest.fixture(scope="function")
def login_page(page: Page, settings: Settings) -> LoginPage:
    """Login page object fixture."""
    return LoginPage(page, base_url=settings.BASE_URL)


@pytest.fixture(scope="function")
def dashboard_page(page: Page, settings: Settings) -> DashboardPage:
    """Dashboard page object fixture."""
    return DashboardPage(page, dashboard_url=settings.DASHBOARD_URL)

# ===========================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and attach screenshots on failure.
    """
    outcome = yield
    rep = outcome.get_result()

    # Only on test failure
    if rep.failed and rep.when == "call":
        # Get page fixture if available
        page = None
        for fixture in item.fixturenames:
            if fixture == "page":
                try:
                    page = item.funcargs[fixture]
                    break
                except (KeyError, AttributeError):
                    pass

        if page is not None:
            try:
                screenshot_dir = "test-results/screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(
                    screenshot_dir,
                    f"{item.name.replace('/', '_')}.png"
                )
                page.screenshot(path=screenshot_path)

                # Attach to Allure report
                with open(screenshot_path, "rb") as f:
                    allure.attach(
                        f.read(),
                        name="Screenshot on Failure",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception:
                pass
