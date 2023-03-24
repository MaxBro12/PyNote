
# ! Основное
fold_data = 'server_data'

file_conf = f'{fold_data}/settings.toml'

file_conf_inner = {
    'app': {
        'width': 500,
        'height': 500,
    },
    'user': {
        'id': 0,
        'token': 0,
    }
}

file_log = f'{fold_data}/logger.log'
file_error = f'{fold_data}/error.log'

file_db = f'{fold_data}/base.db'

fold_notes = f'{fold_data}/notes'
