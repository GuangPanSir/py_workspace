from django.db.models import Max

from userApp.models import *

from mydiangoDemo01.userApp.models import UserInfo


def accountIsExit(user_account):
    user_list = UserInfo.objects.filter(userAccount=user_account)
    if user_list is not None and len(user_list) > 0:
        return True
    else:
        return False


def createUserId():
    user_id = UserInfo.objects.aggregate(models.Max("userId"))
    return user_id['userId__max'] + 1


def login(user_acc, user_pass):
    try:
        login_user = UserInfo.objects.get(userAccount=user_acc, userPass=user_pass)
    except Exception:
        return None
    return login_user


