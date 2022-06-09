from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    user = None

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None

            # REFRESCAR TOKEN SI ES NECESARIO Y OBTENER EL USUARIO
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            
            if user != None:
                self.user = user
                return user

        return None

        # MANERA MAS RAPIDA DE HACER LA AUTENTICACION -- metodo authentication, exceptions

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales')

        return (self.user, None)