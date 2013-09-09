from setuptools import setup


PACKAGE = "severities_extension"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="En extension to add severities to reviews in ReviewBoard",
    author="Taller Technologies",
    packages=["severities"],
    entry_points={
        'reviewboard.extensions':
            '%s = severities.extension:SeverityExtension' % PACKAGE,
    },
)