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
                        "cryptography==1.5.2", "Django==1.4.2", "django_make_app==0.1.3", "django-cms==3.0.13"],
    entry_points={
        'console_scripts': [
            'example-pip-travis=Main:main'
        ]
    }
)
