# directory-header-footer

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

## Testing
	$ make test

# Settings

| Django setting variable          | notes                              |
| ---------------------------------|------------------------------------|
| SSO_LOGIN_URL                    | URL for signing in to sso          |
| SSO_SIGNUP_URL                   | URL for signing up to sso          |
| SSO_LOGOUT_URL                   | URL for signing out of sso         |
| SSO_PROFILE_URL                  | URL for sso profile                |
| SSO_PASSWORD_RESET_URL           | URL for resetting password         |
| HEADER_FOOTER_CONTACT_US_URL     | URL for footer "contact us"        |
| HEADER_FOOTER_CSS_ACTIVE_CLASSES | Dict guiding header's "active app" |
