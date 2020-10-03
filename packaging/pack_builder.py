import os
from json import load, dumps
from sys import stderr
from zipfile import ZipFile, ZIP_DEFLATED

# Due to unfinished end.txt and splashes.txt, they are not added to the pack.
# Due to missing realms strings, they are not added to the pack.


class pack_builder(object):
    '''Build packs.'''

    def __init__(self, main_res_path: str):
        self.__args = {}
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""
        self.__main_res_path = main_res_path

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, value: dict):
        self.__args = value

    @property
    def warning_count(self):
        return self.__warning

    @property
    def error_count(self):
        return self.__error

    @property
    def filename(self):
        return self.__filename != "" and self.__filename or "Did not build any pack."

    @property
    def main_resource_path(self):
        return self.__main_res_path

    @property
    def logs(self):
        return self.__log_list and '\n'.join(self.__log_list) or "Did not build any pack."

    def clean_status(self):
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""

    def build(self):
        self.clean_status()
        args = self.args
        # args validation
        status, info = self.__check_args()
        if status:
            # process args
            # get language strings
            main_lang_data = self.__get_language_content()
            # get realms strings
            # no realms strings yet
            # realms_lang_data = load(open(os.path.join(
            #    self.main_resource_path, "assets/realms/lang/lzh.json"), 'r', encoding='utf8'))
            # process pack name
            pack_name = "lzh.zip"
            self.__filename = pack_name
            # process mcmeta
            mcmeta = self.__process_meta(args)
            # decide language file name & ext
            lang_file_name = self.__get_lang_filename(args['type'])
            # set output dir
            pack_name = os.path.join(args['output'], pack_name)
            # mkdir
            if os.path.exists(args['output']) and not os.path.isdir(args['output']):
                os.remove(args['output'])
            if not os.path.exists(args['output']):
                os.mkdir(args['output'])
            # create pack
            info = f"Building pack {pack_name}"
            print(info)
            self.__log_list.append(info)
            pack = ZipFile(
                pack_name, 'w', compression=ZIP_DEFLATED, compresslevel=5)
            # no pack.png yet
            # pack.write(os.path.join(self.main_resource_path,
            #                        "pack.png"), arcname="pack.png")
            pack.writestr("LICENSE", self.__handle_license())
            pack.writestr("pack.mcmeta", dumps(
                mcmeta, indent=4, ensure_ascii=False))
            # dump lang file into pack
            if args['type'] != 'legacy':
                # normal/compat
                pack.writestr(f"assets/minecraft/lang/{lang_file_name}",
                              dumps(main_lang_data, indent=4, ensure_ascii=True, sort_keys=True))
                # no realms strings yet
                # pack.writestr(f"assets/realms/lang/{lang_file_name}",
                #              dumps(realms_lang_data, indent=4, ensure_ascii=True, sort_keys=True))
            else:
                # legacy
                pack.writestr(
                    f"assets/minecraft/lang/{lang_file_name}", self.__generate_legacy_content(main_lang_data))
            pack.close()
            print("Build successful.")
        else:
            self.__raise_error(info)

    def __raise_warning(self, warning: str):
        print(f'\033[33mWarning: {warning}\033[0m', file=stderr)
        self.__log_list.append(f'Warning: {warning}')
        self.__warning += 1

    def __raise_error(self, error: str):
        print(f'\033[1;31mError: {error}\033[0m', file=stderr)
        print("\033[1;31mTerminate building because an error occurred.\033[0m")
        self.__log_list.append(f'Error: {error}')
        self.__log_list.append("Terminate building because an error occurred.")
        self.__error += 1

    def __check_args(self):
        args = self.args
        # check "format"
        if 'format' not in args or args['format'] is None:
            # did not specify "format", assume a value
            format = args['type'] == 'legacy' and 3 or 6
            self.__raise_warning(
                f'Did not specify "pack_format". Assuming value is "{format}".')
            args['format'] = format
        else:
            if (args['type'] == 'legacy' and args['format'] > 3) or (args['type'] in ('normal', 'compat') and args['format'] <= 3):
                return False, f'Type "{args["type"]}" does not match pack_format {args["format"]}'
        # check essential arguments
        for key in ('type', 'leaveblank', 'output'):
            if key not in args:
                return False, f'Missing required argument "{key}"'
        return True, None

    def __process_meta(self, args: dict) -> dict:
        data = load(open(os.path.join(self.main_resource_path,
                                      'pack.mcmeta'), 'r', encoding='utf8'))
        pack_format = args['type'] == 'legacy' and 3 or (
            'format' in args and args['format'] or None)
        data['pack']['pack_format'] = pack_format or data['pack']['pack_format']
        if args['type'] == 'compat':
            data.pop('language')
        return data

    def __get_lang_filename(self, type: str) -> str:
        return type == 'normal' and 'lzh.json' or (
            type == 'compat' and 'zh_tw.json' or 'zh_tw.lang')

    def __get_language_content(self):
        content = load(open(os.path.join(self.main_resource_path,
                                         "assets/minecraft/lang/lzh.json"), 'r', encoding='utf8'))
        # doubt whether this is really used
        if not self.args['leaveblank']:
            content = {k: v for k, v in content.items() if v}
        return content

    def __generate_legacy_content(self, content: dict) -> str:
        # get mappings list
        mappings = load(open(os.path.join(self.main_resource_path,
                                          "mappings", "all_mappings"), 'r', encoding='utf8'))
        legacy_lang_data = {}
        for item in mappings:
            mapping_file = f"{item}.json"
            if mapping_file not in os.listdir("mappings"):
                self.__raise_warning(
                    f"Missing mapping '{mapping_file}', skipping.")
            else:
                mapping = load(
                    open(os.path.join("mappings", mapping_file), 'r', encoding='utf8'))
                for k, v in mapping.items():
                    if v not in content:
                        self.__raise_warning(
                            f"Corrupted key-value pair in file {mapping_file}: {{'{k}': '{v}'}}, skipping.")
                    else:
                        legacy_lang_data[k] = content[v]
        return ''.join(f'{k}={v}\n' for k, v in legacy_lang_data.items())

    def __handle_license(self):
        return ''.join(item[1] for item in enumerate(
            open(os.path.join(self.main_resource_path, "LICENSE"), 'r', encoding='utf8')))
