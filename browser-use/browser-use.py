import asyncio
from browser_use import Browser
import time

async def main():
    # Initialize browser
    browser = Browser()

    # Await the async call to get playwright browser instance
    playwright_browser = await browser.get_playwright_browser()

    # Create a new context and page (await the coroutines)
    context = await playwright_browser.new_context()
    page = await context.new_page()

    # Navigate to the index.html page (await the coroutine)
    await page.goto("file:///C:/browser-use/index.html")  # update path

    # Fill the text box and click button to navigate
    await page.fill("input#textbox", "Some text here")
    await page.click("button[id='btn']")

    # Wait for the next page to load (you can also wait for a selector to appear)
    await page.wait_for_selector("input#checkbox")

    # Click the checkbox and submit button
    await page.click("input#checkbox")
    await page.click("button[id='btnsts']")

    # Get the message text
    message = await page.inner_text("span#message")
    print(message)

    time.sleep(20)
    # Close context and browser
    await context.close()
    await browser.close()

# Run the async main
asyncio.run(main())
