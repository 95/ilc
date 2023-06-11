from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import asyncio
import time
from selenium.webdriver.common.keys import Keys

async def show_loading_screen(driver):
    while driver.current_url == "https://discord.com/login":
        loading_text = "Logging in"
        for i in range(3):
            print(loading_text + "." * (i+1), end='\r')
            await asyncio.sleep(1)

async def check_captcha_presence(driver):
    while driver.current_url == "https://discord.com/login":
        try:
            captchaPresent = await asyncio.to_thread(driver.find_element, By.XPATH, "//*[text()='Wait! Are you human?']")
        except NoSuchElementException:
            captchaPresent = None

        if captchaPresent:
            print("Captcha is present. Please solve it before continuing\n")
            await asyncio.sleep(5)

async def logged_in(driver):
    if driver.current_url == "https://discord.com/channels/@me":
        try:
            settings = await asyncio.to_thread(driver.find_element, By.CSS_SELECTOR, 'button[aria-label="User Settings"]')
        except NoSuchElementException:
            settings = None

        if settings:
            settings.click()
            await asyncio.sleep(3)

async def check_for_update(driver):
    await asyncio.sleep(3)
    editButton = await asyncio.to_thread(driver.find_element, By.CSS_SELECTOR, 'button[aria-label="Edit Username"]')
    editButton.click()
    while True:
        try:
            discriminatorButton = await asyncio.to_thread(driver.find_element, By.CSS_SELECTOR, 'button[aria-label="Discriminator"]')
            await asyncio.sleep(10)
        except NoSuchElementException:
            settings = None
            print("update has been released")
            break

async def main():
    email = 'sparrbodman3@hotmail.com'
    password = 'eW61Qq45'

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://discord.com/login")

    emailForm = driver.find_element(By.NAME, "email")
    passwordsForm = driver.find_element(By.NAME, "password")
    emailForm.send_keys(email)
    passwordsForm.send_keys(password)
    passwordsForm.send_keys(Keys.ENTER)

    await show_loading_screen(driver)
    await check_captcha_presence(driver)
    await logged_in(driver)
    await check_for_update(driver)

    # Close the browser
    driver.quit()

# Run the main function
asyncio.run(main())
