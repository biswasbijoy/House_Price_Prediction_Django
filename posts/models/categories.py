from django.db import models
from posts.models.base_time_stamp import BaseStampStampModel


class PostCategory(BaseStampStampModel):
    CATEGORY_OPTION_CHOICES = [
        ('1', 'Sell',),
        ('2', 'Buy',),
        ('3', 'Information',),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_OPTION_CHOICES, default='1')
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_category_display()
