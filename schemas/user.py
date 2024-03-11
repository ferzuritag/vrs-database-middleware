def user_schema(user) -> dict:
    return {
        'id': str(user['_id']),
        'email': user['email'],
        'verified': user['verified'],
        'active': user['active']
    }