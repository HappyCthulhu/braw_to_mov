import os
from pathlib import Path

from logger_settings import logger


# TODO: создать функцию для кроссплатформенных путей
def get_dir_files(fp):
    return os.listdir(fp)


def get_f_name_without_format(f_name):
    return f_name.split('.')[0]


def get_braw_file(f_names):
    braw_files = []

    for f_name in f_names:
        f_format = f_name.split('.')[-1]
        if 'braw' == f_format:
            braw_files.append(f_name)

    return braw_files


def check_if_f_names_is_correct(files):
    logger.info('Следующие файлы будут переименованы:\n')
    [print(file) for file in files]
    print('')
    logger.info(
        'Если все файлы найдены правильно, нажмите Enter. Если нет - закройте программу и напишите Валерочке!!!')

    input()


def rename_files(files, dp):
    for old_name in files:
        old_fp = Path(dp).joinpath(old_name)
        new_fp = f'{Path(dp).joinpath(get_f_name_without_format(old_name))}.mov'

        os.rename(old_fp, new_fp)

# logger.info('Пожалуйста, ниже введите путь до директории:')
# TODO: сделать кроссплатформенные пути сделать
# fps = '/home/valera/PycharmProjects/braw_to_mov/files'

# all_files = get_dir_files(fps)
# braw_files = get_braw_file(all_files)  # file names without format (without .braw)
# check_if_f_names_is_correct(braw_files)
# rename_files(braw_files)
# fps = input()
