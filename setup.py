from distutils.core import setup

setup(
    name='assemblyai-cli',
    description='AssemblyAI Command Line Interface',
    author='Evan Hallmark',
    author_email='evan@ehallmarksolutions.com',
    version='0.3',
    license='MIT',
    url='https://github.com/AssemblyAI/assemblyai-cli',
    download_url='https://github.com/AssemblyAI/assemblyai-cli/archive/v0.3.tar.gz',
    packages=['', 'modules'],
    package_dir={'': 'src'},
    install_requires=['requests', 'future'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': ['assemblyai=assemblyai:main'],
    }
)