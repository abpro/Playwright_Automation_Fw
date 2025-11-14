from playwright.sync_api import Page
from locators.sf_login_page_locators import SFLoginPageLocators
from core.base_page import BasePage

class SFLoginPage(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.locators = SFLoginPageLocators

    def navigate(self):
        self.page.goto("https://orgfarm-d77b32298e-dev-ed.develop.lightning.force.com/")
    
    def enterUsername(self):
        self.page.get_by_label("Username").fill("playwright@testorgappa.com")#playwright@testorgappa.com #ankurbakshi03792@agentforce.com

    def enterPassword(self):
        self.page.get_by_label("Password").fill("Will@1Sales")

    def clickLogin(self):
        self.page.locator("#Login").click()
    
    def fillSearchSetup(self):
        self.page.get_by_placeholder("Search Setup").fill("This is it")

    def enterVerificationCode(self):
        self.page.get_by_label("Verification Code").fill("CSLX34AL2Z")

    def clickVerify(self):
        self.page.get_by_role("button", name="Verify").click()
    
    def isVerificationCodeVisible(self) -> bool:
        return self.page.get_by_label("Verification Code").is_visible()
    

    

