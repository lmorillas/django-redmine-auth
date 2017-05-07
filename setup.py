from setuptools import setup
import os

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-redmine-auth',
    version='1.1',
    packages=['redmine_auth'],
    include_package_data=False,
    license='BSD License',
    description='Django app for redmine authentication',
    long_description=README,
    url='https://github.com/JulienDrecq/django-redmine-auth',
    author='Julien DRECQ',
    author_email='drecq.julien@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
