"""
Orquestrador Principal do Projeto de Mestrado:
Avaliação da Fragilidade de RAG sob Variações Linguísticas em PT-BR
"""

import sys
import argparse
from pathlib import Path

# Suporte a UTF-8 no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="Orquestrador do Pipeline de Pesquisa para o Artigo de Mestrado"
    )
    parser.add_argument(
        "--modulo", "-m",
        choices=["1", "2", "3", "4", "todos"],
        default="1",
        help="Escolha qual módulo executar: 1 (Extração), 2 (QA Base), 3 (Estilos/Ruídos), 4 (Avaliação)"
    )
    parser.add_argument("--input", "-i", default=None, help="Caminho customizado de entrada")
    parser.add_argument("--output", "-o", default=None, help="Caminho customizado de saída")
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Força reprocessamento de documentos existentes (desativa modo incremental)"
    )

    args = parser.parse_args()

    print("=" * 65)
    print("🎓 PIPELINE DE PESQUISA - ARTIGO DE MESTRADO")
    print("=" * 65)

    if args.modulo in ["1", "todos"]:
        print("\n🔹 Executando Módulo 01: Extração com Docling...")
        from modulos.etapa1_extracao.extrator import extrair_documentos
        extrair_documentos(dir_entrada=args.input, dir_saida=args.output, force=args.force)

    if args.modulo in ["2", "todos"]:
        print("\n🔹 Módulo 02: Geração de QA Base (Em fase de definição de estratégia)")
        print("   Consulte a pasta 'modulos/etapa2_geracao_qa' para os prompts e diretrizes.")

    if args.modulo in ["3", "todos"]:
        print("\n🔹 Módulo 03: Estilos e Ruídos (Inspirado no paper 'Out of Style')")
        print("   Consulte a pasta 'modulos/etapa3_estilos_ruidos' para as 4 dimensões de perturbação.")

    if args.modulo in ["4", "todos"]:
        print("\n🔹 Módulo 04: Avaliação de Perguntas e Auditoria Semântica")
        print("   Consulte a pasta 'modulos/etapa4_avaliacao' para os critérios de similaridade e descarte.")

    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
