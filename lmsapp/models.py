from django.db import models

class AndyModel(models.Model):
	andy = models.CharField(max_length=200)
	
	def __str__(self):
		return self.andy

class InstModel(models.Model):
	inst = models.CharField(max_length=200)
	
	def __str__(self):
		return self.inst

class LerModel(models.Model):
	ler = models.CharField(max_length=200)
	
	def __str__(self):
		return self.ler
