from django.conf import settings


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


def urls_processor(request):
    return {
        'great_home': settings.URL_GREAT_HOME,
        'great_export_home': settings.URL_GREAT_EXPORT_HOME,
        # personas
        'new_to_exporting': settings.URL_EXPORTING_NEW,
        'occasional_exporter': settings.URL_EXPORTING_OCCASIONAL,
        'regular_exporter': settings.URL_EXPORTING_REGULAR,
        # guidance/article sections
        'guidance_market_research': settings.URL_GUIDANCE_MARKET_RESEARCH,
        'guidance_customer_insight': settings.URL_GUIDANCE_CUSTOMER_INSIGHT,
        'guidance_finance': settings.URL_GUIDANCE_FINANCE,
        'guidance_business_planning': settings.URL_GUIDANCE_BUSINESS_PLANNING,
        'guidance_getting_paid': settings.URL_GUIDANCE_GETTING_PAID,
        'guidance_operations_compliance': settings.URL_OPERATIONS_COMPLIANCE,
        # services
        'services_fab': settings.URL_SERVICES_FAB,
        'services_soo': settings.URL_SERVICES_SOO,
        'services_exopps': settings.URL_SERVICES_EXOPPS,
        'services_get_finance': settings.URL_SERVICES_GET_FINANCE,
        'services_events': settings.URL_SERVICES_EVENTS,
        'info_about': settings.URL_INFO_ABOUT,
        'info_contact_us': settings.URL_INFO_CONTACT_US,
        'info_privacy_and_cookies': settings.URL_INFO_PRIVACY_AND_COOKIES,
        'info_terms_and_conditions': settings.URL_INFO_TERMS_AND_CONDITIONS,
        'info_dit': settings.URL_INFO_DIT,
    }


def header_footer_context_processor(request):
    active_classes = getattr(settings, 'HEADER_FOOTER_CSS_ACTIVE_CLASSES', {})
    return {
        'header_footer_contact_us_url': settings.HEADER_FOOTER_CONTACT_US_URL,
        'header_footer_css_active_classes': active_classes,
    }
