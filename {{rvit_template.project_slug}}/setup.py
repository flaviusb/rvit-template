from setuptools import setup

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
{{rvit_template.license_long}}
Operating System :: OS Independent
Programming Language :: Python :: 3
""".strip().splitlines()


setup(
    name='{{rvit_template.project_name}}',
    version='{{rvit_template.version}}',
    classifiers=classifiers,
    description='description of your app',
    url='',
    author='{{rvit_template.author_name}}',
    author_email='',
    # packages=find_packages('src', exclude=['ez_setup']),
    # package_dir={'': 'src'},
    namespace_packages=['{{rvit_template.project_slug}}'],
    license='{{rvit_template.license}}',
    packages=['{{rvit_template.project_slug}}'],
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

