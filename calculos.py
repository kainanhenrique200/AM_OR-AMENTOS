"""
calculos.py — Funções utilitárias de cálculo para o sistema de orçamentos e metragens.
Pode ser importado por qualquer outro módulo do projeto.
"""


def calcular_area(largura: float, comprimento: float) -> float:
    """Retorna a área em m² a partir de largura e comprimento."""
    return largura * comprimento


def arredondar_area(area: float, casas: int = 2) -> float:
    """Arredonda a área para o número de casas decimais indicado."""
    return round(area, casas)


def converter_para_decimal(area: float, divisor: float = 100) -> float:
    """Converte a área dividindo pelo divisor (padrão 100)."""
    return area / divisor


def calcular_valor_material(area: float, preco_m2: float) -> float:
    """Calcula o custo do material: área × preço por m²."""
    return area * preco_m2


def calcular_total_orcamento(
    valor_material: float,
    quantidade: int,
    montagem: float,
    taxa_cartao_pct: float
) -> float:
    """
    Calcula o valor final de um orçamento.

    subtotal = (valor_material × quantidade) + montagem
    taxa     = subtotal × (taxa_cartao_pct / 100)
    total    = subtotal + taxa
    """
    subtotal = (valor_material * quantidade) + montagem
    taxa = subtotal * (taxa_cartao_pct / 100)
    return subtotal + taxa


# ── Teste isolado ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\nSISTEMA DE METRAGEM — teste de cálculos\n")

    largura = float(input("Digite a largura (m): "))
    comprimento = float(input("Digite o comprimento (m): "))

    area = calcular_area(largura, comprimento)
    area_arredondada = arredondar_area(area)
    decimal = converter_para_decimal(area)

    print(f"\nÁrea total:       {area:.2f} m²")
    print(f"Área arredondada: {area_arredondada} m²")
    print(f"Conversão decimal: {decimal:.4f}")