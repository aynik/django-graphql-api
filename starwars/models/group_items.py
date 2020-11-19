from django.db import models


class Group(models.Model):
    selected_item = models.PositiveIntegerField(blank=True, null=True)


class Item(models.Model):
    title = models.CharField(max_length=128)
    group = models.ForeignKey(Group, related_name="items", on_delete=models.CASCADE)

    @property
    def group_index(self):
        return list(self.group.items.values_list("id", flat=True)).index(self.id)
