from setuptools import setup, find_packages

setup(
    name="pyweather",
    install_requires=[
        'requests >= 1.0.3',
    ],
    packages=find_packages('.'),
    package_dir={'': '.'},
    version="1.0.2",
    description="wunderground.com client",
    long_description=open('README.rst').read(-1),
    author="Tomas Zulberti",
    author_email="tzulberti@gmail.com",
    url="https://github.com/tzulberti/pyweather.git",
    zip_safe=False,
    keywords=[
        "weather",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Environment :: Web Environment',
        'Operating System :: OS Independent'
        ],
    license='License :: OSI Approved :: BSD License',
)
