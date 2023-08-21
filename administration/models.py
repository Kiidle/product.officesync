from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class CustomPermission(models.Model):
    permission = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.permission

class Role(models.Model):
    class Colors(models.TextChoices):
        DARKRED = "darkred", "Dunkelrot"
        RED = "red", "Rot"
        DARKORANGE = "darkorange", "Dunkelorange"
        ORANGE = "orange", "Orange"
        LIGHTGREEN = "lightgreen", "Hellgrün"
        DARKGREEN = "darkgreen", "Dunkelgrün"
        DARKCYAN = "darkcyan", "Türkis"
        LIGHTBLUE = "lightblue", "Hellblau"
        DARKBLUE = "darkblue", "Dunkelblau"
        MEDIUMPURPLE = "mediumpurple", "Violett"
        HOTPINK = "hotpink", "Rosa"
        GRAY = "gray", "Grau"
        BROWN = "brown", "Braun"
        BLACK = "black", "Schwarz"

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=Colors.choices, default=Colors.BLACK)
    permissions = models.ManyToManyField(CustomPermission, related_name='roles', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Logs(models.Model):
    ACTION_CHOICES = (
        ('CREATE', 'Erstellen'),
        ('EDIT', 'Bearbeiten'),
        ('DELETE', 'Löschen'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    model_name = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.content_type:
            self.model_name = self.content_type.model

        super(Logs, self).save(*args, **kwargs)

    def __str__(self):
        return f'User: {self.user.username} | Action: {self.action} | {self.model_name}: {self.content_object} | Date: {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']