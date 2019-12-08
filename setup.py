from io import open
from setuptools import find_packages, setup


extras = {
    'serving': ['uvicorn', 'fastapi']
}
extras['all'] = [package for package in extras.values()]

setup(
    name="transformers-vectorizer",
    version="0.0.1",
    author="Radhwane Chebaane",
    author_email="radcheb@gmail.com",
    description="Extract numerical vectors out of text using transformers",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords='NLP deep learning transformer pytorch BERT',
    license='Apache',
    url="https://github.com/radcheb/transformers-vectorizer",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    install_requires=['numpy',
                      'boto3',
                      'requests',
                      'tqdm',
                      'regex',
                      'sentencepiece',
                      'sacremoses'],
    extras_require=extras,
    # python_requires='>=3.5.0',
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)