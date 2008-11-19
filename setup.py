"""
Setup for the Sass Pygments Lexer
"""
from setuptools import setup

__author__ = 'chris@eppsteins.net'

setup(
    name='Sass Pygments Lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['sass_lexer'],
    entry_points='''[pygments.lexers]
sasslexer = sass_lexer:SassLexer
'''
)
