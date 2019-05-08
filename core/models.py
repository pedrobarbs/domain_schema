import uuid
from enum import Enum

from django.db import models


class FIELD_TYPES(Enum):   # A subclass of Enum
    CHAR = "char"
    BOOLEAN = "bool"
    INTEGER = 'int'
    DECIMAL = 'dec'

    def __str__(self):
        return self.value


class Solution(models.Model):
    """
    Solution model. This is the main solution to which the platform will serve. (SAGER)
    """
    name = models.CharField(max_length=30)


class App(models.Model):
    """
    app model
    """
    name = models.CharField(max_length=30)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='apps')


class Migration(models.Model):
    """
    Domain migration
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now=True)


class Entity(models.Model):
    """
    Entity model. This is the Entity that will be used in the solution. (USINA)
    """
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='entities')
    migration = models.OneToOneField(Migration, on_delete=models.CASCADE, related_name='entity')
    last_migration = models.OneToOneField(Migration, on_delete=models.CASCADE, related_name='+')
    name = models.CharField(max_length=30)
    table = models.CharField(max_length=30)


    def save(self, *args, **kwargs):
        self.last_migration = Migration.objects.create()

        if not self.id:
            self.migration = self.last_migration

        super(Entity, self).save(*args, **kwargs)


class Field(models.Model):
    """
    field model
    """
    name = models.CharField(max_length=30)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='fields')
    migration = models.ForeignKey(Migration, on_delete=models.CASCADE, related_name='fields')
    field_type = models.CharField(
        max_length=4,
        choices=[(field, field.value) for field in FIELD_TYPES])

    def save(self, *args, **kwargs):
        self.migration = self.entity.last_migration
        super(Field, self).save(*args, **kwargs)


class EntityMap(models.Model):
    """
    Map model
    """
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='maps')
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='maps')
    name = models.CharField(max_length=30)


class MappedField(models.Model):
    """
    Mapped field model
    """
    entity_map = models.ForeignKey(EntityMap, on_delete=models.CASCADE, related_name='fields')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='mappings')
    alias = models.CharField(max_length=30)



