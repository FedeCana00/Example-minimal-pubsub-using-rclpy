from setuptools import setup

package_name = 'py_subpub'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fede',
    maintainer_email='fede@todo.todo',
    description='Examples of minimal publisher/subsriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_subpub.publisher:main',
            'listener = py_subpub.subscriber:main'
        ],
    },
)
