class Security:
    def authenticate(self, username, password):
        """Simple authentication system"""
        users = {
            'admin': 'admin123',
            'user': 'user123'
        }

        if username in users and users[username] == password:
            return {'username': username, 'role': 'manager' if username == 'admin' else 'worker'}
        return None