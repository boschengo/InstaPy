import random

farming_accounts = ['nidalonso', 'nidalonso']
accounts_password = 'Thebotproject'

followers_target_account = ['matiasabat', 'guido_dellarosa']
farming_tags = ['love', 'instagood', 'photooftheday', 'beautiful', 'happy', 'cute', 'me', 'picoftheday',
                'friends', 'girl', 'fun', 'smile']


def get_quantity_executions(accounts_ratio=0.70):
    print('Ratio to select accounts: {}'.format(accounts_ratio))
    return int(len(farming_accounts) * accounts_ratio)


def get_accounts_for_farming():
    accounts_counter = 0
    selected_accounts_var = []
    quantity_executions = get_quantity_executions()
    while accounts_counter < quantity_executions:
        selected_account_var = random.choice(farming_accounts)
        selected_accounts_var.append(selected_account_var)
        farming_accounts.remove(selected_account_var)
        accounts_counter = accounts_counter + 1
    print('Selected accounts: {}'.format(selected_accounts_var))
    return selected_accounts_var


def get_tags_for_farming():
    tags_counter = 0
    selected_tags_var = []
    quantity_desired_tags = 3
    while tags_counter < quantity_desired_tags:
        selected_tag_var = random.choice(farming_tags)
        selected_tags_var.append(selected_tag_var)
        farming_tags.remove(selected_tag_var)
        tags_counter = tags_counter + 1
    print('Selected accounts: {}'.format(tags_counter))
    return selected_tags_var

