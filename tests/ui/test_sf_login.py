from pages.sf_login_page import SFLoginPage
import time

class TestSFLogin():

    def test_sf_logincheck(self, page):
        sf_loginpage = SFLoginPage(page)
        sf_loginpage.navigate()
        sf_loginpage.enterUsername()
        sf_loginpage.enterPassword()
        sf_loginpage.clickLogin()
        time.sleep(1)
        sf_loginpage.fillSearchSetup()
