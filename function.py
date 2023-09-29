from playwright.sync_api import sync_playwright
def capture_first_post_screenshot():
    url = 'https://kun.uz/news/category/jahon'
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        # Log in to your Instagram account
        page.wait_for_timeout(7000)

        # Go to your profile page
        profile_url = 'https://kun.uz/news/category/jahon'
        page.goto(profile_url)
        page.get_by_text('big-news_title')

        page.wait_for_timeout(3000)
        screenshot = page.screenshot(path='first_post_screenshot.png')
        browser.close()

    return screenshot


# Capture the screenshot
capture_first_post_screenshot()