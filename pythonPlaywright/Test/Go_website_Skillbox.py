import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://skillbox.ru/code/", timeout=60000)
    page.locator("label").filter(has_text="Профессия").locator("span").click()
    page.locator(".ui-range").click()
    page.locator("span").filter(has_text="1С").nth(1).click()
    expect(page.get_by_role("main")).to_contain_text("Профессии (2)")


