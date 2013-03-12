from subprocess import check_call
from shlex import split
import ftplib


def PyPIUpload(reg=False):
    if reg:
        check_call(split("python setup.py register"))
    check_call(split("python setup.py sdist upload"))

def S3Upload(proj_info, bucket, format):
    pass

def FTPUpload(proj_info, uri, format):
    pass
