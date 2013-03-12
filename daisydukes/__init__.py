import util
import sys
import argparse
import archive


def DaisyDukesRunner():
    if len(sys.argv) >= 2:
        cmd = sys.argv[1]
        if cmd == 'archive' or cmd == 'fold':
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
    parser.add_argument('--extrafiles',
                        metavar='F', type=str, nargs='+',default=[],
                        help='A list of extra files to add to the archive')
    args = parser.parse_args(sys.argv[2:])
    proj_info = util.trap_setup()[1]
    if args.zip:
        archive.ArchiveZip(proj_info, args.extrafiles)
    elif args.gzip:
        archive.ArchiveTar(proj_info, args.extrafiles, 'gz')
    elif args.bzip:
        archive.ArchiveTar(proj_info, args.extrafiles, 'bz2')
    elif args.lzma:
        archive.ArchiveTar(proj_info, args.extrafiles, 'lzma')
    elif args.xz:
        archive.ArchiveTar(proj_info, args.extrafiles, 'xz')
    else:
        archive.ArchiveZip(util.trap_setup()[1], args.extrafiles)


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
