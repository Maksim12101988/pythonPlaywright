import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://github.com/search/advanced")
    page.get_by_label("Written in this language").select_option("Python")
    page.get_by_placeholder("200, >1000").click()
    page.get_by_placeholder("200, >1000").fill(">20000")
    page.get_by_placeholder("app.rb, footer.erb").click()
    page.get_by_placeholder("app.rb, footer.erb").fill("environment.yml")
    page.locator("#search_form div").filter(has_text="Advanced options From these").get_by_role("button").click()
    expect(page.get_by_test_id("search-sub-header")).to_contain_text("213 results")
