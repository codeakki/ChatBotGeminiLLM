from setuptools import find_packages,setup

setup(
    name='chatbot',
    version='0.0.1',
    author='akki',
    author_email='codewithakki',
    install_requires=["google-generativeai","streamlit","python-dotenv"],
    packages=find_packages()
)