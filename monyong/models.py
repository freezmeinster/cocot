# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    STATE = (
        ("S", "Start"),
        ("D", "Done"),
        ("X", "Cancel")
    )

    name = models.CharField(max_length=255)
    state = models.CharField(max_length=1, choices=STATE, default="S")
    progress = models.IntegerField(default=1)
    last_line_log = models.IntegerField(default=0)
    log = models.TextField(blank=True)

    def __unicode__(self):
        return self.name