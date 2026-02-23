from django.db import models
class Feedback(models.Model):
    uname = models.CharField(max_length=50)
    feedback = models.CharField(max_length=2000, default='', blank=True)

    @staticmethod
    def get_all_feedbacks():
        return Feedback.objects.all()

