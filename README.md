# Transfeminiinit website
Transfeminiinit ry is a Finnish organization for transgender women peer support. This website is being developed as part of a proposal for a new web platform for the organization. This website is not yet published.

## setup
### tailwind
`cd transfeminiinit`
`python manage.py tailwind start`

### development server
`cd transfeminiinit`
`python manage.py runserver`

## making translations
`cd transfeminiinit`
`django-admin makemessages -l fi` for Finnish
`django-admin makemessages -l sv` for Swedish
`django-admin makemessages -l en` for English

Translations are then filled out in the admin panel.
