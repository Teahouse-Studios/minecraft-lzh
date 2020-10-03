import build
import os

if __name__ == '__main__':
    preset_args = [
        {'type': 'compat', 'leaveblank': False, 'output': 'builds', 'format': 6},
        {'type': 'legacy', 'leaveblank': False, 'output': 'builds', 'format': 3},
        {'type': 'normal', 'leaveblank': True, 'output': 'builds', 'format': 6},
        {'type': 'normal', 'leaveblank': False, 'output': 'builds', 'format': 6}
    ]
    preset_name = [
        "lzh_compatible.zip",
        "lzh_legacy.zip",
        "lzh_leaveblank.zip",
        "lzh.zip"
    ]
    pack_counter = 0
    perfect_pack_counter = 0
    base_folder = "builds"
    for file in os.listdir(base_folder):
        os.remove(os.path.join(base_folder, file))
    for args, name in zip(preset_args, preset_name):
        info, warning_count, error_count = build.build(args)
        if error_count == 0:
            pack_counter += 1
            if warning_count == 0:
                perfect_pack_counter += 1
            if name != "lzh.zip":
                os.rename("builds/lzh.zip",
                          os.path.join(base_folder, name))
                print(f"Renamed pack to {name}.")
        else:
            print(f"Failed to build pack {name}.")
    print(
        f"Built {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")
