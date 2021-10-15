from setuptools import find_packages, setup


"""install_requires = [
    'click==7.1.2',
    'pandas-profiling'
]

install_requires=install_requires,
"""

setup(
    name='Flashcards',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

