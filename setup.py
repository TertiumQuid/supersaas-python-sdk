from setuptools import setup, find_packages

setup(
    name='supersaas-python-sdk',
    version='0.1.0',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    description='Online bookings/appointments/calendars using the SuperSaaS scheduling platform',
    author='Travis Dunn',
    author_email='travis@supersaas.com',
    keywords=['online appointment schedule', 'booking calendar', 'appointment book', 'reservation system', 
              'scheduling software', 'online booking system', 'scheduling system'],
    url='github.com/tertiumQuid/supersaas-python-sdk',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
