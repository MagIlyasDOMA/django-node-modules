from pip_setuptools import find_packages, setup, requirements, clean

clean()
setup(
    name='django-node-modules',
    version='1.0.6',
    packages=find_packages(),
    include_package_data=True,
    author_email='magilyas.doma.09@list.ru',
    author='Маг Ильяс DOMA (MagIlyasDOMA)',
    description="A Django application for easily managing and serving files from local node_modules and remote NPM packages directly from Django templates",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/magilyasdoma/django-node-modules',
    install_requires=requirements(),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    project_urls=dict(
        Source='https://github.com/magilyasdoma/django-node-modules',
        Documentation='https://github.com/magilyasdoma/django-node-modules/README.md',
        Tracker='https://github.com/magilyasdoma/django-node-modules/issues',
    ),
    python_requires='>=3.10',
    keywords=[
        'django',
        'node.js',
        'node',
        'nodejs',
        'npm',
        'static'
    ]
)
