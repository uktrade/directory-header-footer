def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        ROOT_URLCONF='thing',
        SSO_LOGIN_URL='http://login.com',
        SSO_SIGNUP_URL='http://signup.com',
        SSO_LOGOUT_URL='http://logout.com',
        SSO_PROFILE_URL='http://profile.com',
        INSTALLED_APPS=['directory_header_footer'],
        HEADER_FOOTER_CONTACT_US_URL='http://contact-us.com',
        HEADER_FOOTER_CSS_ACTIVE_CLASSES={'fab': True},
    )
