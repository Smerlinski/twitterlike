# Generated by Django 2.2.17 on 2021-01-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_auto_20210128_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetlike',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tweetlike',
            name='tweet',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.DeleteModel(
            name='TweetLike',
        ),
    ]