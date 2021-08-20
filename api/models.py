from django.db import models


class UserRequest(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return "User: {0} {1}".format(self.first_name, self.last_name)

