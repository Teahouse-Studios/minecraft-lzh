from os.path import join, dirname
from packaging.pack_builder import pack_builder


def build(args):
    current_dir = dirname(__file__)
    builder = pack_builder(
        join(current_dir, "minecraft-lzh"), join(current_dir, "mappings"))
    builder.args = args
    builder.build()
    return builder.filename, builder.warning_count, builder.error, builder.log_list


if __name__ == '__main__':
    from argparse import ArgumentParser
    from os import listdir, remove, curdir
    from os.path import exists, isdir

    def generate_parser():
        parser = ArgumentParser(description="Automatic build resourcepacks")
        parser.add_argument('type', default='normal', choices=('normal', 'compat', 'legacy'),
                            help='Build type. Should be "normal", "compat" or "legacy".')
        parser.add_argument('-b', '--leaveblank', action='store_true',
                            help="Leave all the blanks when building resource packs.")
        parser.add_argument('-f', '--format', type=int,
                            help='Specify "pack_format". when omitted, will default to 3 if build type is "legacy" and 6 if build type is "normal" or "compat". A wrong value will cause the build to fail.')
        parser.add_argument('-o', '--output', nargs='?', default='builds',
                            help="Specify the location to output packs. Default location is 'builds/' folder.")
        return parser
    args = vars(generate_parser().parse_args())
    if args['type'] == 'clean':
        target = join(curdir, args['output'])
        if exists(target) and isdir(target):
            for i in listdir(target):
                remove(join(target, i))
        print(f"Cleaned up {target}.")
    else:
        build(args)
