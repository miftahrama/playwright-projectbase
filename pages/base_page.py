from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def press_enter(self, locator: Locator) -> None:
        locator.wait_for(state="visible")
        locator.focus()
        self.page.keyboard.press("Enter")

    def scroll_to_element_and_click(self, locator: Locator) -> None:
        locator.wait_for(state="attached")
        locator.evaluate("element => element.scrollIntoView({block: 'center', behavior: 'smooth'})")
        locator.wait_for(state="visible")
        locator.click()
