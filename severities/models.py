from django.db import models

SEVERITIES = (
    (10, 'Minor'),
    (20, 'Major'),
    (30, 'Cosmetic'),
)

class ReviewSeverity(models.Model):
    """Allows setting the priority of a review."""
    review = models.ForeignKey('ReviewRequest')
    severity = models.ChoiceField(choices=SEVERITIES, default=10)