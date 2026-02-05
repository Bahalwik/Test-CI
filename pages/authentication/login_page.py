from components.authentication.login_form_component import LoginFormComponent
from components.authentication.registration_form_component import RegistrationFormComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from elements.link import Link
from elements.button import Button
from elements.text import Text
import re
import allure


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.registration_form = RegistrationFormComponent(page)

        self.login_button = Button(page, 'login-page-login-button', 'Button')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')

        self.wrong_email_or_password_alert = Text(
            page, 'login-page-wrong-email-or-password-alert', 'Wrong_email_or_password_alert')

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    @allure.step('Check visible wrong_email_or_password_alert')
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')

