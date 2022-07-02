from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Entry(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор", default="Unknown")
    author_mail = models.CharField(max_length=50, null=False, blank=False, verbose_name="Почта")
    content = models.TextField(max_length=3000, null=False, blank=False,  verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name="Статус")

    def __str__(self):
        return f"{self.id}. {self.author}: {self.author_mail}"

    class Meta:
        db_table = "entries"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
