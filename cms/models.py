from django.db import models


class Member(models.Model):
    name = models.CharField('メンバー名', max_length=255)
    div = models.CharField('所属', max_length=255, blank=True)
    sex = models.CharField('性別', max_length=255, blank=True)
    team = models.IntegerField('チーム', blank=True, default=0)

    def __str__(self):
        return self.name


class attribute(models.Model):
    rel = models.ForeignKey(Member, verbose_name='', related_name='attributes', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
