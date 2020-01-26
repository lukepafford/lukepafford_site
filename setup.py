from setuptools import setup, find_packages

setup(
    name="django-lukepafford-blog",
    version="1.0.19",
    description="Django site for personal blog, and anything else",
    url="https://github.com/lukepafford/lukepafford_site",
    author="Luke Pafford",
    author_email="lukepafford@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="blog django",
    package_dir={"": "lukepafford_blog"},
    packages=find_packages("lukepafford_blog"),
    include_package_data=True,
    install_requires=[
        "django",
        "django-allauth",
        "django-environ",
        "django-markdown-deux",
        "pyyaml",
        "gunicorn",
    ],
)
