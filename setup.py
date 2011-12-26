from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='reviewboard-svn-hooks',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='reviewboard svn subversion hook',
      author='LaiYonghao',
      author_email='mail@laiyonghao.com',
      url='http://code.google.com/p/reviewboard-svn-hooks/',
      license='mit',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      init_used_rid_db = reviewboardsvnhooks.init_used_rid_db:main
      strict_review = reviewboardsvnhooks.strict_review:main
      """,
      )
