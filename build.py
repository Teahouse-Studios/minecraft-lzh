import zipfile
import json
import argparse
import os

# Thanks to MysticNebula70

def main():
    parser = argparse.ArgumentParser(description="Automatic build resourcepacks")
    parser.add_argument('type', default='normal', help="Build type. Should be 'all', 'normal' or 'leaveblank'.")
    args = vars(parser.parse_args())
    if args['type'] == 'all':
        build_all()
    else:
        build(args)
    print("Build succeeded!")

def build(args):
    with open("assets/minecraft/lang/lzh.json", 'r', encoding='utf8') as f:
        lang_data = json.load(f)
    pack_name = get_packname(args)
    # all builds have these files
    pack = zipfile.ZipFile(pack_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5)
    pack.write("LICENSE")
    pack.write("pack.mcmeta")
    if args['type'] == 'normal':
        # normal build
        # delete untranslated strings, by chyx
        lang_data = {k:v for k,v in lang_data.items() if v}
        pack.writestr("assets/minecraft/lang/lzh.json", json.dumps(lang_data, indent=4, ensure_ascii=True))
    elif args['type'] == 'leaveblank':
        pack.writestr("assets/minecraft/lang/lzh.json", json.dumps(lang_data, indent=4, ensure_ascii=True))
    pack.close()

def build_all():
    build({'type': 'normal'})
    build({'type': 'leaveblank'})

def get_packname(args):
    base_name = "lzh"
    if args['type'] == 'normal':
        pass
    elif args['type'] == 'leaveblank':
        base_name = base_name + "_leaveblank"
    return base_name + ".zip"

if __name__ == "__main__":
    main()