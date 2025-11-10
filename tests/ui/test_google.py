from pages.google_page import GooglePage


class TestGoogle:

    def test_open_google(self, page):
       gp = GooglePage(page)   
       gp.open()
       gp.get_title()
       assert "Google" in page.text_content("body")
       print("✅ Test Passed: 'Google' text found on page")