from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from mainpage.models import Speaker, Comment, Direction, Socials, Advantage, Course, Module, Intention


# Register your models here.

#данные от админки
#schooladmin
#26112001cee

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}
	list_display = ["name", "surname", "degree", "ssau_ref", "photo", "info", "phrase"]
	fields = [("name", "surname"), "degree", "ssau_ref", "photo", "info", "phrase"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ["author", "date", "course", "text", "show"]
	fields = ["author", "course", "date", "text", "show"]


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
	list_display = ["name"]
	fields = ["name"]


@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
	list_display = ["logo_path", "link"]
	fields = ["logo_path", "link"]


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
	list_display = ["name", "text"]
	fields = ["name", "text", "img"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}
	list_display = ["name", "direction", "description", "duration", "start"]
	fields = ["name", "logo_path", ("duration", "hours"), "price", "description", "description_file", "start", "diploma_path", "skills", "direction", "diagram_path", "modules"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
	list_display = ["name", "description"]
	fields = ["name", "description", "speaker"]


@admin.register(Intention)
class IntentionAdmin(admin.ModelAdmin):
	list_display = ["course", "text"]
	fields = ["course", "text"]

