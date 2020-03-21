import zipfile
import json
import argparse
import os

# Thanks to MysticNebula70

mappings = ['addServer', 'advancements', 'advMode', 'attribute', 'book', 'build', 'chat',
            'commands', 'connect', 'container', 'controls', 'createWorld', 'death',
            'deathScreen', 'debug', 'demo', 'difficulty', 'disconnect', 'effect',
            'enchantment', 'entity', 'filled_map', 'gameMode', 'generator', 'gui', 'inventory',
            'item', 'itemGroup', 'key', 'language', 'lanServer', 'lingering_potion',
            'mcoServer', 'menu', 'merchant', 'mount', 'multiplayer', 'narrator', 'options',
            'potion', 'recipe', 'record', 'resourcePack', 'screenshot', 'selectServer',
            'selectWorld', 'sign', 'soundCategory', 'spectatorMenu', 'splash_potion',
            'stat', 'stats', 'structure_block', 'subtitles', 'tile', 'tipped_arrow',
            'title', 'translation', 'tutorial']

successful_pack_counter = 0
warning_pack_counter = 0
pack_counter = 0

def main():
    parser = argparse.ArgumentParser(description="Automatic build resourcepacks")
    parser.add_argument('type', default='normal', help="Build type. Should be 'all', 'normal', 'leaveblank' or 'compatible'.")
    parser.add_argument('-l', '--legacy', action='store_true', help="(Not fully implemented) Use legacy format (.lang) when building resource packs. If build type is 'all', this argument will be ignored.")
    parser.add_argument('-b', '--leaveblank', action='store_true', help="Leave all the blanks when building resource packs. If build type is 'all', this argument will be ignored.")
    args = vars(parser.parse_args())
    if args['type'] == 'all':
        build_all()
    else:
        build(args)
    print("\n[INFO] Built %d pack(s), with %d pack(s) no warning" % (pack_counter, successful_pack_counter))

def build(args):
    global pack_counter
    global successful_pack_counter
    global warning_pack_counter
    with open("assets/minecraft/lang/lzh.json", 'r', encoding='utf8') as f:
        lang_data = json.load(f)
    pack_name = get_packname(args)
    print("[INFO] Building " + pack_name)
    warning_counter = 0
    # all builds have these files
    pack = zipfile.ZipFile(pack_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5)
    pack.write("LICENSE")
    # processing pack.mcmeta
    with open("pack.mcmeta", 'r', encoding='utf8') as meta:
        metadata = json.load(meta)
    # decide build type
    if args['type'] == 'normal':
        lang_name = "lzh"
    elif args['type'] == 'compatible':
        lang_name = "zh_tw"
        del metadata['language']
    if not args['leaveblank']:
        # delete untranslated strings, by chyx
        lang_data = {k:v for k,v in lang_data.items() if v}
    if not args['legacy']:
        lang_extension = ".json"
        # normal build
        pack.writestr("assets/minecraft/lang/" + lang_name + lang_extension, json.dumps(lang_data, indent=4, ensure_ascii=True))
    else:
        # legacy build
        lang_extension = ".lang"
        legacy_lang_data = {}
        for file in mappings:
            file_name = file + ".json"
            if file_name not in os.listdir("mappings"):
                print("\033[33m[WARN] Missing mapping: %s, Skipping\033[0m" % (file_name))
                warning_counter += 1
                pass
            else:
                location = "mappings/" + file_name
                with open(location, encoding='utf8') as f:
                    mapping = json.load(f)
                for k,v in mapping.items():
                    if (k not in mapping.keys()) or (v not in lang_data.keys()):
                        print("\033[33m[WARN] " + "Corrupted key-value pair in file %s: {\"%s\": \"%s\"}\033[0m" % (file_name, k, v))
                        warning_counter += 1
                        pass
                    else:
                        legacy_lang_data.update({k:lang_data.pop(v)})
        legacy_lang_file = ""
        for k, v in legacy_lang_data.items():
            legacy_lang_file += "%s=%s\n" %(k,v)
        pack.writestr("assets/minecraft/lang/" + lang_name + lang_extension, legacy_lang_file)
        # change pack format
        metadata['pack'].update({"pack_format": 3})
    pack.writestr("pack.mcmeta", json.dumps(metadata, indent=4, ensure_ascii=False))
    pack.close()
    print("[INFO] Built pack %s with %d warning(s)" % (pack_name, warning_counter))
    if warning_counter == 0:
        successful_pack_counter += 1
    else:
        warning_pack_counter += 1
    pack_counter += 1

def build_all():
    build({'type': 'normal', 'legacy': False, 'leaveblank': False})
    build({'type': 'normal', 'legacy': False, 'leaveblank': True})
    build({'type': 'compatible', 'legacy': False, 'leaveblank': False})
    build({'type': 'compatible', 'legacy': True, 'leaveblank': False})

def get_packname(args):
    base_name = "lzh"
    if args['type'] == 'normal':
        pass
    elif args['type'] == 'compatible':
        base_name = base_name + "_compatible"
    if args['legacy']:
        base_name = base_name + "_legacy"
    if args['leaveblank']:
        base_name = base_name + "_leaveblank"
    return base_name + ".zip"

if __name__ == "__main__":
    main()