from django.db import models

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name

class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_text = models.TextField(blank=True, null=True)
    article_text2 = models.TextField(blank=True, null=True)
    article_text3 = models.TextField(blank=True, null=True)
    article_title = models.CharField(max_length=500, null=True)
    article_logo = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500, null=True)
    author_profile_link = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    article_summary = models.CharField(max_length=50000, null=True)

    def __str__(self):
        return self.article_title

class Trending(models.Model):
    article_id = models.IntegerField(primary_key=True)
    trending_title = models.CharField(max_length=500, null=True)
    trending_logo = models.CharField(max_length=500, null=True)
    trending_date = models.CharField(max_length=500, null=True)
    trending_url = models.IntegerField()

    def __str__(self):
        return self.trending_title

class Homec(models.Model):
    homec_id = models.IntegerField(primary_key=True)
    homec_title = models.CharField(max_length=500, null=True)
    homec_logo = models.CharField(max_length=500, null=True)
    homec_url = models.IntegerField()

    def __str__(self):
        return self.homec_title

class Homel(models.Model):
    homel_id = models.IntegerField(primary_key=True)
    homel_title = models.CharField(max_length=500, null=True)
    homel_logo = models.CharField(max_length=500, null=True)
    homel_date = models.CharField(max_length=500, null=True)
    homel_url = models.IntegerField()

    def __str__(self):
        return self.homel_title