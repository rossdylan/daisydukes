from subprocess import check_call
from shlex import split


exclude_list = ["*.pyc", ".ropeproject"]
exclude = " ".join(exclude_list)


def createArchiveName(name, version, ext):
    return "{}-{}.{}".format(name, version, ext)


def getFilesList(packages):
    files_list = map(lambda f: "/".join(f.split(".")), packages)
    files_list.append("setup.py")
    files_list.append("README")
    return files_list


def ArchiveZip(proj_info, extra_files):
    aname = createArchiveName(
        proj_info['name'],
        proj_info['version'],
        'zip'
    )
    files_list = getFilesList(proj_info['packages'])
    files_list.extend(extra_files)
    zip_command = "zip -r {} {} -x {} ".format(aname, " ".join(files_list), exclude)
    check_call(split(zip_command))


def ArchiveTar(proj_info, extra_files, format):
    aname = createArchiveName(
        proj_info['name'],
        proj_info['version'],
        'tar.{}'.format(format)
    )
    files_list = getFilesList(proj_info['packages'])
    files_list.extend(extra_files)
    tar_excludes = " ".join(map(lambda s: "--exclude={}".format(s), exclude_list))
    tar_command = "tar -caf {} {} {}".format(aname, " ".join(files_list), tar_excludes)
    check_call(split(tar_command))


