from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    articles = models.ManyToManyField(
        'Article',
        through='TagToArticle',
        related_name="tags",
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class TagToArticle(models.Model):
    class Meta:
        verbose_name = 'Тематическая статья'
        verbose_name_plural = 'Тематические статьи'

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья", related_name="scopes")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Тэг", related_name="scopes")
    is_main = models.BooleanField(verbose_name="основной", default=False, blank=False, null=False)
