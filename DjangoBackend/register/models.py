from django.db import models
from django.http import request
from django.shortcuts import render

# Create your models here.

class userRegestration (models.Model):
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class userEmailPassword (models.Model):
    emailID = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
