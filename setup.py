import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(name='gym_karmedbandits',
      version='0.0.1',
      url="https://github.com/NoblesseCoder/karmedbandits",
      author="Ashik Poovanna",
      author_email="ashobot@gmail.com"	
      description='k-armed bandits environment for OpenAI Gym',
      long_description=README,
      long_description_content_type="text/markdown",
      license='MIT License',
      install_requires=['gym','numpy'])
