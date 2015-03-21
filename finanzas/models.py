from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class Exercise(models.Model):
    year = models.IntegerField(unique=True)

    def __unicode__(self):
        return str(self.year)


class Concept(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Period(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    month = models.IntegerField()

    class Meta:
        unique_together = ("exercise", "month")

    def __unicode__(self):
        return str(self.exercise) + " " + str(self.month)


class Movement(models.Model):
    MOVEMENT_TYPE = (
        ('I', 'Income'),
        ('E', 'Expense')
    )

    movement_type = models.CharField(max_length=1, choices=MOVEMENT_TYPE)
    date = models.DateField(editable=True, default=date.today)
    period = models.ForeignKey(Period, editable=False, null=True, on_delete=models.PROTECT)
    concept = models.ForeignKey(Concept, on_delete=models.PROTECT)
    comments = models.CharField(max_length=128, null=True, blank=True)
    amount = models.IntegerField()

    def save(self, *args, **kw):
        # If comments are empty, use the name of the concept
        if len(self.comments) == 0:
            self.comments = self.concept.name

        # Let's choose the period
        # If exercise does not exist, create it
        # Periods will be created by the post_save of the exercise
        try:
            exercise = Exercise.objects.get(year=self.date.year)
        except Exercise.DoesNotExist:
            exercise = Exercise(year=self.date.year)
            exercise.save()

        period = Period.objects.get(exercise=exercise.id, month=self.date.month)
        self.period = period

        super(Movement, self).save(*args, **kw)

    def __unicode__(self):
        return self.comments


@receiver(post_save, sender=Exercise)
def exercise_post_save(sender, created, instance, **kwargs):
    if created:
        for i in range(1, 13):
            new_period = Period(exercise=instance, month=i)
            new_period.save()