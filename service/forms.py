from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Project, Worker
from datetime import timedelta


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "project",
            "start_date",
            "end_date",
            "progress",
            "assigned_to",
        ]
        labels = {
            "name": "Название задачи",
            "project": "Проект",
            "start_date": "Дата начала",
            "end_date": "Дата окончания",
            "progress": "Прогресс",
            "assigned_to": "Назначено",
        }
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["project"].queryset = Project.objects.all()
        self.fields["assigned_to"].queryset = Worker.objects.all()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     start_date = cleaned_data.get('start_date')
    #     end_date = cleaned_data.get('end_date')
    #
    #     if start_date and end_date:
    #         if end_date < start_date:
    #             raise ValidationError('Дата окончания не может быть раньше даты начала.')
    #
    #     return cleaned_data

    def save(self, commit=True):
        instance = super(TaskForm, self).save(commit=False)
        if instance.start_date and instance.end_date:
            instance.days_required = (instance.end_date - instance.start_date).days
        if commit:
            instance.save()
        return instance
