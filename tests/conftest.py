def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        ROOT_URLCONF='thing',
        SSO_PROXY_LOGIN_URL='http://login.com',
        SSO_PROXY_SIGNUP_URL='http://signup.com',
        SSO_PROXY_LOGOUT_URL='http://logout.com',
        SSO_PROFILE_URL='http://profile.com',
        INSTALLED_APPS=[
            'directory_constants',
            'directory_header_footer',
        ],
        HEADER_FOOTER_CONTACT_US_URL='http://contact-us.com',
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
        }],
        HEADER_FOOTER_CSS_ACTIVE_CLASSES={'fab': True},
    )
