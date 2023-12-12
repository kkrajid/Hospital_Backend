
# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management_.settings')

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter , URLRouter
# from chat.routing import websocket_urlpatterns



# application = ProtocolTypeRouter(
#     {
#         "http" : get_asgi_application() ,
#         "websocket" : AuthMiddlewareStack(
#             URLRouter(
#                 websocket_urlpatterns
#             )   
#         )
#     }
# )

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management_.settings')

# Ensure that Django is properly set up before importing the routing module
django.setup()

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    }
)
