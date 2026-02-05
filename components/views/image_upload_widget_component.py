from typing import Pattern
import re
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.views.empty_view_component import EmptyBarComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyBarComponent(page, identifier)


        self.preview_course_image = page.get_by_test_id(
            f'{identifier}-image-upload-widget-preview-image')

        self.info_preview_image_icon = page.get_by_test_id(
            f'{identifier}-image-upload-widget-info-icon')
        self.info_preview_image_title = page.get_by_test_id(
            f'{identifier}-image-upload-widget-info-title-text')
        self.info_preview_image_description = page.get_by_test_id(
            f'{identifier}-image-upload-widget-info-description-text')

        self.delete_info_image_button = page.get_by_test_id(
            f'{identifier}-image-upload-widget-remove-button')
        self.info_preview_image_upload = page.get_by_test_id(
            f'{identifier}-image-upload-widget-upload-button')
        self.upload_info_image_button = page.get_by_test_id(
            f'{identifier}-image-upload-widget-input')

    def check_visible(
            self,
            is_image_uploaded: bool = False
    ):
        expect(self.info_preview_image_upload).to_be_visible()

        expect(self.info_preview_image_title).to_be_visible()
        expect(self.info_preview_image_title).to_have_text(
            'Tap on "Upload image" button to select file')

        expect(self.info_preview_image_description).to_be_visible()
        expect(self.info_preview_image_description).to_have_text(
            "Recommended file size 540X300")

        if is_image_uploaded:
            expect(self.delete_info_image_button).to_be_visible()
            expect(self.preview_course_image).to_be_visible()
        else:
            self.preview_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here"
            )

    def click_delete_image_button(self):
        self.delete_info_image_button.click()

    def upload_preview_image(self, file: str):
        self.upload_info_image_button.set_input_files(file)
