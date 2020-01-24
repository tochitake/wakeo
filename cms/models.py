from django.db import models


class Page(models.Model):
    name = models.CharField('ページ名', max_length=255)
    serialcd = models.CharField('シリアルコード', max_length=255)
    memo = models.CharField('メモ', max_length=255, blank=True)

    def __str__(self):
        return self.serialcd


class Member(models.Model):
    #rel = models.ForeignKey(Page, verbose_name='', related_name='Members', on_delete=models.CASCADE, default='A')
    name = models.CharField('メンバー名', max_length=255)
    div = models.CharField('所属', max_length=255, blank=True)
    sex = models.CharField('性別', max_length=255, blank=True)
    team = models.IntegerField('チーム', blank=True, default=0)
    serialcd = models.CharField('シリアルコード', max_length=255, blank=True)
    # pageid = models.CharField('ページID', max_length=255)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField('チーム名', max_length=255)
    serialcd = models.CharField('シリアルコード', max_length=255, blank=True)
    team = models.IntegerField('チーム', blank=True, default=0)

    def __str__(self):
        return self.name

class attribute(models.Model):
    rel = models.ForeignKey(Member, verbose_name='', related_name='attributes', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
