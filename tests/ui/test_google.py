from pages.google_page import GooglePage


class TestGoogle:

    def test_open_google(self, page):
        google_page = GooglePage(page)
        google_page.navigate()
        
        # Verify Google text is present
        assert google_page.verify_google_text_present(), "Google text not found on page"
        
        print("✅ Test Passed: 'Google' text found on page")