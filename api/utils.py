import dns.resolver
import dns.exception

from re import match
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def validate_email_domain(email):
    BANNED_DOMAINS = ['gmail.com', 'icloud.com']
    domain = email.split('@')[1].lower()

    if domain in BANNED_DOMAINS:
        raise ValidationError(_('You cannot use \'%(domain)s\' domain'), params={'domain': domain},)
    else:
        try:
            dns.resolver.resolve(domain, 'MX')
        except dns.exception.DNSException as e:
            print('Domain does not exist', e)
            raise ValidationError(_('Domain \'%(domain)s\' could not be found :('), params={'domain': domain},)


def validate_password(password):
    if not match(r'^[A-Z](?=.*[0-9])(?=.*[a-zA-Z])(?=.*[_])[a-zA-Z0-9_]+$', password):
        print('Invalid password')
        raise ValidationError(_('Password must contain alphanumeric characters, underscores and starts with '
                                'a capital letter. Length: [7-16] characters.'), code='invalid')


def validate_first_name(first_name):
    if not match(r'^[a-zA-Z-]+$', first_name):
        print('Invalid First Name')
        raise ValidationError(_('First name must contain only latin letters and dashes.'), code='invalid')


def validate_last_name(last_name):
    if not match(r'^[a-zA-Z- ]+$', last_name):
        print('Invalid Last Name')
        raise ValidationError(_('Last name must contain only latin letters, dashes and spaces.'), code='invalid')
