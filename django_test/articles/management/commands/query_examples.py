from django.core.management.base import BaseCommand
from articles.models import Article, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):

        '''
        Простейшие запросы
        '''
        # Получить список всех объектов
        articles = Article.objects.all()
        print(type(articles))

        # articles - type = QuerySet
        print(articles.first())

        # get
        '''
        art = articles.filter(id=1) # не нужно делать так!
        '''
        art = articles.get(id=1) # не нужно делать так!

        print(art, type(art))

        # filter/exclude
        art = articles.filter(id=1)

        art_exclude = articles.exclude(id=1)
        print('Filter: ', art)
        print('Exclude: ', art_exclude)

        '''
        Непростейшие запросы
        '''
        # больше меньше
        articles = Article.objects.filter(article_rating__gt = 9) #gte (больше или равно)
        print('Статьи с рейтингом более 9ти: ', articles)

        articles = Article.objects.filter(article_rating__lt = 9) #lte (меньше или равно)
        print('Статьи с рейтингом менее 9ти: ', articles)

        # запросы с условием на текстовые данные

        articles = Article.objects.filter(article_name__startswith = 'C')
        print('Статьи с названием на букву C ', articles)

        articles = Article.objects.filter(article_name__contains = 'L')
        print('В название статьи входит символ L: ', articles)

        # Запросы к связанным моделям

        '''
        Способ 1
        '''
        tags = Tag.objects.filter(tag_name__startswith = 'H')
        articles = Article.objects.filter(article_tag = tags[0])
        print('Статьи с определенным тегом: ', articles)

        '''
        Способ 2
        '''
        articles = Article.objects.filter(article_tag__tag_name__startswith = 'N')
        print('Статьи с определенным тегом 2: ', articles)
