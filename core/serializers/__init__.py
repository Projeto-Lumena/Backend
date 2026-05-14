from django.conf.locale import fr

from .user import UserRegistrationSerializer, UserSerializer
from .endereco import EnderecoSerializer
from .avaliacao import AvaliacaoSerializer
from .pedido import PedidoSerializer
from .pagamento import PagamentoSerializer
from .embalagem import EmbalagemSerializer
from .item_pedido import ItemPedidoSerializer
from .fita import FitaSerializer
from .produto import ProdutoListSerializer, ProdutoRetrieveSerializer, ProdutoSerializer
from .produto_variacao import ProdutoVariacaoSerializer  
from .tampa import TampaSerializer
from .tipo import TipoProdutoSerializer
from .recipiente import RecipienteSerializer
from .aroma import AromaSerializer 
from .adesivo import AdesivoSerializer
from .categoria import CategoriaSerializer
from .parafina import ParafinaSerializer
from .pavio import PavioSerializer