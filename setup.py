from setuptools import setup, find_packages
version = '0.0.1'
requires = []


setup(name='daisydukes',
    version=version,
    description="Set up a minimal, yet comfortable structure \
        for a Python project",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    keywords='python development project packaging, deployment',
    author='Ross Delinger',
    author_email='ross.delinger@gmail.com',
    url='https://github.com/rossdylan/daisydukes',
    license='GPLv3+',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points="""
    [console_scripts]
      daisydukes = daisydukes:DaisyDukesRunner
    """)
