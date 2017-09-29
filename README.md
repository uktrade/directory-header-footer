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

## Testing
	$ make test

# Settings

| Django setting variable          | notes                              |
| ---------------------------------|------------------------------------|
| SSO_PROXY_LOGIN_URL                    | URL for signing in to sso          |
| SSO_PROXY_SIGNUP_URL                   | URL for signing up to sso          |
| SSO_PROXY_LOGOUT_URL                   | URL for signing out of sso         |
| SSO_PROXY_PROFILE_URL                  | URL for sso profile                |
| SSO_PROXY_PASSWORD_RESET_URL           | URL for resetting password         |
| HEADER_FOOTER_CONTACT_US_URL     | URL for footer "contact us"        |
| HEADER_FOOTER_CSS_ACTIVE_CLASSES | Dict guiding header's "active app" |


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-header-footer/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-header-footer

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-header-footer/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-header-footer/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-header-footer

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-header-footer.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-header-footer
