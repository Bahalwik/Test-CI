from playwright.sync_api import sync_playwright, expect, Page, Playwright
import pytest
import allure
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType

from tools.playwright.pages import initialize_playwright_page
from config import setting, Browser
from tools.routes import AppRoute


@pytest.fixture(params=setting.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param

    )

    # browser = playwright.chromium.launch(headless=False)
    #
    # context = browser.new_context(record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()
    #
    # allure.attach.file(
    #     f'./tracing/{request.node.name}.zip',
    #     name='trace',
    #     extension='zip'
    # )
    #
    # allure.attach.file(
    #     page.video.path(),
    #     name='video',
    #     attachment_type=allure.attachment_type.WEBM
    #     #attachment_type = AttachmentType.WEBM
    # )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(base_url=setting.get_base_url())

    page = context.new_page()

    registration_page = RegistrationPage(page=page)

    registration_page.visit(AppRoute.REGISTRATION)

    registration_page.registration_form.fill_register_form(
        email=setting.test_user.email,
        username=setting.test_user.username,
        password=setting.test_user.password
    )
    registration_page.click_registration_button()
    context.storage_state(path=setting.browser_state_file)
    browser.close()


@pytest.fixture(params=setting.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright):

    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=setting.browser_state_file,
        browser_type=request.param
    )


    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(storage_state='browser-state.json', record_video_dir='./videos')
    #
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    #
    # browser.close()
    #
    # allure.attach.file(
    #     f'./tracing/{request.node.name}.zip',
    #     name='trace',
    #     extension='zip'
    # )
    #
    # allure.attach.file(
    #     page.video.path(),
    #     name='video',
    #     attachment_type=allure.attachment_type.WEBM
    # )
