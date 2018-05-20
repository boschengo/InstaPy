import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy


class LikeFollowers:

    def __init__(self, user_to_farming, user_password):
        self.username = user_to_farming
        self.password = user_password
        self.session = None

    def get_session(self):
        self.session = InstaPy(username=self.username, password=self.password, headless_browser=True, multi_logs=True)

    def set_relationship_bounds(self):
        self.session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True,
                                             max_followers=4590, max_following=5555, min_followers=45, min_following=77)

    def do_my_followers_magic(self):
        self.get_session()
        self.set_relationship_bounds()
        try:
            # Interact with the people that a given user is following
            # set_do_comment, set_do_follow and set_do_like are applicable

            self.session.set_user_interact(amount=50, randomize=False, percentage=100, media='Photo')
            self.session.set_do_like(enabled=True, percentage=100)
            self.session.interact_user_followers(self.username, amount=10, randomize=True)

        except Exception as exc:
            # if changes to IG layout, upload the file to help us locate the change
            if isinstance(exc, NoSuchElementException):
                file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
                with open(file_path, 'wb') as fp:
                    fp.write(self.session.browser.page_source.encode('utf8'))
                print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                    '*' * 70, file_path))
            # full stacktrace when raising Github issue
            raise

        finally:
            # end the bot session
            self.session.end()