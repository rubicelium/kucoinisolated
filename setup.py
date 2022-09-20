from setuptools import setup


setup(
    name='newkucoin',
    version='v1.0',
    packages=['kucoin', 'kucoin/base_request', 'kucoin/margin', 'kucoin/market', 'kucoin/trade', 'kucoin/user',
              'kucoin/websocket', 'kucoin/ws_token'],
    license="MIT",
    author='Rubic',
    author_email="technology@rubicelium.io",
    url='https://github.com/rubicelium/newkucoin',
    description="newkucoin",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
