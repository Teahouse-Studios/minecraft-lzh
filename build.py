import os
from argparse import ArgumentParser
from packaging.pack_builder import pack_builder


def build(args):
    print(os.getcwd())
    builder = pack_builder(os.getcwd())
    builder.args = args
    builder.build()
    return builder.logs, builder.warning_count, builder.error_count


if __name__ == '__main__':
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
        for i in os.listdir('builds/'):
            os.remove(os.path.join('builds', i))
        print("\nDeleted all packs built.")
    else:
        build(args)
