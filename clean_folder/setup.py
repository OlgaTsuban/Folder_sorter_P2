from setuptools import setup, find_namespace_packages 

setup( 
    name='clean_folder',
    version='0.0.1',
    description='Clean folder program by Python',
    author='tsubanolga',
    author_email='tsubanolga@gmail.com',
    url='https://github.com/OlgaTsuban/GoIT_homework6.git',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)