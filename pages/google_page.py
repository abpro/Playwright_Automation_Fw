from playwright.sync_api import Page
from core.base_page import BasePage

class GooglePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        # reuse BasePage.navigate
        self.navigate("https://www.google.com")

    def search(self, query: str):
        self.search_input.fill(query)
        # pressing Enter is more reliable than clicking the hidden button
        self.search_input.press("Enter")
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        # demonstrate calling the inherited method
        return super().get_title()
    
    def goToAboutPage(self):
        self.page.get_by_role("link", name="About", exact=True).click()
    
    def googleLogo(self) -> bool:
        return self.page.get_by_role("link", name="Google logo", exact=True).is_visible()