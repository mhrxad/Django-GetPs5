# ------------------------------------ parsley ------------------------------------

# Install Django Parsley => 'pip install django-parsley'
# Add 'parsley' to INSTALLED_APPS in your settings file
# Add '@parsleyfy' decorator to Django form class (for default mode)
# Parsley relies on jQuery (>= 1.8), and it will need to be included before including Parsley
# parsley documentation => https://parsleyjs.org/doc/
# parsley.js installation => https://parsleyjs.org/doc/download.html
# parsley.css installation => https://parsleyjs.org/src/parsley.css
# add ( data-parsley-validate ) to each <form> you want to be validated

from parsley.decorators import parsleyfy


class parsley:
    minlength = 'minlength'
    required = 'data-parsley-required'
    type = 'data-parsley-type'
    range = 'data-parsley-range'
    maxlength = 'maxlength'
    length = 'data-parsley-length'
    min = 'min'
    max = 'max'
    pattern = 'data-parsley-pattern'
    mincheck = 'data-parsley-mincheck'
    maxcheck = 'maxcheck'
    check = 'data-parsley-check'
    equalto = "data-parsley-equalto"

    # data-parsley-required = "true"
    # data-parsley-required = "false"

    # data-parsley-type = "email"
    # data-parsley-type = "number"
    # data-parsley-type = "integer"
    # data-parsley-type = "digits"
    # data-parsley-type = "alphanum"
    # data-parsley-type = "url"

    # data-parsley-range = "[6, 10]"

    # minlength = "6"

    # maxlength = "6"

    # data-parsley-length = "[6, 10]"

    # min = "6"

    # max = "6"

    # data-parsley-pattern = "\d+"

    # data-parsley-mincheck = "3"

    # data-parsley-maxcheck = "3"

    # data-parsley-check = "[1, 3]"

    # data-parsley-equalto = "#anotherfield_id"
