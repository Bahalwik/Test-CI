import pytest

from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage

import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from tools.routes import AppRoute
from config import setting
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
class TestCourses:
    @allure.title('Check display empty courses list')
    @allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
    @allure.epic(AllureEpic.LMS)
    @allure.feature(AllureFeature.COURSES)
    @allure.story(AllureStory.COURSES)
    @allure.severity(Severity.NORMAL)
    @allure.parent_suite(AllureEpic.LMS)
    @allure.suite(AllureFeature.COURSES)
    @allure.sub_suite(AllureStory.COURSES)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(setting.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_empty_courses_view()

    @allure.title('Create correct new course')
    @allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.page.goto(AppRoute.CREATE_COURSES)

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page.create_course_form.check_visible_create_course_form(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercises_button()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(
            setting.test_data.image_png_file)

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill_create_course_form(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible_view(
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10',
            index='0'

        )
