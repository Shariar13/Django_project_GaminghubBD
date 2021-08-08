from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin


class pubg_registered_id(models.Model):
    username = models.CharField(max_length=100, null=True)
    tournament_name = models.CharField(max_length=100, null=True)
    tournament = models.CharField(max_length=100, null=True)
    pubg_id_1 = models.CharField(max_length=100, null=True)
    pubg_id_2 = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True)
    transactionid = models.CharField(max_length=100, null=True, blank=True)
    phone_4_digit = models.CharField(max_length=100, null=True, blank=True)
    registration_status = models.CharField(max_length=100, null=True)
    room_id = models.CharField(max_length=100, null=True)
    room_password = models.CharField(max_length=100, null=True)
    slot = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    # date=models.DateField(auto_now_add=True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username

    class Meta:
        db_table = "home_pubg_registered_id"





class pubg_registered_id_10_taka(models.Model):
    username = models.CharField(max_length=100)
    pubg_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    transactionid = models.CharField(max_length=100)
    phone_4_digit = models.CharField(max_length=100)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username







class freefire_registered_id(models.Model):
    username = models.CharField(max_length=100, null=True)
    tournament_name = models.CharField(max_length=100, null=True)
    tournament = models.CharField(max_length=100, null=True)
    freefire_id_1 = models.CharField(max_length=100, null=True)
    freefire_id_2 = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=100, null=True)
    transactionid = models.CharField(max_length=100, null=True, blank=True)
    phone_4_digit = models.CharField(max_length=100, null=True, blank=True)
    registration_status = models.CharField(max_length=100, null=True)
    room_id = models.CharField(max_length=100, null=True)
    room_password = models.CharField(max_length=100, null=True)
    slot = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    # date=models.DateField(auto_now_add=True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username
