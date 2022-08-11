"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[{'setup': 'desktop', 'width': 1920, 'height': 1080},
                        {'setup': 'mobile', 'width': 400, 'height': 600}])
def browser_open(request):
    browser.config.window_width = request.param['width']
    browser.config.window_height = request.param['height']
    browser.open('https://github.com/')
    return request.param['setup']


def test_github_desktop(browser_open):
    if browser_open == 'mobile':
        pytest.skip('mobile setup')
    browser.element('a[href="/login"]').click()


def test_github_mobile(browser_open):
    if browser_open == 'desktop':
        pytest.skip('desktop setup')
    browser.element('button[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
