from django.conf import settings


def sso_processor(request):
    url = request.build_absolute_uri()
    return {
        'sso_user': request.sso_user,
        'sso_is_logged_in': request.sso_user is not None,
        'sso_login_url': '{0}?next={1}'.format(settings.SSO_LOGIN_URL, url),
        'sso_register_url': settings.SSO_SIGNUP_URL,
        'sso_logout_url': settings.SSO_LOGOUT_URL,
        'sso_profile_url': settings.SSO_PROFILE_URL,
    }


def header_footer_context_processor(request):
    active_classes = getattr(settings, 'HEADER_FOOTER_CSS_ACTIVE_CLASSES', {})
    return {
        'header_footer_contact_us_url': settings.HEADER_FOOTER_CONTACT_US_URL,
        'header_footer_css_active_classes': active_classes,
    }
