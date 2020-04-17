from setuptools import setup, find_packages

setup(
    name="scheduler",
    version="0.1",
    packages=find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3"],
    package_data={},
    # metadata to display on PyPI
    author="Niels Warncke",
    author_email="niels.warncke@gmail.com",
    description="A simple scheduler, e.g. for training loops",
    keywords="schedule, training loop",
    classifiers=["License :: OSI Approved :: Python Software Foundation License"]
    # could also include long_description, download_url, etc.
)
