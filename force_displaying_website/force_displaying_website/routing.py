from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

import force_app.routing


application = ProtocolTypeRouter({
    # http->django views are added by default

    'websocket': AuthMiddlewareStack(
        URLRouter(
            force_app.routing.websocket_urlpatterns
        )
    ),
})
