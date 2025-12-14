from setuptools import find_packages, setup

setup(
    name='django-node-modules',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    author_email='magilyas.doma.09@list.ru',
    author='Маг Ильяс DOMA (MagIlyasDOMA)',
    url='https://github.com/magilyasdoma/django-node-modules',
    install_requires=[
        'filetype>=1.2.0',
        'django==5.2.9',
        'django-static-engine>=0.1.6, <0.2.0'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
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
