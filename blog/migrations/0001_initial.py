# Generated by Django 3.2.6 on 2021-08-19 15:39
import json

from django.conf import settings
from django.db import migrations, models


def insert_bad_articles(apps, _):
    Article = apps.get_model('blog', 'Article')
    with open(settings.BASE_DIR / 'blog/fixtures/articles.json', 'r') as f:
        articles = json.load(f)
    for article in articles:
        Article.objects.create(**article['fields'])


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RunPython(
            code=insert_bad_articles,
            reverse_code=migrations.RunPython.noop
        )
    ]
