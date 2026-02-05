from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyBarComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_empty_view = EmptyBarComponent(page, identifier='create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)

        self.exercises_title = page.get_by_test_id(
            'create-course-exercises-box-toolbar-title-text')
        self.exercises_button = page.get_by_test_id(
            'create-course-exercises-box-toolbar-create-exercise-button')


    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()

    def check_visible_create_exercises_button(self):
        expect(self.exercises_button).to_be_visible()

    def click_create_exercises_button(self):
        self.exercises_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise'
        )
