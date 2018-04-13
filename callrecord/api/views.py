from .validator import call_data_validator

def save_call_data(data):
    if call_data_validator(data):
        return {'success': 'POST method is working'}, 200

    return {'error': 'Data validation problem'}, 400
