from setuptools import setup, find_packages

setup(
    name='DeepSeek-Coder',
    version='0.1.0',
    author='DeepSeek AI',
    author_email='info@deepseek.ai',
    description='A tool to clone and enhance codebases using DeepSeeker AI technologies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deepseek-ai/DeepSeek-Coder.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'deepseeker=deepseeker.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)