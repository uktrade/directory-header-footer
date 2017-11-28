from unittest.mock import Mock
import pytest

from directory_header_footer import context_processors
from directory_constants.constants import urls as default_urls


@pytest.fixture
def sso_user():
    return Mock(
        id=1,
        email='jim@example.com'
    )


@pytest.fixture
def request_logged_in(rf, sso_user):
    request = rf.get('/')
    request.sso_user = sso_user
    return request


@pytest.fixture
def request_logged_out(rf):
    request = rf.get('/')
    request.sso_user = None
    return request


def test_sso_logged_in(request_logged_in):
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_is_logged_in'] is True


def test_sso_profile_url(request_logged_in, settings):
    settings.SSO_PROFILE_URL = 'http://www.example.com/profile/'
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_profile_url'] == settings.SSO_PROFILE_URL


def test_sso_register_url_url(request_logged_in, settings):
    settings.SSO_PROXY_SIGNUP_URL = 'http://www.example.com/signup/'
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_register_url'] == (
        'http://www.example.com/signup/?next=http://testserver/'
    )


def test_sso_logged_out(request_logged_out):
    context = context_processors.sso_processor(request_logged_out)
    assert context['sso_is_logged_in'] is False


def test_sso_login_url(request_logged_in, settings):
    settings.SSO_PROXY_LOGIN_URL = 'http://www.example.com/login/'
    expected = 'http://www.example.com/login/?next=http://testserver/'
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_login_url'] == expected


def test_sso_logout_url(request_logged_in, settings):
    settings.SSO_PROXY_LOGOUT_URL = 'http://www.example.com/logout/'
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_logout_url'] == (
        'http://www.example.com/logout/?next=http://testserver/'
    )


def test_sso_user(request_logged_in, sso_user):
    context = context_processors.sso_processor(request_logged_in)
    assert context['sso_user'] == sso_user


def test_header_footer_context_processor(settings):
    settings.HEADER_FOOTER_CONTACT_US_URL = 'http://bones.com'
    settings.HEADER_FOOTER_CSS_ACTIVE_CLASSES = {'fab': True}

    context = context_processors.header_footer_context_processor(None)

    assert context == {
        'header_footer_contact_us_url': 'http://bones.com',
        'header_footer_css_active_classes': {'fab': True},
    }


def test_urls_processor(rf, settings):
    settings.GREAT_HOME = 'http://home.com'
    settings.GREAT_EXPORT_HOME = 'http://export.com'
    settings.EXPORTING_NEW = 'http://export.com/new'
    settings.EXPORTING_OCCASIONAL = 'http://export.com/occasional'
    settings.EXPORTING_REGULAR = 'http://export.com/regular'
    settings.GUIDANCE_MARKET_RESEARCH = 'http://market-research.com'
    settings.GUIDANCE_CUSTOMER_INSIGHT = 'http://customer-insight.com'
    settings.GUIDANCE_FINANCE = 'http://finance.com'
    settings.GUIDANCE_BUSINESS_PLANNING = 'http://business-planning.com'
    settings.GUIDANCE_GETTING_PAID = 'http://getting-paid.com'
    settings.GUIDANCE_OPERATIONS_AND_COMPLIANCE = (
        'http://operations-and-compliance.com')
    settings.SERVICES_FAB = 'http://export.com/fab'
    settings.SERVICES_SOO = 'http://export.com/soo'
    settings.SERVICES_EXOPPS = 'http://export.com/exopps'
    settings.SERVICES_GET_FINANCE = 'http://export.com/get-finance'
    settings.SERVICES_EVENTS = 'http://export.com/events'
    settings.INFO_ABOUT = 'http://about.com'
    settings.INFO_CONTACT_US_DIRECTORY = 'http://contact.com'
    settings.INFO_PRIVACY_AND_COOKIES = 'http://privacy-and-cookies.com'
    settings.INFO_TERMS_AND_CONDITIONS = 'http://terms-and-conditions.com'
    settings.INFO_DIT = 'http://dit.com'

    actual = context_processors.urls_processor(None)

    assert actual == {
        'header_footer_urls': {
            'great_home': 'http://home.com',
            'great_export_home': 'http://export.com',
            'new_to_exporting': 'http://export.com/new',
            'occasional_exporter': 'http://export.com/occasional',
            'regular_exporter': 'http://export.com/regular',
            'guidance_market_research': 'http://market-research.com',
            'guidance_customer_insight': 'http://customer-insight.com',
            'guidance_finance': 'http://finance.com',
            'guidance_business_planning': 'http://business-planning.com',
            'guidance_getting_paid': 'http://getting-paid.com',
            'guidance_operations_and_compliance': (
                'http://operations-and'
                '-compliance.com'),
            'services_fab': 'http://export.com/fab',
            'services_soo': 'http://export.com/soo',
            'services_exopps': 'http://export.com/exopps',
            'services_get_finance': 'http://export.com/get-finance',
            'services_events': 'http://export.com/events',
            'info_about': 'http://about.com',
            'info_contact_us': 'http://contact.com',
            'info_privacy_and_cookies': 'http://privacy-and-cookies.com',
            'info_terms_and_conditions': 'http://terms-and-conditions.com',
            'info_dit': 'http://dit.com',
        }
    }


