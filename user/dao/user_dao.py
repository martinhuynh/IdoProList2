from user.models import User


class UserDAO():
    def getUser(self, user_id):
        return User.objects.get(id=user_id)