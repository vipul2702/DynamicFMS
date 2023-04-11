from django.contrib.auth.tokens import PasswordResetTokenGenerator
 
from six import text_type
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(int(user.pk)) 
        )
    
generate_token = TokenGenerator()