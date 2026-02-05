from config import setting
import platform
import sys



def create_allure_environment_file():

    items = [f'{key}={value}' for key, value in setting.model_dump().items()]

    properties = '\n'.join(items)

    with open(setting.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
        file.write(sys.version)
        file.write(f'{platform.system()}, {platform.release()}')
