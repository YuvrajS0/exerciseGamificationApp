from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

        widgets = {
            'workout_title': forms.TextInput(
                attrs={
                    'class': '6u 12u$(xsmall)',
                    'placeholder':'Title',
                    'type':'text'
                    }
                ),
            'workout_pub_date': forms.DateTimeInput(
                attrs={
                    'class': '6u$ 12u$(xsmall)',
                    'type':'date'
                    }
                ),
            'workout_start_time': forms.TimeInput(
                attrs={
                    'class': '6u 12u$(xsmall)',
                    'type': 'time'
                }
            )
        }