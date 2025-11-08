from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index=True,
        null=False,
        verbose_name="Author",
        help_text="Name of the author"
        )
    title = models.CharField(
        verbose_name="Title",
        max_length=100,
        db_index=True,
        blank=False,
        null=False,
        help_text="Specify the name of the content"
        )
    content = models.TextField(
        verbose_name="Content",
        max_length=500,
        blank=False,
        null=False,
        help_text="Enter content"
    )
    created_at = models.DateTimeField(
        verbose_name="Created",
        db_index=True,
        auto_now_add=True,
        help_text="Date of creation"
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated",
        db_index=True,
        auto_now=True,
        help_text="Date update"
    )

    class Meta:
        pass