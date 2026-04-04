from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import UserRegistrationView, UserViewSet, EnderecoViewSet, AvaliacaoViewSet, PedidoViewSet, PagamentoViewSet, EmbalagemViewSet, ItemPedidoViewSet, FitaViewSet, ProdutoViewSet, TampaViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'endereco', EnderecoViewSet, basename='endereco')
router.register(r'avaliacao', AvaliacaoViewSet, basename='avaliacao')
router.register(r'pedido', PedidoViewSet, basename='pedido')
router.register(r'pagamento', PagamentoViewSet, basename='pagamento')
router.register(r'embalagem', EmbalagemViewSet, basename='embalagem')
router.register(r'item-pedido', ItemPedidoViewSet, basename='item-pedido')
router.register(r'fita', FitaViewSet, basename='fita')
router.register(r'produto', ProdutoViewSet, basename='produto')
router.register(r'tampa', TampaViewSet, basename='tampa')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de usuários
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),
    # API
    path('api/', include(router.urls)),
]
