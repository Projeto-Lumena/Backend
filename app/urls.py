from django.conf import settings
from django.conf.urls.static import static
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

from core.views import (
    AdesivoViewSet,
    AromaViewSet,
    AvaliacaoViewSet,
    CategoriaViewSet,
    EmbalagemViewSet,
    EnderecoViewSet,
    FitaViewSet,
    ItemPedidoViewSet,
    PagamentoViewSet,
    ParafinaViewSet,
    PavioViewSet,
    PedidoViewSet,
    ProdutoVariacaoViewSet,
    ProdutoViewSet,
    RecipienteViewSet,
    TampaViewSet,
    TipoProdutoViewSet,
    UserRegistrationView,
    UserViewSet,
)
from uploader.router import router as uploader_router

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
router.register(r'produto-variacao', ProdutoVariacaoViewSet, basename='produto-variacao')
router.register(r'tampa', TampaViewSet, basename='tampa')
router.register(r'tipo', TipoProdutoViewSet, basename='tipo')
router.register(r'recipiente', RecipienteViewSet, basename='recipiente')
router.register(r'aroma', AromaViewSet, basename='aroma')
router.register(r'adesivo', AdesivoViewSet, basename='adesivo')
router.register(r'categoria', CategoriaViewSet, basename='categoria')
router.register(r'parafina', ParafinaViewSet, basename='parafina')
router.register(r'pavio', PavioViewSet, basename='pavio')


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
    # Uploader de mídia
    path('api/media/', include(uploader_router.urls)),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de usuários
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),
    # API
    path('api/', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
