from django.conf import settings

from directory_constants.constants import urls as default_urls


def sso_processor(request):
    url = request.build_absolute_uri()
    login_url = settings.SSO_PROXY_LOGIN_URL
    return {
        'sso_user': request.sso_user,
        'sso_is_logged_in': request.sso_user is not None,
        'sso_login_url': '{0}?next={1}'.format(login_url, url),
        'sso_register_url': settings.SSO_PROXY_SIGNUP_URL,
        'sso_logout_url': settings.SSO_PROXY_LOGOUT_URL,
        'sso_profile_url': settings.SSO_PROFILE_URL,
    }


def get_url(url_name):
    return getattr(settings, url_name, None) or getattr(default_urls, url_name)


def urls_processor(request):
    return {
        'header_footer_urls': {
            'great_home': get_url('GREAT_HOME'),
            'great_export_home': get_url('GREAT_EXPORT_HOME'),
            # personas
            'new_to_exporting': get_url('EXPORTING_NEW'),
            'occasional_exporter': get_url('EXPORTING_OCCASIONAL'),
            'regular_exporter': get_url('EXPORTING_REGULAR'),
            # guidance/article sections
            'guidance_market_research': get_url('GUIDANCE_MARKET_RESEARCH'),
            'guidance_customer_insight': get_url('GUIDANCE_CUSTOMER_INSIGHT'),
            'guidance_finance': get_url('GUIDANCE_FINANCE'),
            'guidance_business_planning': (
                get_url('GUIDANCE_BUSINESS_PLANNING')
            ),
            'guidance_getting_paid': get_url('GUIDANCE_GETTING_PAID'),
            'guidance_operations_and_compliance': (
                get_url('GUIDANCE_OPERATIONS_AND_COMPLIANCE')
            ),
            # services
            'services_fab': get_url('SERVICES_FAB'),
            'services_soo': get_url('SERVICES_SOO'),
            'services_exopps': get_url('SERVICES_EXOPPS'),
            'services_get_finance': get_url('SERVICES_GET_FINANCE'),
            'services_events': get_url('SERVICES_EVENTS'),
            'info_about': get_url('INFO_ABOUT'),
            'info_contact_us': get_url('INFO_CONTACT_US_DIRECTORY'),
            'info_privacy_and_cookies': get_url('INFO_PRIVACY_AND_COOKIES'),
            'info_terms_and_conditions': get_url('INFO_TERMS_AND_CONDITIONS'),
            'info_dit': get_url('INFO_DIT'),
        }
    }


def header_footer_context_processor(request):
    active_classes = getattr(settings, 'HEADER_FOOTER_CSS_ACTIVE_CLASSES', {})
    return {
        'header_footer_contact_us_url': settings.HEADER_FOOTER_CONTACT_US_URL,
        'header_footer_css_active_classes': active_classes,
        'header_footer_language_select': settings.HEADER_FOOTER_LANGUAGE_SELECT
    }
