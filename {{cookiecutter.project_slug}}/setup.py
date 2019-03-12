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
    # packages=find_packages('src', exclude=['ez_setup']),
    # package_dir={'': 'src'},
    namespace_packages=['{{cookiecutter.project_slug}}'],
    license='{{cookiecutter.license}}',
    packages=['{{cookiecutter.project_slug}}'],
    install_requires=[
        'rvit @ git+https://github.com/flaviusb/rvit',
        'kivy @ git+https://github.com/flaviusb/kivy.git@change_check_for_cython',
        'cython',
        'jinja2',
        'numpy',
        'pygame',
    ],
    include_package_data=True,
    zip_safe=False,
)

