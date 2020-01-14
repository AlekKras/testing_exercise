#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  model.py
#  
# 
#  
#  

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, RadioField


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name")])
    color = StringField('Color', validators=[DataRequired("Plese enter your color")])
    pet = RadioField('Pets?', default='dog', choices = [('cat', 'Cat'), ('dog', 'Dog')])
    submit = SubmitField('Submit')
