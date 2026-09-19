"""
Configurações do Módulo 01: Extração e Estruturação de Documentos (Docling).
"""

from pathlib import Path
import torch

# Raiz do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Diretórios padrão de dados
DIR_ENTRADA_PADRAO = ROOT_DIR / "dados" / "01_brutos"
DIR_SAIDA_PADRAO = ROOT_DIR / "dados" / "02_chunks"

# Configuração de Hardware / Aceleração
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
NUM_THREADS = 4

# Parâmetros de Processamento do Docling
# Desativado por padrão para PDFs digitais (economiza VRAM na RTX 2050 e acelera muito)
DO_OCR = False

# Reconstrói e preserva células, linhas e colunas de tabelas complexas
DO_TABLE_STRUCTURE = True

# Desativado para economizar I/O e evitar imagens repetidas/decorativas (foco textual/tabelas)
GENERATE_PICTURE_IMAGES = False

# Codificação padrão para arquivos de texto e Markdown
MARKDOWN_ENCODING = "utf-8"
JSON_ENCODING = "utf-8"
