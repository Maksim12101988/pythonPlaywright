import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://github.com/microsoft/vscode/graphs/commit-activity")

    # Наводим курсор на график
    graph_element = page.locator("#commit-activity-master > svg > g > g.bar.mini.active > rect")
    graph_element.hover()

    # Ожидаем появления тултипа
    tooltip_selector = ".svg-tip.n *"
    page.locator(tooltip_selector).wait_for(timeout=15000)  # Ожидаем 15 секунд



"""
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://github.com/microsoft/vscode/graphs/commit-activity")
    expect(page.locator("rect").first).to_be_visible()
"""








