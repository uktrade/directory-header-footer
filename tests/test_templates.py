from django.template.loader import render_to_string
from bs4 import BeautifulSoup

import pytest


@pytest.mark.parametrize('template_name', (
    'directory_header_footer/header.html',
    'directory_header_footer/header_old.html',
))
def test_header_logged_in(template_name):
    context = {
        'sso_is_logged_in': True,
        'sso_login_url': 'login.com',
        'sso_logout_url': 'logout.com',
    }
    html = render_to_string(template_name, context)
    assert 'Sign in' not in html
    assert context['sso_login_url'] not in html
    assert 'Sign out' in html
    assert context['sso_logout_url'] in html


@pytest.mark.parametrize('template_name', (
    'directory_header_footer/header.html',
    'directory_header_footer/header_old.html',
))
def test_header_logged_out(template_name):
    context = {
        'sso_is_logged_in': False,
        'sso_login_url': 'login.com',
        'sso_logout_url': 'logout.com',
    }
    html = render_to_string(template_name, context)
    assert 'Sign in' in html
    assert context['sso_login_url'] in html
    assert 'Sign out' not in html
    assert context['sso_logout_url'] not in html


def test_service_active_class_empty():
    context = {
        'header_footer_css_active_classes': {}
    }
    template_name = 'directory_header_footer/header_old.html'
    html = render_to_string(template_name, context)
    element = BeautifulSoup(html, 'html.parser').find(id='nav-fab')
    assert 'navigation-main-link--active' not in element.attrs['class']


def test_service_active_class_fab():
    context = {
        'header_footer_css_active_classes': {
            'fab': True
        }
    }
    template_name = 'directory_header_footer/header_old.html'
    html = render_to_string(template_name, context)
    element_fab = BeautifulSoup(html, 'html.parser').find(id='nav-fab')
    element_soo = BeautifulSoup(html, 'html.parser').find(id='nav-soo')
    assert 'navigation-main-link--active' in element_fab.attrs['class']
    assert 'navigation-main-link--active' not in element_soo.attrs['class']


def test_service_active_class_soo():
    context = {
        'header_footer_css_active_classes': {
            'soo': True
        }
    }
    template_name = 'directory_header_footer/header_old.html'
    html = render_to_string(template_name, context)
    element_soo = BeautifulSoup(html, 'html.parser').find(id='nav-soo')
    element_fab = BeautifulSoup(html, 'html.parser').find(id='nav-fab')
    assert 'navigation-main-link--active' in element_soo.attrs['class']
    assert 'navigation-main-link--active' not in element_fab.attrs['class']


def test_urls_exist_in_new_header():
    template_name = 'directory_header_footer/header.html'
    context = {
        'header_footer_urls': {
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
        }
    }
    html = render_to_string(template_name, context)
    header_footer_urls = context['header_footer_urls']
    assert header_footer_urls['great_export_home'] in html
    assert header_footer_urls['new_to_exporting'] in html
    assert header_footer_urls['occasional_exporter'] in html
    assert header_footer_urls['regular_exporter'] in html
    assert header_footer_urls['guidance_market_research'] in html
    assert header_footer_urls['guidance_customer_insight'] in html
    assert header_footer_urls['guidance_finance'] in html
    assert header_footer_urls['guidance_business_planning'] in html
    assert header_footer_urls['guidance_getting_paid'] in html
    assert header_footer_urls['guidance_operations_and_compliance'] in html
    assert header_footer_urls['services_fab'] in html
    assert header_footer_urls['services_soo'] in html
    assert header_footer_urls['services_exopps'] in html
    assert header_footer_urls['services_get_finance'] in html
    assert header_footer_urls['services_events'] in html


def test_urls_exist_in_old_header():
    template_name = 'directory_header_footer/header_old.html'
    context = {
        'header_footer_urls': {
            'great_home': 'http://home.com',
            'great_export_home': 'http://export.com',
            'new_to_exporting': 'http://export.com/new',
            'occasional_exporter': 'http://export.com/occasional',
            'regular_exporter': 'http://export.com/regular',
            'services_fab': 'http://export.com/fab',
            'services_soo': 'http://export.com/soo',
            'services_exopps': 'http://export.com/exopps',
            'services_get_finance': 'http://export.com/get-finance',
            'services_events': 'http://export.com/events',
            'info_about': 'http://about.com',
            'info_contact_us': 'http://contact.com',
        }
    }
    html = render_to_string(template_name, context)
    header_footer_urls = context['header_footer_urls']
    assert header_footer_urls['great_home'] in html
    assert header_footer_urls['great_export_home'] in html
    assert header_footer_urls['new_to_exporting'] in html
    assert header_footer_urls['occasional_exporter'] in html
    assert header_footer_urls['regular_exporter'] in html
    assert header_footer_urls['services_fab'] in html
    assert header_footer_urls['services_soo'] in html
    assert header_footer_urls['services_exopps'] in html
    assert header_footer_urls['services_get_finance'] in html
    assert header_footer_urls['services_events'] in html
    assert header_footer_urls['info_about'] in html
    assert header_footer_urls['info_contact_us'] in html


def test_urls_exist_in_new_footer():
    template_name = 'directory_header_footer/footer.html'
    context = {
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
    html = render_to_string(template_name, context)
    header_footer_urls = context['header_footer_urls']
    assert header_footer_urls['great_home'] in html
    assert header_footer_urls['great_export_home'] in html
    assert header_footer_urls['new_to_exporting'] in html
    assert header_footer_urls['occasional_exporter'] in html
    assert header_footer_urls['regular_exporter'] in html
    assert header_footer_urls['guidance_market_research'] in html
    assert header_footer_urls['guidance_customer_insight'] in html
    assert header_footer_urls['guidance_finance'] in html
    assert header_footer_urls['guidance_business_planning'] in html
    assert header_footer_urls['guidance_getting_paid'] in html
    assert header_footer_urls['guidance_operations_and_compliance'] in html
    assert header_footer_urls['services_fab'] in html
    assert header_footer_urls['services_soo'] in html
    assert header_footer_urls['services_exopps'] in html
    assert header_footer_urls['services_get_finance'] in html
    assert header_footer_urls['services_events'] in html
    assert header_footer_urls['info_about'] in html
    assert header_footer_urls['info_contact_us'] in html
    assert header_footer_urls['info_privacy_and_cookies'] in html
    assert header_footer_urls['info_terms_and_conditions'] in html
    assert header_footer_urls['info_dit'] in html


def test_urls_exist_in_old_footer():
    template_name = 'directory_header_footer/footer_old.html'
    context = {
        'header_footer_urls': {
            'great_export_home': 'http://export.com',
            'new_to_exporting': 'http://export.com/new',
            'occasional_exporter': 'http://export.com/occasional',
            'regular_exporter': 'http://export.com/regular',
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
    html = render_to_string(template_name, context)
    header_footer_urls = context['header_footer_urls']
    assert header_footer_urls['great_export_home'] in html
    assert header_footer_urls['new_to_exporting'] in html
    assert header_footer_urls['occasional_exporter'] in html
    assert header_footer_urls['regular_exporter'] in html
    assert header_footer_urls['services_fab'] in html
    assert header_footer_urls['services_soo'] in html
    assert header_footer_urls['services_exopps'] in html
    assert header_footer_urls['services_get_finance'] in html
    assert header_footer_urls['services_events'] in html
    assert header_footer_urls['info_about'] in html
    assert header_footer_urls['info_contact_us'] in html
    assert header_footer_urls['info_privacy_and_cookies'] in html
    assert header_footer_urls['info_terms_and_conditions'] in html
    assert header_footer_urls['info_dit'] in html
