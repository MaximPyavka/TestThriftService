from setuptools import setup

setup(name='thrift_test',
      version='1.0',
      author='Max Pyavka',
      author_email='kokoko@gmail.com',
      url='https://www.kokoko.com',
      packages=['matrix', 'vector', 'async_service'],
      package_data={
          '': ["*.md", "*.thrift", "*.txt"],
      },
      install_requires=["thrift==0.13.0", "pythonnet==2.4.0"]
      )
