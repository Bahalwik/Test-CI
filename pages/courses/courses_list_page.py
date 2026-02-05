from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.views.empty_view_component import EmptyBarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SideBarComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavBarComponent(page)
        self.sidebar = SideBarComponent(page)

        self.empty_view = EmptyBarComponent(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)

        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_empty_courses_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )


