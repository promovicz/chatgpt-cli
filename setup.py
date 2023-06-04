import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="chatgpt-cli",
    version="0.1",
    author="Marco Lardera",
    author_email="larderamarco@hotmail.com",
    description="Simple script for chatting with ChatGPT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/marcolardera/chatgpt-cli",
    packages=['chatgptcli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "chatgpt-cli = chatgptcli.__main__:main",
        ],
    },
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
    package_data={'chatgptcli':['chatgpt.yaml']},
)
