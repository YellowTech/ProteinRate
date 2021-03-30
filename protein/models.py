import datetime

from django.db import models
from django.utils import timezone

class ProteinShake(models.Model):
    name = models.CharField("Name", max_length=200)
    proteinPercentage = models.DecimalField("g of Protein per 100g", decimal_places=2, max_digits=5)
    creaminess = models.SmallIntegerField("Creaminess")
    solubility = models.SmallIntegerField("Solubility")
    sweetness = models.SmallIntegerField("Sweetness")
    artificiality = models.SmallIntegerField("Artificiality")
    smell = models.SmallIntegerField("Smell")
    taste = models.SmallIntegerField("Taste")

    opinion = models.SmallIntegerField("Personal Opinion")

    review = models.TextField("Review")

    url = models.URLField("Product Page")

    def __str__(self):
        return self.name

#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
