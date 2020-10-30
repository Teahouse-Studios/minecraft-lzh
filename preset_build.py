if __name__ == '__main__':
    import build
    from json import load
    import os
    from sys import exit

    pack_version = '0.2.1'
    build_unsuccessful = 0

    def check_version_consistency():
        mcmeta_desc = (load(open("minecraft-lzh/pack.mcmeta",
                                 'r', encoding='utf8')))['pack']['description']
        return pack_version in mcmeta_desc
    if check_version_consistency():
        preset_args = [
            {'type': 'normal', 'leaveblank': False,
             'output': 'builds', 'format': 6},
            {'type': 'compat', 'leaveblank': False,
                'output': 'builds', 'format': 6},
            {'type': 'normal', 'leaveblank': True,
                'output': 'builds', 'format': 6},
            {'type': 'legacy', 'leaveblank': False,
             'output': 'builds', 'format': 3}
        ]
        preset_name = [
            f"minecraft-lzh_v{pack_version}.zip",
            f"minecraft-lzh_compatible_v{pack_version}.zip",
            f"minecraft-lzh_leaveblank_v{pack_version}.zip",
            f"minecraft-lzh_legacy_v{pack_version}.zip"
        ]
        pack_counter = 0
        perfect_pack_counter = 0
        base_folder = "builds"
        if os.path.exists(base_folder) and not os.path.isdir(base_folder):
            os.remove(base_folder)
        if not os.path.exists(base_folder):
            os.mkdir(base_folder)
        for file in os.listdir(base_folder):
            os.remove(os.path.join(base_folder, file))
        for args, name in zip(preset_args, preset_name):
            pack_name, warning_count, error, _ = build.build(args)
            if not error:
                pack_counter += 1
                if warning_count == 0:
                    perfect_pack_counter += 1
                if name != pack_name:
                    os.rename(os.path.join(base_folder, pack_name),
                              os.path.join(base_folder, name))
                    print(f"Renamed pack to {name}.")
            else:
                print(f"Failed to build pack {name}.")
                build_unsuccessful = 1
        print(
            f"Built {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")
        exit(build_unsuccessful)
    else:
        exit(
            f'\033[1;31mError: Pack version "{pack_version}" does not match the number in pack.mcmeta.\033[0m')
