# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext as _

# Create your models here.


class Sprint(models.Model):
	
	name = models.CharField(max_length=100, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	end = models.DateField(unique=True)

	def __str__(self):
		return str(self.name)



class Task(models.Model):

	STATUS_TODO = 1
	STATUS_IN_PROGRESS = 2
	STATUS_TESTING = 3
	STATUS_DONE = 4

	STATUS_CHOICES = (
		(STATUS_TODO, _('Not Started')),
		(STATUS_IN_PROGRESS, _('IN PROGRESS')),
		(STATUS_TESTING, _('TESTING')),
		(STATUS_DONE, _('DONE')),
		)

	name = models.CharField(max_length=100, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	sprint = models.ForeignKey(Sprint, blank=True, null=True)
	status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
	order = models.SmallIntegerField(default=0)
	assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TaskAssignee', null=True)
	started = models.DateField(blank=True, null=True)
	due = models.DateField(blank=True, null=True)
	completed = models.DateField(blank=True, null=True)

	def __str__(self):
		return str(self.name)
