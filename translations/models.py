from django.db import models


class Translation(models.Model):
    TRANSLATION_STATUSES = (
        ('not initiated', 'not initiated'),
        ('in translation', 'in translation'),
        ('pending QA', 'pending QA'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('sent to client', 'sent to client'),
    )

    original_text = models.TextField()
    translated_text = models.TextField()
    status = models.CharField(
        choices=TRANSLATION_STATUSES,
        default='not initiated',
        max_length=25,
    )
    is_complete = models.BooleanField(default=False)
    assigned_to = models.CharField(
        choices=(
            ('qa', 'qa'),
            ('translator', 'translator'),
            ('none', 'none'),
        ),
        default='none',
        max_length=15,
    )
    qa_user = models.ForeignKey('users.QualityAssurance', on_delete=models.SET_NULL, null=True, blank=True)
    translator = models.ForeignKey('users.Translator', on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
