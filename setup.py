from setuptools import setup


setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/rherrerarayo/sklearn_transforms/',
      author='ROSA HERRERA',
      author_email='rkatherine-h@hotmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False
)