def test_urls_processor_defaults(rf, settings):

    actual = context_processors.urls_processor(None)

    assert actual == {
        'header_footer_urls': {
            'great_home': default_urls.GREAT_HOME,
            'great_export_home': default_urls.GREAT_EXPORT_HOME,
            'new_to_exporting': default_urls.EXPORTING_NEW,
            'occasional_exporter': default_urls.EXPORTING_OCCASIONAL,
            'regular_exporter': default_urls.EXPORTING_REGULAR,
            'guidance_market_research': default_urls.GUIDANCE_MARKET_RESEARCH,
            'guidance_customer_insight': (
                default_urls.GUIDANCE_CUSTOMER_INSIGHT),
            'guidance_finance': default_urls.GUIDANCE_FINANCE,
            'guidance_business_planning': (
                default_urls.GUIDANCE_BUSINESS_PLANNING),
            'guidance_getting_paid': default_urls.GUIDANCE_GETTING_PAID,
            'guidance_operations_and_compliance': (
                default_urls.GUIDANCE_OPERATIONS_AND_COMPLIANCE),
            'services_fab': default_urls.SERVICES_FAB,
            'services_soo': default_urls.SERVICES_SOO,
            'services_exopps': default_urls.SERVICES_EXOPPS,
            'services_get_finance': default_urls.SERVICES_GET_FINANCE,
            'services_events': default_urls.SERVICES_EVENTS,
            'info_about': default_urls.INFO_ABOUT,
            'info_contact_us': default_urls.INFO_CONTACT_US_DIRECTORY,
            'info_privacy_and_cookies': default_urls.INFO_PRIVACY_AND_COOKIES,
            'info_terms_and_conditions': (
                default_urls.INFO_TERMS_AND_CONDITIONS),
            'info_dit': default_urls.INFO_DIT,
        }
    }


def test_urls_processor_defaults_explicitly_none(rf, settings):
    settings.GREAT_HOME = None
    settings.GREAT_EXPORT_HOME = None
    settings.EXPORTING_NEW = None
    settings.EXPORTING_OCCASIONAL = None
    settings.EXPORTING_REGULAR = None
    settings.GUIDANCE_MARKET_RESEARCH = None
    settings.GUIDANCE_CUSTOMER_INSIGHT = None
    settings.GUIDANCE_BUSINESS_PLANNING = None
    settings.GUIDANCE_GETTING_PAID = None
    settings.GUIDANCE_OPERATIONS_AND_COMPLIANCE = None
    settings.SERVICES_FAB = None
    settings.SERVICES_SOO = None
    settings.SERVICES_EXOPPS = None
    settings.SERVICES_GET_FINANCE = None
    settings.SERVICES_EVENTS = None
    settings.INFO_ABOUT = None
    settings.INFO_CONTACT_US_DIRECTORY = None
    settings.INFO_PRIVACY_AND_COOKIES = None
    settings.INFO_TERMS_AND_CONDITIONS = None
    settings.INFO_DIT = None

    actual = context_processors.urls_processor(None)

    assert actual == {
        'header_footer_urls': {
            'great_home': default_urls.GREAT_HOME,
            'great_export_home': default_urls.GREAT_EXPORT_HOME,
            'new_to_exporting': default_urls.EXPORTING_NEW,
            'occasional_exporter': default_urls.EXPORTING_OCCASIONAL,
            'regular_exporter': default_urls.EXPORTING_REGULAR,
            'guidance_market_research': default_urls.GUIDANCE_MARKET_RESEARCH,
            'guidance_customer_insight': (
                default_urls.GUIDANCE_CUSTOMER_INSIGHT),
            'guidance_finance': default_urls.GUIDANCE_FINANCE,
            'guidance_business_planning': (
                default_urls.GUIDANCE_BUSINESS_PLANNING),
            'guidance_getting_paid': default_urls.GUIDANCE_GETTING_PAID,
            'guidance_operations_and_compliance': (
                default_urls.GUIDANCE_OPERATIONS_AND_COMPLIANCE),
            'services_fab': default_urls.SERVICES_FAB,
            'services_soo': default_urls.SERVICES_SOO,
            'services_exopps': default_urls.SERVICES_EXOPPS,
            'services_get_finance': default_urls.SERVICES_GET_FINANCE,
            'services_events': default_urls.SERVICES_EVENTS,
            'info_about': default_urls.INFO_ABOUT,
            'info_contact_us': default_urls.INFO_CONTACT_US_DIRECTORY,
            'info_privacy_and_cookies': default_urls.INFO_PRIVACY_AND_COOKIES,
            'info_terms_and_conditions': (
                default_urls.INFO_TERMS_AND_CONDITIONS),
            'info_dit': default_urls.INFO_DIT,
        }
    }
