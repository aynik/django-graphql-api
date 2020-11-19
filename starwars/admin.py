from django import forms
from django.contrib import admin, messages

from . import models


class ModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            messages.error(request, "Only superusers can change models")
            return False
        return super(ModelAdmin, self).save_model(request, obj, form, change)


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = "__all__"

    selected_item = forms.ModelChoiceField(queryset=models.Item.objects, required=False)

    def __init__(self, data=None, *args, **kwargs):
        super(GroupAdminForm, self).__init__(data, *args, **kwargs)
        if self.instance:
            self.fields["selected_item"].queryset = self.instance.items

    def clean_selected_item(self):
        data = self.cleaned_data
        if data["selected_item"] and self.instance:
            data["selected_item"] = list(
                self.instance.items.values_list("id", flat=True)
            ).index(data["selected_item"].id)
        return data


class ItemInline(admin.TabularInline):
    model = models.Item
    fk_name = "group"


class GroupAdmin(admin.ModelAdmin):
    fields = ["selected_item"]
    form = GroupAdminForm
    inlines = [ItemInline]


admin.site.register(models.Group, GroupAdmin)

excluded_model_names = ["Group"]

for model in map(
    models.__dict__.get,
    [
        model_name
        for model_name in models.__all__
        if model_name not in excluded_model_names
    ],
):
    admin.site.register(model, ModelAdmin)
