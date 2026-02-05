import allure


def test_feature123():
    with allure.step("Opening browser"):
        ...  # Тут код открытия браузера

    with allure.step("Creating course"):
        ...  # Тут код создания курса

    with allure.step("Closing browser"):
        ...  # Тут код закрытия браузера


@allure.step("Opening browser")
def open_browser():
    ...


@allure.step("Creating course")
def create_course():
    ...


@allure.step("Closing browser")
def close_browser():
    ...


def test_feature():
    open_browser()
    create_course()
    close_browser()






@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_feature22():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")