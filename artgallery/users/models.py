from PIL import Image
from django.db import models
from django.contrib.auth.models import User


def path_avatar(instance, filename):
    return 'profile/avatar/{username}/{filename}'.format(username=instance.user.username, filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=path_avatar, default='default.jpg')

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'
