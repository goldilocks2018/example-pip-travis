from setuptools import setup, find_packages

package_name = "copilot_example_pip_travis"
package_version = "1.0.0"

setup(
    name=package_name,
    version=package_version,
    author="Black Duck CoPilot",
    author_email="copilot@blackducksoftware.com",
    url="https://github.com/BlackDuckCoPilot/example-pip-travis",
    install_requires=["requests", "numpy", "Django", "pathlib",
                        "gunicorn==19.4.5", "Kotti==0.5.0a6", "markdown2==2.3.5", "moin==1.9.5",
                        "oauth2==1.5.153", "pycares==1.0.0", "pymongo==2.4.2", "PyYAML==3.11",
                        "qutebrowser==0.6.1", "recurly==2.6.0", "rsa==3.1.1", "topydo==0.13",
                        "Zope2==2.12.2",
                        "apache-libcloud==0.13.2", "oslo.middleware==2.0.0",
                        "Products.CMFEditions==2.0b7", "ovs==2.7.0",
                        "manila-ui==2.2.0", "django-tastypie==0.9.9",
                        "tlslite-ng==0.5.1", "aodh==2.0.0.0b2", "graphite-web==0.9.6",
                        "priority==1.1.1", "django-anymail==1.2.1", "mysql-connector==2.1.3",
                        "tripleo-image-elements==0.8.1", "tile-generator==5.0.7",
                        "owlmixin==2.0.0a6", "Products.kupu==1.4.16",
                        "ansible==1.8.3", "ansible-vault==1.0.4", "archmage==0.3", "askbot==0.7.37",
                        "asyncssh==1.5.1", "Bcfg2==1.2.0", "Beaker==1.6.4", "bleach==2.1", "bottle==0.11.1",
                        "celery==2.4.0", "ceph-deploy==1.5.22", "confire==0.2.0",
                        "cryptography==1.5.2", "Django==1.4.2", "django_make_app==0.1.3", "django-cms==3.0.13",
                        "django-markupfield==1.3.1", "Djblets==0.8.1", "docker-py==0.5.3", "dulwich==0.9.8", "Fabric==0.9.5",
                        "fedmsg==0.18.1", "feedparser==5.0", "hpack==2.0.1", "html5lib==0.99999999",
                        "httplib2==0.8", "instack-undercloud==7.2.0", "ipython==3.2.1", "Jinja2==2.5.5", "jwcrypto==0.3.1",
                        "Kallithea==0.3.1", "keyring==0.9.1", "keystonemiddleware==1.5.0", "koji==1.15.0",
                        "logilab-common==0.60.0", "lxml==2.2.6", "Mako==0.3.3", "MapProxy==1.10.3", "Mercurial==3.0",
                        "mistune==0.7.2", "mlalchemy==0.1.2", "murano==1.0.2", "murano-dashboard==1.0.2",
                        "notebook==5.2.1", "nova-lxd==13.1.0", "numpy==1.6.0", "openpyxl==2.4.1",
                        "paramiko==2.4.0", "Paste==1.7.5", "Pillow==2.8.0", "pip==1.2", "Plone==4.3.15",
                        "pycrypto==2.1.0", "pyfribidi==0.10.0", "pyftpdlib==0.2.0", "Pygments==2.0", "PyJWT==1.5.0",
                        "pykerberos==1.1.4", "pysaml2==1.0.2", "python-bugzilla==0.8.0", "python-cjson==1.0.5",
                        "python-docx==0.8.5", "python-fedora==0.8.0", "python-glanceclient==0.7.0", "python-gnupg==0.3.5",
                        "python-jose==1.3.1", "python-keystoneclient==1.7.0", "python-muranoclient==0.7.2", "pywbem==0.7.0",
                        "PyWebDAV==0.9.3", "pyxdg==0.25", "Radicale==1.0.1", "requests==2.4.1", "restkit==2.1.0",
                        "salt==0.10.3", "Sanic==0.5.0", "Scrapy==0.24.6", "sleekxmpp==1.3.1", 
                        "SOAPpy==0.12.5", "sosreport==3.2", "supervisor==3.1.2", "swauth==1.2.0", "swift==1.0.2", "tablib==0.11.4",
                        "textract==1.4.0", "tlslite==0.4.9", "tornado==1.2", "tqdm==4.4.1", "tripleo-heat-templates==0.6.4",
                        "tryton==3.8.7", "trytond==3.4.7", "tweepy==1.4", "txAWS==0.2.3.1", "urllib3==1.18",
                        "Werkzeug==0.11"],
    entry_points={
        'console_scripts': [ ]
    }
)
