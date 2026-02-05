import re

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.image import Image
from components.navigation.sidebar_list_item_components import SidebarListItemComponent


class EmptyBarComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Image(page, f'{identifier}-empty-view-icon', 'Image')
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Description')

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
