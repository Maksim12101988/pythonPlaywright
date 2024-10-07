import re
from playwright.sync_api import Page, expect


def get_issue_titles(page):
    # Получаем все элементы списка задач
    elements = page.query_selector_all('.js-navigation-item')

    # Создаем список названий задач
    titles = []

    # Проходим по каждому элементу списка
    for element in elements:
        title_element = element.query_selector('.js-navigation-item-title')
        if title_element:
            title = title_element.inner_text()
            titles.append(title.strip())

    return titles


def check_bug_in_title(title):
    return re.search(r'\bbug\b', title, re.IGNORECASE) is not None


def test_example(page: Page) -> None:
    page.goto("https://github.com/microsoft/vscode/issues")

    # Нажимаем на поле поиска
    page.get_by_placeholder("Search all issues").click()

    # Вводим поиск
    page.get_by_placeholder("Search all issues").fill("is:issue is:open bag")


    page.get_by_placeholder("Search all issues").press("Enter")

    # Ждем, пока страница загрузится
    page.wait_for_load_state("networkidle")

    # Получаем все названия задач
    issue_titles = get_issue_titles(page)

    print("Все названия задач:")
    for title in issue_titles:
        print(title)

    # Проверяем, что каждая задача содержит слово "bug" (не регистронезависимо)
    bug_count = sum(check_bug_in_title(title) for title in issue_titles)
    total_issues = len(issue_titles)

    assert bug_count == total_issues, f"Ожидалось, что все {total_issues} задачи содержат слово \"bug\", но найдено только {bug_count}"

