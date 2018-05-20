import os
import time
import executor_config
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy


class LikeFollowTags:

    def __init__(self, user_to_farming, user_password):
        self.target_tags = executor_config.get_tags_for_farming()
        self.username = user_to_farming
        self.password = user_password
        self.session = None

    def get_session(self):
        self.session = InstaPy(username=self.username, password=self.password, headless_browser=False, multi_logs=True)

    def set_relationship_bounds(self):
        self.session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True,
                                             max_followers=4590, max_following=5555, min_followers=45, min_following=77)

    def do_tags_magic(self):
        self.get_session()
        self.set_relationship_bounds()
        try:
            self.session.login()

            # follow_by_tags
            self.session.follow_by_tags(self.target_tags, amount=15, skip_top_posts=True, use_smart_hashtags=False)

            # like by tags
            self.session.set_delimit_liking(enabled=True, max=1005, min=20)
            self.session.set_user_interact(amount=5, randomize=True, percentage=70, media='Photo')
            self.session.like_by_tags(self.target_tags, amount=15, interact=True)

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
