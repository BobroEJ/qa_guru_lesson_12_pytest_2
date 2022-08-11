"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_open(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com/')


@pytest.mark.parametrize('browser_open', [(1920, 1080)], indirect=True)
def test_github_desktop(browser_open):
    browser.element('a[href="/login"]').click()


@pytest.mark.parametrize('browser_open', [(400, 600)], indirect=True)
def test_github_mobile(browser_open):
    browser.element('button[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()

