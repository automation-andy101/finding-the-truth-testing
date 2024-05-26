from config.config import get_driver

def before_all(context):
    context.driver = get_driver()

def after_all(context):
    context.driver.quit()
