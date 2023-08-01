from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateTimeField, SelectField, TextAreaField, SubmitField
import email_validator
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired, Regexp
from wtforms import validators
from wtforms.fields import DateField, EmailField, TelField
from datetime import date


class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired(), Length(
        min=8, max=20, message='Enter Username between 8 and 20 characters'), Regexp(
        "^[a-zA-Z0-9_]+$", message='Username can be Alphabetic or Alphanumeric')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=10, max=10, message='Enter Exactly 10 characters only'), Regexp(
        "^(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", message='Enter atleast 1 special character, 1 Number, 1 Uppercase( use aaaaaa1@A for debugging)')])
    submit = SubmitField('Log In')


class patientSchema(FlaskForm):
    patient_ssn = IntegerField("Patient SSN", validators=[InputRequired(
        message='Please Enter a Numeric Value'), NumberRange(min=1, max=999999999, message='Max 9 digit Numeric')])
    patient_id = IntegerField("Patient ID")
    patient_name = StringField("Patient Name", validators=[InputRequired()])
    patient_age = IntegerField('Age', validators=[InputRequired(message='Please Enter a Numeric Value'), NumberRange(
        min=1, max=99, message="Should be an Integer between 1 and 99")])
    date_of_admission = DateField(
        "Admission date", format='%Y-%m-%d', validators=[InputRequired()],default= date.today())
    type_of_bed = SelectField('Type of Bed', choices=[
        ("General", "General Ward"),
        ("Semi", "Semi Sharing"),
        ("Single", "Single Room")],
        validators=[InputRequired()])
    address = TextAreaField("Address", validators=[InputRequired()])
    state = StringField("State", validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    submit = SubmitField("Submit")


class PatientSearchForm(FlaskForm):
    patient_id = IntegerField("Patient ID", validators=[
                              InputRequired(message="Please Enter an Integer")])
    submit = SubmitField("Submit")


class IssueMedForm(FlaskForm):
    med_name = SelectField(
        u'Medicine Name',
        choices=[]
    )
    med_qty = IntegerField('Quantity', validators=[NumberRange(
        min=1, message="Quantity can't be less than 1"), InputRequired(message="Please enter an Integer")])
    submit = SubmitField('Submit')


class medicineSchema(FlaskForm):
    patient_id = IntegerField("Patient ID")
    medicine_name = StringField("Medicine Name", validators=[InputRequired()])
    quantity = IntegerField('Quantity', validators=[InputRequired(
        message='Please Enter a Numeric Value'), NumberRange(min=1, max=99)])
    submit = SubmitField("Submit")


class DiagnosticsForm(FlaskForm):
    test_name = SelectField(
        u'Test Name',
        choices=[]
    )
    submit = SubmitField('Get Charges')


class diagnosticsSchema(FlaskForm):
    patient_id = IntegerField("Patient ID")
    diagnosis = StringField("Diagnosis", validators=[InputRequired()])
    submit = SubmitField("Submit")
