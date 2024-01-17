from setuptools import setup, find_packages

setup(
    name='CodeAnalysisTool',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for code analysis, enhancement, review, and learning with AI capabilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/CodeAnalysisTool',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'radon',
        'flake8',
        'bandit',
        'mypy',
        'black',
        'isort',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'analyze=main:analyze_code',
            'enhance=main:enhance_code',
            'review=main:review_code',
            'learn=main:learn_from_code',
            'openai-util=main:generate_response'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)