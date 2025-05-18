from setuptools import setup

APP = ['convertidor_img.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': [],  # add any additional packages you use (like 'PIL', etc.)
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)