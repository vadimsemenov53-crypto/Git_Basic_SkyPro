from src.main import save_file, clear_names, filter_russian_names, filter_english_names

cleared_names = clear_names("names.txt")

filtered_name_rus = filter_russian_names(cleared_names)
save_file(
    'russian_names.txt',
'\n'.join(filtered_name_rus))

filtered_name_eng = filter_english_names(cleared_names)
save_file(
    'english_names.txt',
    '\n'.join(filtered_name_eng)
)