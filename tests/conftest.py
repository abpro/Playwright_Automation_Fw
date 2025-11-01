import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments"""
    return {
        "headless": False,  # Set to True for CI/CD
        "slow_mo": 500      # Slow down by 500ms for visibility
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments"""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True
    }


@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
