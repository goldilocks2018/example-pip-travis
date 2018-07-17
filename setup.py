from setuptools import setup, find_packages

package_name = "copilot_example_pip_travis"
package_version = "1.0.1"

setup(
    name=package_name,
    version=package_version,
    author="Black Duck CoPilot",
    author_email="copilot@blackducksoftware.com",
    url="https://github.com/BlackDuckCoPilot/example-pip-travis",
    install_requires=[
                        "gunicorn==19.4.5", "Kotti==0.5.0a6", "markdown2==2.3.5", "moin==1.9.5",
                        "oauth2==1.5.153", "pycares==1.0.0", "pymongo==2.4.2", "PyYAML==3.11",
                        "qutebrowser==0.6.1", "recurly==2.6.0", "rsa==3.1.1", "topydo==0.13", "iso8601<=0.1.11",
                        "apache-libcloud==0.13.2", "oslo.middleware==2.0.0",
                        "Products.CMFEditions==2.0b7", "ovs==2.7.0",
                        "manila-ui==2.2.0", "django-tastypie==0.9.9",
                        "tlslite-ng==0.5.1", "aodh==2.0.0.0b2", "graphite-web==0.9.6"
                        ],
    entry_points={
        'console_scripts': ['example-pip-travis=Main:main' ]
    }
)
