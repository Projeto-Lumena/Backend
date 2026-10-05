from .avaliacao import AvaliacaoSerializer
from .categoria import CategoriaSerializer
from .endereco import EnderecoSerializer
from .pagamento import PagamentoSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraSerializer,
)
from .produto_variacao import ProdutoVariacaoSerializer  
from .produto import ProdutoListSerializer, ProdutoRetrieveSerializer, ProdutoSerializer
from .tipo import TipoProdutoSerializer
from .user import UserRegistrationSerializer, UserSerializer