from django.template.loader import render_to_string

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
