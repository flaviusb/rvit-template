from setuptools import setup

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
{{cookiecutter.license_long}}
Operating System :: OS Independent
Programming Language :: Python :: 3
""".strip().splitlines()


setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.version}}',
    classifiers=classifiers,
    description='description of your app',
    url='',
    author='{{cookiecutter.author_name}}',
    author_email='',
    #namespace_packages=['{{cookiecutter.project_slug}}'],
    license='{{cookiecutter.license}}',
    packages=['{{cookiecutter.project_slug}}'],
    install_requires=[
        'rvit @ git+https://github.com/flaviusb/rvit.git@widgets',
        'kivy @ git+https://github.com/flaviusb/kivy.git@change_check_for_cython',
        'cython',
        'jinja2',
        'numpy',
        'pygame',
    ],
    entry_points={
        'gui_scripts': [
            '{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}:start',
        ]
    },
    include_package_data=True,
    zip_safe=False,
)

