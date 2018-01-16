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
You can integrate this repo using its built-in context processors (see context_processors.py) or you can write your own ([documentation](https://docs.djangoproject.com/en/1.11/ref/templates/api/#writing-your-own-context-processors)). If using built-in, add them to your settings.py like so:

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

See the `urls_processor` in `context_processors.py` for a full list of URL variable names. URLs are pulled from [directory-constants](https://github.com/uktrade/directory-constants/)

### Adding to templates
After making the appropriate changes in your settings just add the header/footer to your templates with `{% include 'directory_header_footer/header.html' %}`. Use `header_old.html` and `footer_old.html` if using the old design.

### CSS

Note that some styling *can* break in the new header/footer when used in the different services. To fix this using sass, copy the header/footer css (`static/Dit-Pattern-Styling/public/css/main.css` or `main_old.css`), rename to `.scss` and import it as a sass file e.g. in `main.scss`:

```
@import 'vars';
@import 'mixins';
@import 'base';
etc ...
// imported header/footer styling
@import 'header-footer';
// to override any broken header/footer styling
@import 'header-footer-fixes';
```

Keeping bug fixes in a separate sass file means whenever this repo is updated, project-specific bug fixes are not lost.

#### Alternatively:

Add these to your layout template.

For the old header/footer:

```
<link href="{% static 'Dit-Pattern-Styling/public/css/main_old.css' %}" media="all" rel="stylesheet" />
```
For the new header/footer (including JS):

```
<link href="{% static 'Dit-Pattern-Styling/public/css/main.css' %}" media="all" rel="stylesheet" />
<link href="{% static 'Dit-Pattern-Styling/public/css/compatibility.css' %}" media="all" rel="stylesheet" />
<script src="{% static 'Dit-Pattern-Styling/public/js/third-party.js' %}"></script>
<script src="{% static 'Dit-Pattern-Styling/public/js/script.js' %}"></script>
```

This adds an extra stylesheet to every page specifically for the header/footer and, if you have any style fixes, you will need to add these to a different stylesheet loaded after the header/footer stylesheet that will override broken styling.

### Automated dependency updates

You can run `make header_footer` to update the `directory-header-footer` dependency in the following repos (providing you have them on your system in the same directory as this one):
* directory-sso
* directory-sso-profile
* directory-ui-buyer
* directory-ui-export-readiness
* help
* navigator

The scripts will ask you for the new version number, the name of the git branch to commit changes to, and the commit message then apply this to all the above repos and push the branch to the remote. PRs for each update will still need to be done manually.

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-header-footer/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-header-footer

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-header-footer/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-header-footer

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-header-footer.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-header-footer
