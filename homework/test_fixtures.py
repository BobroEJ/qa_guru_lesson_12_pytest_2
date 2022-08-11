"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture()
def for_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')


@pytest.fixture()
def for_mobile():
    browser.config.window_width = 400
    browser.config.window_height = 600
    browser.open('https://github.com/')


def test_github_desktop(for_desktop):
    browser.element('a[href="/login"]').click()


def test_github_mobile(for_mobile):
    browser.element('button[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
