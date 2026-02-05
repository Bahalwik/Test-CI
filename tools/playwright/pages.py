from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest
import allure
from config import setting, Browser
from tools.playwright.mocks import mock_static_resources


def initialize_playwright_page(
        playwright: Playwright,
        browser_type: Browser,
        test_name: str,
        storage_state: str | None = None
        ) -> Page:

    browser = playwright[browser_type].launch(headless=setting.headless)

    context = browser.new_context(base_url=setting.get_base_url(),
                                  storage_state=storage_state,
                                  record_video_dir=setting.videos_dir)

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    mock_static_resources(page)

    yield page

    context.tracing.stop(path=setting.tracing_dir.joinpath(f'{test_name}.zip'))

    browser.close()

    allure.attach.file(
        setting.tracing_dir.joinpath(f'{test_name}.zip'),
        name='trace',
        extension='zip'
    )

    allure.attach.file(
        page.video.path(),
        name='video',
        attachment_type=allure.attachment_type.WEBM
    )