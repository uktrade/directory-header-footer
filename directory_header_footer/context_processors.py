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


def urls_processor(request):
    return {
        'great_home': getattr(
            settings, 'GREAT_HOME',
            default_urls.GREAT_HOME),
        'great_export_home': getattr(
            settings, 'GREAT_EXPORT_HOME',
            default_urls.GREAT_EXPORT_HOME),
        # personas
        'new_to_exporting': getattr(
            settings, 'EXPORTING_NEW',
            default_urls.EXPORTING_NEW),
        'occasional_exporter': getattr(
            settings, 'EXPORTING_OCCASIONAL',
            default_urls.EXPORTING_OCCASIONAL),
        'regular_exporter': getattr(
            settings, 'EXPORTING_REGULAR',
            default_urls.EXPORTING_REGULAR),
        # guidance/article sections
        'guidance_market_research': getattr(
            settings, 'GUIDANCE_MARKET_RESEARCH',
            default_urls.GUIDANCE_MARKET_RESEARCH),
        'guidance_customer_insight': getattr(
            settings, 'GUIDANCE_CUSTOMER_INSIGHT',
            default_urls.GUIDANCE_CUSTOMER_INSIGHT),
        'guidance_finance': getattr(
            settings, 'GUIDANCE_FINANCE',
            default_urls.GUIDANCE_FINANCE),
        'guidance_business_planning': getattr(
            settings, 'GUIDANCE_BUSINESS_PLANNING',
            default_urls.GUIDANCE_BUSINESS_PLANNING),
        'guidance_getting_paid': getattr(
            settings, 'GUIDANCE_GETTING_PAID',
            default_urls.GUIDANCE_GETTING_PAID),
        'guidance_operations_and_compliance': getattr(
            settings, 'GUIDANCE_OPERATIONS_AND_COMPLIANCE',
            default_urls.GUIDANCE_OPERATIONS_AND_COMPLIANCE),
        # services
        'services_fab': getattr(
            settings, 'SERVICES_FAB',
            default_urls.SERVICES_FAB),
        'services_soo': getattr(
            settings, 'SERVICES_SOO',
            default_urls.SERVICES_SOO),
        'services_exopps': getattr(
            settings, 'SERVICES_EXOPPS',
            default_urls.SERVICES_EXOPPS),
        'services_get_finance': getattr(
            settings, 'SERVICES_GET_FINANCE',
            default_urls.SERVICES_GET_FINANCE),
        'services_events': getattr(
            settings, 'SERVICES_EVENTS',
            default_urls.SERVICES_EVENTS),
        'info_about': getattr(
            settings, 'INFO_ABOUT',
            default_urls.INFO_ABOUT),
        'info_contact_us': getattr(
            settings, 'INFO_CONTACT_US_DIRECTORY',
            default_urls.INFO_CONTACT_US_DIRECTORY),
        'info_privacy_and_cookies': getattr(
            settings, 'INFO_PRIVACY_AND_COOKIES',
            default_urls.INFO_PRIVACY_AND_COOKIES),
        'info_terms_and_conditions': getattr(
            settings, 'INFO_TERMS_AND_CONDITIONS',
            default_urls.INFO_TERMS_AND_CONDITIONS),
        'info_dit': getattr(
            settings, 'INFO_DIT',
            default_urls.INFO_DIT),
    }


def header_footer_context_processor(request):
    active_classes = getattr(settings, 'HEADER_FOOTER_CSS_ACTIVE_CLASSES', {})
    return {
        'header_footer_contact_us_url': settings.HEADER_FOOTER_CONTACT_US_URL,
        'header_footer_css_active_classes': active_classes,
    }
