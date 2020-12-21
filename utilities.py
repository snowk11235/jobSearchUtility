"""
Utility functions
------------------
Author:K.*
re-worked 12/21/20
"""
from bs4 import BeautifulSoup



def strip_job_description_extras(muddy_text):
    soup = BeautifulSoup(muddy_text, features="html.parser")
    stripped_text = soup.get_text()
    return stripped_text