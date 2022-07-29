from saml2.saml import NAMEID_FORMAT_TRANSIENT
from saml2.sigver import get_xmlsec_binary
import os
import saml2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SPID_BASE_URL = os.environ.get('SPID_BASE_URL', "https://localhost:8000")
SPID_URLS_PREFIX = 'spid'

SPID_ACS_URL_PATH = f'{SPID_URLS_PREFIX}/acs/'
SPID_SLO_POST_URL_PATH = f'{SPID_URLS_PREFIX}/ls/post/'
SPID_SLO_URL_PATH = f'{SPID_URLS_PREFIX}/ls/'
SPID_METADATA_URL_PATH = f'{SPID_URLS_PREFIX}/metadata/'

LOGIN_URL = f'/{SPID_URLS_PREFIX}/login'
LOGOUT_URL = f'/{SPID_URLS_PREFIX}/logout'
LOGIN_REDIRECT_URL = f'/{SPID_URLS_PREFIX}/echo_attributes'
LOGOUT_REDIRECT_URL = '/'

SAML2_DEFAULT_BINDING = saml2.BINDING_HTTP_POST
SPID_DIG_ALG = saml2.xmldsig.DIGEST_SHA256
SPID_SIG_ALG = saml2.xmldsig.SIG_RSA_SHA256
SPID_NAMEID_FORMAT = NAMEID_FORMAT_TRANSIENT
SPID_AUTH_CONTEXT = 'https://www.spid.gov.it/SpidL1'

SPID_CERTS_DIR = os.path.join(os.environ.get('PWD'), 'certificates/')
SPID_PUBLIC_CERT = os.path.join(SPID_CERTS_DIR, 'public.cert')
SPID_PRIVATE_KEY = os.path.join(SPID_CERTS_DIR, 'private.key')

# source: https://registry.spid.gov.it/identity-providers
SPID_IDENTITY_PROVIDERS_URL = 'https://registry.spid.gov.it/assets/data/idp.json'
SPID_IDENTITY_PROVIDERS_METADATA_DIR = os.path.join(BASE_DIR, 'spid_config/metadata/')

<<<<<<< HEAD
SPID_SAML_CHECK_REMOTE_METADATA_ACTIVE = os.environ.get('SPID_SAML_CHECK_REMOTE_METADATA_ACTIVE', '0') == '1'
SPID_SAML_CHECK_METADATA_URL = os.environ.get('SPID_SAML_CHECK_METADATA_URL', 'http://localhost:8080/metadata.xml')

SPID_TESTENV2_REMOTE_METADATA_ACTIVE = os.environ.get('SPID_TESTENV2_REMOTE_METADATA_ACTIVE', '0') == '1'
SPID_TESTENV2_METADATA_URL = os.environ.get('SPID_TESTENV2_METADATA_URL', 'http://localhost:8088/metadata')
=======
SPID_SAML_CHECK_IDP_ACTIVE = os.environ.get('SPID_SAML_CHECK_IDP_ACTIVE', 'False') == 'True'
SPID_SAML_CHECK_METADATA_URL = os.environ.get('SPID_SAML_CHECK_METADATA_URL', 'https://localhost:8080/metadata.xml')

SPID_DEMO_IDP_ACTIVE = os.environ.get('SPID_DEMO_IDP_ACTIVE', 'False') == 'True'
SPID_DEMO_METADATA_URL = os.environ.get('SPID_DEMO_METADATA_URL', 'https://localhost:8080/demo/metadata.xml')

SPID_VALIDATOR_IDP_ACTIVE = os.environ.get('SPID_VALIDATOR_IDP_ACTIVE', 'False') == 'True'
SPID_VALIDATOR_METADATA_URL = os.environ.get('SPID_VALIDATOR_METADATA_URL', "https://validator.spid.gov.it/metadata.xml")

>>>>>>> main

# Avviso 29v3
SPID_PREFIXES = dict(
    spid='https://spid.gov.it/saml-extensions',
    fpa='https://spid.gov.it/invoicing-extensions'
)

