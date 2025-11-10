from playwright.sync_api import Page
from locators.sf_login_page_locators import SFLoginPageLocators
from core import base_page

class SFLoginPage():

    def __init__(self, page: Page):
        self.page = page
        self.locators = SFLoginPageLocators

    def navigate(self):
        self.page.goto("https://orgfarm-d77b32298e-dev-ed.develop.lightning.force.com/")
    
    def enterUsername(self):
        self.page.get_by_label("Username").fill("ankurbakshi03792@agentforce.com")

    def enterPassword(self):
        self.page.get_by_label("Password").fill("Will@1Sales")

    def clickLogin(self):
        self.page.locator("#Login").click()
    
    def fillSearchSetup(self):
        self.page.get_by_placeholder("Search Setup").fill("This is it")
    

