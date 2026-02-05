import pytest

from pages.dashboard.dashboard_page import DashboardListPage
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature

from allure_commons.types import Severity
from config import setting
from tools.routes import AppRoute

@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.severity(Severity.NORMAL)
    @allure.title('Check displaying of dashboard page')
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardListPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(setting.test_user.username)

        dashboard_page_with_state.check_visible_dashboard_title()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_activities_chart()
        dashboard_page_with_state.check_visible_students_chart()