# Avviso SPID n. 19 v.4 per enti AGGREGATORI aggiungere chiave vuota PublicServicesFullOperator
# Il plugin genererà automaticamente anche il tag ContactPerson con l’attributo spid:entityType valorizzato a spid:aggregator

SPID_CONTACTS = [
    {
        'contact_type': 'other',
        'telephone_number': '+398475634785',
        'email_address': 'tech-info@example.org',
        'IPACode': 'that-IPA-code',
        'VATNumber': 'IT12345678901',
        'FiscalCode': 'XYZABCAAMGGJ000W',
<<<<<<< HEAD
        'Private': '',
        # 'PublicServicesFullOperator':''
=======
        'Public': '',
        #'PublicServicesFullOperator':''
>>>>>>> main
    },
    # {
    # 'contact_type': 'billing',
    # 'telephone_number': '+39 84756344785',
    # 'email_address': 'info@example.org',
    # 'company': 'example s.p.a.',
    ## 'CodiceFiscale': 'NGLMRA80A01D086T',
    # 'IdCodice': '983745349857',
    # 'IdPaese': 'IT',
    # 'Denominazione': 'Destinatario Fatturazione',
    # 'Indirizzo': 'via tante cose',
    # 'NumeroCivico': '12',
    # 'CAP': '87100',
    # 'Comune': 'Cosenza',
    # 'Provincia': 'CS',
    # 'Nazione': 'IT',
    # },
]

<<<<<<< HEAD
# new features parameter
SPID_CURRENT_INDEX: int = int(os.getenv("SPID_CURRENT_INDEX", "0"), 10)  # in my case export SPID_CURRENT_INDEX=1

SAML_ATTRIBUTE_CONSUMING_SERVICE_LIST = [
    {
        "serviceNames": (
            {"lang": "en", "text": "service #1"},
            {"lang": "it", "text": "servizio #1"},
        ),
        "serviceDescriptions": (
            {"lang": "en", "text": "description of service #1"},
            {"lang": "it", "text": "descrizione del servizio #1"},
        ),
        "attributes": ("spidCode", "fiscalNumber", "email", "name", "familyName", "placeOfBirth", "dateOfBirth",)
    }
]

assertion_consumer_service = [
    (f'{SPID_BASE_SCHEMA_HOST_PORT}/{SPID_ACS_URL_PATH}', saml2.BINDING_HTTP_POST),
]

single_logout_service = [
    (f'{SPID_BASE_SCHEMA_HOST_PORT}/{SPID_SLO_POST_URL_PATH}', saml2.BINDING_HTTP_POST),
    # (f'{SPID_BASE_SCHEMA_HOST_PORT}/{SPID_SLO_URL_PATH}', saml2.BINDING_HTTP_REDIRECT),
]

encryption_keypairs = [{
    'key_file': SPID_PRIVATE_KEY,
    'cert_file': SPID_PUBLIC_CERT,
}]

if 1 == SPID_CURRENT_INDEX:
    assertion_consumer_service.insert(0, (f'https://previousservice.example.it/acs', SPID_DEFAULT_BINDING))

    single_logout_service.insert(0, (f'https://previousservice.example.it/ls/post', SPID_DEFAULT_BINDING))

    encryption_keypairs.insert(0,
                               {
                                   # use private key of current production service (index="0")
                                   'key_file': SPID_PRIVATE_KEY,
                                   # use public crt of current production service (index="0")
                                   'cert_file': SPID_PUBLIC_CERT,

                               })

    SAML_ATTRIBUTE_CONSUMING_SERVICE_LIST.append(
        {
            "serviceNames": (
                {"lang": "en", "text": "service #2"},
                {"lang": "it", "text": "servizio #2"},
            ),
            "serviceDescriptions": (
                {"lang": "en", "text": "description of service #2"},
                {"lang": "it", "text": "descrizione del servizio #2"},
            ),
            "attributes": ("spidCode", "fiscalNumber", "email", "name", "familyName",)
        }
    )

