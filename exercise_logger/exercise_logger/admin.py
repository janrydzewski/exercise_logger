from django.contrib import admin
from .models import User, Exercise, MuscleGroup, Workout, WorkoutExercise, ExerciseMuscleGroups, WorkoutTemplate, WorkoutTemplateExercises

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(MuscleGroup)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(ExerciseMuscleGroups)
admin.site.register(WorkoutTemplate)
admin.site.register(WorkoutTemplateExercises)