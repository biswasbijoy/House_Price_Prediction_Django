from django.db import models
from posts.models.base_time_stamp import BaseStampStampModel


class PostCategory(BaseStampStampModel):
    CATEGORY_OPTION_CHOICES = (
        ('Cat_one', 'Sell',),
        ('Cat_two', 'Buy',),
        ('Cat_three', 'Information',),
    )

    category = models.CharField(max_length=50, choices=CATEGORY_OPTION_CHOICES, default='Cat_one')
    value = models.PositiveIntegerField(default=0)