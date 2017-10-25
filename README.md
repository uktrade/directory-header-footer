# directory-header-footer

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

---

## Requirements

```shell
pip install -r requirements.txt
```

## Installation

```shell
pip install -e git+https://git@github.com/uktrade/directory-header-footer.git@v0.2.0#egg=directory-header-footer
```

Note:
The version number 'v0.2.0' in the above command should change with each release.
See https://github.com/uktrade/directory-header-footer/releases for possible values.


## Development

    $ git clone https://github.com/uktrade/directory-header-footer
    $ cd directory-header-footer

To integrate your local changes to directory-header-footer in another project locally:

    $ pip install git+file://absolute/path/to/directory-header-footer@your-current-local-branch --upgrade --force-reinstall --no-dependencies

Make sure to commit all changes on directory-header-footer first.

## Testing
	$ make test

## Integration

Add directory_header_footer to your `INSTALLED_APPS` in settings.py

```
INSTALLED_APPS = [
    ...,
    'directory_header_footer'
]
```

### Context Processors
You can integrate this repo using its built-in context processors (see context_processors.py) or you can write your own ([documentation](https://docs.djangoproject.com/en/1.11/ref/templates/api/)). If using built-in, add them to your settings.py like so:

```
TEMPLATES = [
    {
        'BACKEND': ...,
        'DIRS': ...,
        'APP_DIRS': ...,
        'OPTIONS': {
            'context_processors': [
                ...,
                'directory_header_footer.context_processors.sso_processor',
                ('directory_header_footer.context_processors.'
                 'header_footer_context_processor'),
            ],
        },
    },
]
```

### Settings Variables
The built-in context processors rely on the following variables in your settings.py:

| Django settings variable         | Notes                              |
| ---------------------------------|------------------------------------|
| SSO_PROXY_LOGIN_URL              | sso_login_url in templates         |
| SSO_PROXY_SIGNUP_URL             | sso_register_url in templates      |
| SSO_PROXY_LOGOUT_URL             | sso_logout_url in templates        |
| SSO_PROFILE_URL                  | sso_profile_url in templates       |
| HEADER_FOOTER_CONTACT_US_URL     | URL for footer "contact us"        |
| HEADER_FOOTER_CSS_ACTIVE_CLASSES | Dict guiding header's "active app" (not used in new header/footer) |


### Adding to templates
After making the appropriate changes in your settings just add the header/footer to your templates with:

```
{% include 'directory_header_footer/header.html' %}
```
### CSS & JS
Add these to your layout template. 

For the old header/footer: 

```
<link href="{% static 'Dit-Pattern-Styling/public/css/main_old.css' %}" media="all" rel="stylesheet" />
```
For the new header/footer:

```
<link href="{% static 'Dit-Pattern-Styling/public/css/main.css' %}" media="all" rel="stylesheet" />
<link href="{% static 'Dit-Pattern-Styling/public/css/compatibility.css' %}" media="all" rel="stylesheet" />
<script src="{% static 'Dit-Pattern-Styling/public/js/third-party.js' %}"></script>
<script src="{% static 'Dit-Pattern-Styling/public/js/script.js' %}"></script>
```

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-header-footer/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-header-footer

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-header-footer/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-header-footer

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-header-footer.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-header-footer
