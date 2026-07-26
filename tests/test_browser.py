from utils.driver import create_driver


def test_open_starproperty():
    driver = create_driver()

    try:
        driver.get("https://www.starproperty.my/")

        logger.info("Website opened successfully")

    finally:
        driver.quit()