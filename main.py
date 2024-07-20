# Third-Party
from decouple import config

# Local
from src.photo import ActionsWithPhoto


POST = config("POST")
REEL = config("REEL")


def main_with_photo():
    photo = ActionsWithPhoto()
    driver = photo.login_instagram()
    try:
        photo.get_action(
            driver=driver, action="Comment", post_or_reel=POST
        )
        driver.quit()
        print("SUCCESS")
    finally:
        driver.quit()


if __name__ == "__main__":
    main_with_photo()
