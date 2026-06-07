"""
Base page with assertion helpers only.
No wrapping of native Playwright action methods (click, fill, etc.) since Playwright already has built-in auto-wait.
"""
from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # === ASSERTION HELPERS (with Allure integration) ===
    def assert_visible(self, locator: Locator, timeout: int = None) -> None:
        """Assert element is visible."""
        expect(locator).to_be_visible(timeout=timeout)

    def assert_hidden(self, locator: Locator, timeout: int = None) -> None:
        """Assert element is hidden."""
        expect(locator).to_be_hidden(timeout=timeout)

    def assert_enabled(self, locator: Locator, timeout: int = None) -> None:
        """Assert element is enabled."""
        expect(locator).to_be_enabled(timeout=timeout)

    def assert_disabled(self, locator: Locator, timeout: int = None) -> None:
        """Assert element is disabled."""
        expect(locator).to_be_disabled(timeout=timeout)

    def assert_contains_text(self, locator: Locator, expected: str, timeout: int = None) -> None:
        """Assert element contains expected text."""
        expect(locator).to_contain_text(expected, timeout=timeout)

    def assert_has_text(self, locator: Locator, expected: str, timeout: int = None) -> None:
        """Assert element has exact text."""
        expect(locator).to_have_text(expected, timeout=timeout)

    def assert_url_contains(self, expected: str, timeout: int = None) -> None:
        """Assert current URL contains expected string."""
        expect(self.page).to_have_url(f"*{expected}*", timeout=timeout)

    def assert_url_matches(self, pattern: str, timeout: int = None) -> None:
        """Assert current URL matches pattern."""
        expect(self.page).to_have_url(pattern, timeout=timeout)

    def assert_title_contains(self, expected: str, timeout: int = None) -> None:
        """Assert page title contains expected string."""
        expect(self.page).to_have_title(f".*{expected}.*", timeout=timeout)

    def assert_count(self, locator: Locator, expected: int, timeout: int = None) -> None:
        """Assert element count."""
        expect(locator).to_have_count(expected, timeout=timeout)

    # === UTILITY HELPERS ===

    def wait_for_url(self, pattern: str, timeout: int = None) -> None:
        """Wait for URL to match pattern."""
        self.page.wait_for_url(pattern, timeout=timeout)

    def wait_for_load_state(self, state: str = "load") -> None:
        """Wait for page load state."""
        self.page.wait_for_load_state(state)

    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.page.url

    def get_page_title(self) -> str:
        """Get page title."""
        return self.page.title()

    def get_text(self, locator: Locator) -> str:
        """Get element text content."""
        return locator.text_content() or ""

    def is_visible(self, locator: Locator) -> bool:
        """Check if element is visible."""
        return locator.is_visible()

    def is_enabled(self, locator: Locator) -> bool:
        """Check if element is enabled."""
        return locator.is_enabled()

    def scroll_into_view(self, locator: Locator) -> None:
        """Scroll element into view."""
        locator.scroll_into_view_if_needed()

    def press_enter(self, locator: Locator) -> None:
        """Press Enter on element."""
        locator.wait_for(state="visible")
        locator.focus()
        self.page.keyboard.press("Enter")