import util
import sys
import argparse


def DaisyDukesRunner():
    if len(sys.argv) >= 2:
        cmd = sys.argv[1]
        if cmd == 'archive':
            Archive()
        elif cmd == 'upload':
            Upload()
        elif cmd == 'package':
            Package()
        else:
            Help()
    else:
        Help()


def Help():
    print("daisydukes: archive|upload|package")


def Archive():
    """
    Create a archive of this pythong project
    supports tar.* and zip
    """
    parser = argparse.ArgumentParser(description="Create an archive out of a pythong project")
    parser.add_argument('--zip',
                        action='store_true',
                        help='Archive this pythong project as a zip file')
    parser.add_argument('--gzip',
                        action='store_true',
                        help='Archive this pythong project as a tar.gz file')
    parser.add_argument('--bzip',
                        action='store_true',
                        help='Archive this pythong project as a tar.bz2 file')
    parser.add_argument('--lzma',
                        action='store_true',
                        help='Archive this pythong project as a tar.lzma file')
    parser.add_argument('--xz',
                        action='store_true',
                        help='Archive this pythong project as a tar.xz file')
    args = parser.parse_args(sys.argv[1:])


def Upload():
    """
    Upload a pythong project
    Supports: PyPI, FTP, S3
    """
    pass


def Package():
    """
    Package a pythong project as a deb or rpm
    """
    pass
