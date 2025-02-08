import os
from collections import OrderedDict
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    dependencies = f.read().strip().split("\n")

setup(
    name="securegpt",
    version="0.14.0",
    description="SecureGPT, a GPT-empowered penetration testing tool",
    long_description="""
    SecureGPT is a penetration testing tool empowered by ChatGPT.
    It is designed to automate the penetration testing process. It
    is prototyped initially on top of ChatGPT and operate in an
    interactive mode to guide penetration testers in both overall
    progress and specific operations.
    """,
    author="Gelei Deng",
    author_email="gelei.deng@ntu.edu.sg",
    maintainer="Gelei Deng",
    maintainer_email="gelei.deng@ntu.edu.sg",
    url="https://github.com/Zyph3rKeaton/SecureGPT",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/Zyph3rKeaton/SecureGPT"),
            ("Issue tracker", "https://github.com/Zyph3rKeaton/SecureGPT/issues"),
        )
    ),
    license="MIT License",
    packages=["securegpt"] + find_packages(),
    # packages=find_packages(),
    # scripts=['securegpt/main.py'],
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "securegpt=securegpt.main:main",
            "securegpt-cookie=securegpt.extract_cookie:main",
            "securegpt-connection=securegpt.test_connection:main",
        ]
    },
)
