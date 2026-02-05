import pytest

from pages.authentication.login_page import LoginPage
import allure

from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from config import setting
from tools.routes import AppRoute
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestRegistration:
    @allure.severity(Severity.CRITICAL)
    @allure.title('User registration with correct email, username and password')
    def test_successful_registration(self, login_page: LoginPage):
        login_page.page.goto(AppRoute.REGISTRATION)

        login_page.registration_form.fill_register_form(
            email=setting.test_user.email, username=setting.test_user.username, password=setting.test_user.password
        )

        login_page.registration_form.check_visible(
            email=setting.test_user.email, username=setting.test_user.username, password=setting.test_user.password
        )

        registration_button = login_page.page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

