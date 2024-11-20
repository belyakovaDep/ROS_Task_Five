from setuptools import find_packages, setup

package_name = 'robot_cycle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='belyakovaDep',
    maintainer_email='d.belyakova1@g.nsu.ru',
    description='Module 5 Task 4',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cycle = robot_cycle.circle_movement:main',
        ],
    },
)
