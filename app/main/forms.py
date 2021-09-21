from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
  title = StringField('Title', validators = [Required()])
  description = TextAreaField("What would you like to pitch?", validators = [Required()])
  category = RadioField('Label', choices = [('businesspitch', 'Business Pitch'), ('entertainmentpitch', 'Entertainment Pitch'), ('lyricspitch', ' Lyrics Pitch'), ('advertisementpitch', 'Advertisement Pitch'),('relationshippitch' , 'Relationship Pitch')], validators = [Required()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  description = TextAreaField('Add comments', validators = [Required()])
  submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
  submit = SubmitField()

class Downvote(FlaskForm):
  submit = SubmitField()

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.', validators = [Required()])
  submit = SubmitField('Submit')

