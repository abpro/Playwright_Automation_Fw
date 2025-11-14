from pages.sf_login_page import SFLoginPage
import time

class TestSFLogin():

    def test_sf_logincheck(self, page):
        sf_loginpage = SFLoginPage(page)
        sf_loginpage.navigate()
        sf_loginpage.enterUsername()
        sf_loginpage.enterPassword()
        sf_loginpage.clickLogin()
        if(sf_loginpage.isVerificationCodeVisible()):
            sf_loginpage.enterVerificationCode()
            sf_loginpage.clickVerify()
        sf_loginpage.pauseThePage(page) #CSLX34AL2Z
       # sf_loginpage.fillSearchSetup()
