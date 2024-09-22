class Security:
    def authenticate(self, username, password):
        """Simple authentication system"""
        users = {
            '1': '1',
            'user': 'user123',
            'admin':'admin143'
        }

        if username in users and users[username] == password:
            return {'username': username, 'role': 'manager' if username == 'admin' else 'worker'}
        return None