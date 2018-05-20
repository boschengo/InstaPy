from feed_tools import LikeFeedUser
from tags_tools import LikeFollowTags
from like_tools import LikeFollowers
import executor_config
import random
import time


def sleep_to_begin_executions(min_sleep=32, max_sleep=128):
    sleep_time = random.randint(min_sleep, max_sleep)
    print('Waiting {} minutes to start executions...'.format(int(sleep_time/60)))
    time.sleep(sleep_time)
    return


def sleep_between_executions(min_sleep=3, max_sleep=7):
    sleep_time = random.randint(min_sleep, max_sleep)
    print('Waiting {} seconds to continue with other account...'.format(sleep_time))
    time.sleep(sleep_time)
    return


def account_farming(selected_account_var):
    # if random.randint(0, 1):
    like_feed_user = LikeFeedUser(selected_account_var, executor_config.accounts_password)
    like_feed_user.do_feed_magic()
    # if random.randint(0, 1):
    like_feed_user = LikeFollowTags(selected_account_var, executor_config.accounts_password)
    like_feed_user.do_tags_magic()
    # if random.randint(0, 1):
    #     like_feed_user = LikeFollowers(selected_account_var, executor_config.accounts_password)
    #     like_feed_user.do_my_followers_magic()

    print('Account {} farming finished.'.format(selected_account_var))
    return


if __name__ == "__main__":
    iteration_counter = 0
    sleep_to_begin_executions()
    accounts_execution = executor_config.get_accounts_for_farming()
    for selected_account in accounts_execution:
        account_farming(selected_account)
        sleep_between_executions()
