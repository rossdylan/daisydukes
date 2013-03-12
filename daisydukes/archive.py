from subprocess import check_call
from shlex import split


exclude_list = ["*.pyc"]
exclude = " ".join(exclude_list)


def createArchiveName(name, version, ext):
    return "{}-{}.{}".format(name, version, ext)


def getFilesList(packages):
    files_list = map(lambda f: "/".join(f.split(".")), packages)
    files_list.append("setup.py")
    files_list.append("README*")
    return files_list


def ArchiveZip(proj_info):
    aname = createArchiveName(
        proj_info['name'],
        proj_info['version'],
        'zip'
    )
    files_list = getFilesList(proj_info['packages'])
    zip_command = "zip {} {} -x {} ".format(aname, " ".join(files_list), exclude)
    check_call(split(zip_command))
