from django.db import models
from django.utils import timezone

iSBN_choice = (("en", "5"), ("ru", "2"), ("de", "43"))
binding_choices = (("s", 'soft'), ("h", 'hard'))
language_choices = (("en", "english"), ("ru", "russian"), ("de", "german"))
order_status_shoice = (("1", "in progress"), ("2", "done",), ("3", "canceled",))


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    authors_birthday = models.DateTimeField(default=timezone.now)
    authors_key_words = models.CharField(max_length=200)
    books_income = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    review = models.CharField(max_length=200)
    language = models.CharField(max_length=200, choices=language_choices)
    date_created = models.DateTimeField(default=timezone.now)
    binding = models.CharField(max_length=200, choices=binding_choices)
    iSBN = models.IntegerField(choices=iSBN_choice)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Sell(models.Model):
    order_number = models.IntegerField()
    purchased_books = models.ManyToManyField(to=Book, related_name='sells')
    purchased_date = models.DateTimeField(default=timezone.now)
    order_status = models.CharField(max_length=200, choices=order_status_shoice)
