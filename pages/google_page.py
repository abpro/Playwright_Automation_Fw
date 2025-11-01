from playwright.sync_api import Page
from locators.google_home_page_locators import GoogleHomePageLocators

class GooglePage:

    def __init__(self,page : Page):
        self.page = page
        self.locators = GoogleHomePageLocators()

    def navigate(self):
        self.page.goto("https://www.google.com")
    
    def get_page_title(self) -> str:
        return self.page.title()
    
    def verify_google_text_present(self) -> bool:
        content = self.page.content()
        return "Google" in content