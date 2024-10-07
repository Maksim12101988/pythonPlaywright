import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://github.com/microsoft/vscode/issues")
    page.get_by_role("button", name="Author").click()
    page.get_by_role("textbox", name="Filter users").click()
    page.get_by_role("textbox", name="Filter users").click()
    page.get_by_role("textbox", name="Filter users").fill("bpasero")
    page.get_by_role("menuitemradio", name="@bpasero bpasero Benjamin").click()
    expect(page.locator("#js-issues-toolbar")).to_contain_text("302 Open")

