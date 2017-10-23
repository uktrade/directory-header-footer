from django.template.loader import render_to_string
from bs4 import BeautifulSoup

import pytest


@pytest.mark.parametrize('template_name', (
    'directory_header_footer/header.html',
    'directory_header_footer/header_old.html'
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
    'directory_header_footer/header_old.html'
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
