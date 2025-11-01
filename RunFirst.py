from playwright.sync_api import sync_playwright


def test_open_google():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        
        # Open new page
        page = browser.new_page()
        
        # Go to Google
        page.goto("https://www.google.com")
        
        # Wait 3 seconds so you can see it
        page.wait_for_timeout(3000)
        
        # Close
        browser.close()
        
        print("✅ Success! Playwright is working.")


if __name__ == "__main__":
    test_open_google()