SAML_CONFIG = {
    'debug': True,
    'xmlsec_binary': get_xmlsec_binary(['/opt/local/bin', '/usr/bin/xmlsec1']),

    # Avviso SPID n. 19 v.4 per enti AGGREGATORI l’entityID deve contenere il codice attività pub-op-full
    # 'entityid': f'{BASE_URL}/pub-op-full/',
    'entityid': f'{SPID_BASE_URL}/metadata',

    # Attribute maps moved to src/djangosaml2_spid/attribute_maps/
    # 'attribute_map_dir': f'{BASE_DIR}/spid_config/attribute-maps/',

    'service': {
        'sp': {
            'name': f'{SPID_BASE_URL}/metadata/',
            'name_qualifier': SPID_BASE_SCHEMA_HOST_PORT,

            'name_id_format': [SPID_NAMEID_FORMAT],

            'endpoints': {
                'assertion_consumer_service': assertion_consumer_service,
                'single_logout_service': single_logout_service
            },

            # Mandates that the IdP MUST authenticate the presenter directly
            # rather than rely on a previous security context.
            'force_authn': False,  # SPID
            'name_id_format_allow_create': False,

            # attributes that this project need to identify a user
            'required_attributes': [
                'spidCode',
                'name',
                'familyName',
                'fiscalNumber',
                'email'
            ],

            'requested_attribute_name_format': saml2.saml.NAME_FORMAT_BASIC,
            'name_format': saml2.saml.NAME_FORMAT_BASIC,

            # attributes that may be useful to have but not required
            'optional_attributes': [
                'gender',
                'companyName',
                'registeredOffice',
                'ivaCode',
                'idCard',
                'digitalAddress',
                'placeOfBirth',
                'countyOfBirth',
                'dateOfBirth',
                'address',
                'mobilePhone',
                'expirationDate'
            ],

            'signing_algorithm': SPID_SIG_ALG,
            'digest_algorithm': SPID_DIG_ALG,

            'authn_requests_signed': True,
            'logout_requests_signed': True,

            # Indicates that Authentication Responses to this SP must
            # be signed. If set to True, the SP will not consume
            # any SAML Responses that are not signed.
            'want_assertions_signed': True,

            # When set to true, the SP will consume unsolicited SAML
            # Responses, i.e. SAML Responses for which it has not sent
            # a respective SAML Authentication Request.
            'allow_unsolicited': False,
=======
>>>>>>> main

CIE_CONTACTS = [
    {
        'contact_type': 'administrative',
        'IPACode': 'that-IPA-code',
        'VATNumber': 'IT12345678901',
        'FiscalCode': 'XYZABCAAMGGJ000W',
        'NACE2Code': '12.34.56',
        'Municipality': 'H501',
        'Province': 'CS',
        'Country': 'IT',
        'Company': 'same-to-OrganizationName-if-PA',
        'telephone_number': '+398475634785',
        'email_address': 'tech-info@example.org',
        'Public': '',
    },
    {
        'contact_type': 'technical',
        'telephone_number': '+39 84756344785',
        'email_address': 'info@example.org',
        'IPACode': 'that-IPA-code',
        'VATNumber': 'IT12345678901',
        'FiscalCode': 'XYZABCAAMGGJ000W',
        'NACE2Code': '12.34.56',
        'Municipality': 'H501',
        'Province': 'CS',
        'Country': 'IT',
        'Company': 'same-to-OrganizationName-if-PA',
        'telephone_number': '+398475634785',
        'email_address': 'tech-info@example.org',
    },
]

<<<<<<< HEAD
    # Signing
    'key_file': SPID_PRIVATE_KEY,
    'cert_file': SPID_PUBLIC_CERT,

    # Encryption
    'encryption_keypairs': encryption_keypairs,
=======
>>>>>>> main

# Configuration for pysaml2 as managed by djangosaml2. For SPID SP service the most
# part is built dynamically from provided SPID_* settings and from SPID_* defaults.
SAML_CONFIG = {
    # Required organization info, you can set multi-language information here.
    'organization': {
        'name': [('Example', 'it'), ('Example', 'en')],
        'display_name': [('Example', 'it'), ('Example', 'en')],
        'url': [('http://www.example.it', 'it'), ('http://www.example.it', 'en')],
    },

    # Other common options used by SPID configuration
    'debug': True,
    'xmlsec_binary': get_xmlsec_binary(['/opt/local/bin', '/usr/bin/xmlsec1']),

    "disable_ssl_certificate_validation": True,

    # The other entries are dynamically generated from SPID_* provided settings
    # and defaults. You can still provide those entries here but they can useful
    # only for other SAML2 service in your installation, not for SPID.
    #
    # If you want to provide a full static SAML_CONFIG you need to define also
    # SAML_CONFIG_LOADER setting, typically it can be set pointing to the default
    # djangosaml2's config loader function:
    #
    #   SAML_CONFIG_LOADER = 'djangosaml2.conf.config_settings_loader'
    #
}

# OR NAME_ID or MAIN_ATTRIBUTE (not together!)
SAML_USE_NAME_ID_AS_USERNAME = False

SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'username'
SAML_DJANGO_USER_MAIN_ATTRIBUTE_LOOKUP = '__iexact'

SAML_CREATE_UNKNOWN_USER = True

# logout
SAML_LOGOUT_REQUEST_PREFERRED_BINDING = saml2.BINDING_HTTP_POST

SAML_ATTRIBUTE_MAPPING = {
    'spidCode': ('username',),
    'fiscalNumber': ('tin',),
    'email': ('email',),
    'name': ('first_name',),
    'familyName': ('last_name',),
    'placeOfBirth': ('place_of_birth',),
    'dateOfBirth': ('birth_date',),
}

# Additional ACS
# new features parameter
SPID_CURRENT_INDEX: int = int(os.getenv("SPID_CURRENT_INDEX", "0"), 10)  # in my case export SPID_CURRENT_INDEX=1

SAML_ATTRIBUTE_CONSUMING_SERVICE_LIST = [
    {
        "serviceNames": (
            {"lang": "en", "text": "service #1"},
            {"lang": "it", "text": "servizio #1"},
        ),
        "serviceDescriptions": (
            {"lang": "en", "text": "description of service #1"},
            {"lang": "it", "text": "descrizione del servizio #1"},
        ),
        "attributes": ("spidCode", "fiscalNumber", "email", "name", "familyName", "placeOfBirth", "dateOfBirth",)
    }
]

if SPID_CURRENT_INDEX == 1:
    endpoints = SAML_CONFIG['service']['sp']['endpoints']
    endpoints['assertion_consumer_service'].insert(0, (f'https://previousservice.example.it/acs', SPID_DEFAULT_BINDING))

    single_logout_service.insert(0, (f'https://previousservice.example.it/ls/post', SPID_DEFAULT_BINDING))

    encryption_keypairs.insert(0,
                               {
                                   # use private key of current production service (index="0")
                                   'key_file': SPID_PRIVATE_KEY,
                                   # use public crt of current production service (index="0")
                                   'cert_file': SPID_PUBLIC_CERT,

                               })

    SAML_ATTRIBUTE_CONSUMING_SERVICE_LIST += [
        {
            "serviceNames": (
                {"lang": "en", "text": "service #2"},
                {"lang": "it", "text": "servizio #2"},
            ),
            "serviceDescriptions": (
                {"lang": "en", "text": "description of service #2"},
                {"lang": "it", "text": "descrizione del servizio #2"},
            ),
            "attributes": ("spidCode", "fiscalNumber", "email", "name", "familyName",)
        }
    ]
### end additiona ACS feature

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'detailed': {
            'format': '[%(asctime)s] %(message)s [(%(levelname)s)] %(args)s %(name)s %(filename)s.%(funcName)s:%(lineno)s]'
        },
        'json': {
            'format': '{"timestamp": "%(asctime)s", "msg": %(message)s, "level": "%(levelname)s",  "name": "%(name)s", "path": "%(filename)s.%(funcName)s:%(lineno)s", "@source":"django-audit"}'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'formatter': 'detailed',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'djangosaml2_spid.tests': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
