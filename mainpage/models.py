import uuid

from django.db import models

# Create your models here.


class Direction(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=63)

	def __str__(self):
		return f"{self.name}"


class Speaker(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	degree = models.TextField()
	ssau_ref = models.URLField()
	photo = models.ImageField(upload_to='speakers/')
	info = models.TextField()
	phrase = models.CharField(max_length=255)

	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url

	def __str__(self):
		return f"{self.name} {self.surname}, {self.degree}"


class Module(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=255)
	description = models.TextField()
	speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.name}"


class Course(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=255)
	logo_path = models.ImageField(upload_to='logos/')
	duration = models.CharField(max_length=20)
	hours = models.PositiveIntegerField()
	price = models.IntegerField(null=True)
	description = models.TextField()
	description_file = models.FileField(upload_to='descriptions/', null=True)
	start = models.DateField()
	diagram_path = models.ImageField(upload_to='diagrams/', null=True)
	diploma_path = models.ImageField(upload_to='diplomas/')
	skills = models.TextField()
	direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
	modules = models.ManyToManyField(Module)

	def __str__(self):
		return f'{self.name}'

	@property
	def photo_url(self):
		if self.logo_path and hasattr(self.logo_path, 'url'):
			return self.logo_path.url

	@property
	def diagram_url(self):
		if self.diagram_path and hasattr(self.diagram_path, 'url'):
			return self.diagram_path.url

	@property
	def photo_dip_url(self):
		if self.diploma_path and hasattr(self.diploma_path, 'url'):
			return self.diploma_path.url

	@property
	def description_url(self):
		if self.description_file and hasattr(self.description_file, 'url'):
			return self.description_file.url


class Socials(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	logo_path = models.ImageField(upload_to='logos/')
	link = models.CharField(max_length=255)

	@property
	def photo_url(self):
		if self.logo_path and hasattr(self.logo_path, 'url'):
			return self.logo_path.url


class Comment(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	date = models.DateField()
	text = models.TextField()
	show = models.BooleanField(default=False)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
	author = models.CharField(max_length=127, default='')


class Advantage(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=127)
	text = models.TextField()
	img = models.ImageField(upload_to='speakers/')

	@property
	def img_url(self):
		if self.img and hasattr(self.img, 'url'):
			return self.img.url


class Application(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=127)
	phone = models.CharField(max_length=20, default='')
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)


class Intention(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	text = models.TextField()
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)


class Manager(models.Model):
	name = models.fields.CharField(max_length=150)
	logo_path = models.ImageField(upload_to='managers/')
	email = models.EmailField()

	@property
	def photo_url(self):
		if self.logo_path and hasattr(self.logo_path, 'url'):
			return self.logo_path.url


class Director(models.Model):
	name = models.fields.CharField(max_length=150)
	logo_path = models.ImageField(upload_to='directors/')
	email = models.EmailField()

	@property
	def photo_url(self):
		if self.logo_path and hasattr(self.logo_path, 'url'):
			return self.logo_path.url
