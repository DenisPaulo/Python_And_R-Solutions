"""
FarmTech Solutions - Aplicacao em Python
Agricultura Digital - Gestao de Culturas

Culturas suportadas:
  1. Cafe (area retangular: comprimento x largura)
  2. Milho (area circular: pivo central de irrigacao)

Insumos:
  - Cafe: Fosfato (mL por metro linear de rua)
  - Milho: Herbicida (L por hectare)
"""

import math
import json
import os

# ============================================================
# VETORES (listas) para armazenar os dados
# ============================================================
culturas = []         # nome da cultura ("cafe" ou "milho")
areas = []            # area plantada (m2)
insumos_nome = []     # nome do insumo
insumos_qtd = []      # quantidade total de insumo (litros)

ARQUIVO_DADOS = "dados_farmtech.json"


# ============================================================
# FUNCOES DE CALCULO DE AREA
# ============================================================
def calcular_area_retangulo(comprimento, largura):
    """Calcula a area de um retangulo (cafe)."""
    return comprimento * largura


def calcular_area_circulo(raio):
    """Calcula a area de um circulo (milho - pivo central)."""
    return math.pi * raio ** 2


# ============================================================
# FUNCOES DE CALCULO DE INSUMOS
# ============================================================
def calcular_insumo_cafe(ml_por_metro, comprimento_rua, num_ruas):
    """
    Cafe: fosfato aplicado por metro linear em cada rua.
    Retorna a quantidade total em litros.
    """
    total_ml = ml_por_metro * comprimento_rua * num_ruas
    total_litros = total_ml / 1000.0
    return total_litros


def calcular_insumo_milho(litros_por_hectare, area_m2):
    """
    Milho: herbicida aplicado por hectare.
    Retorna a quantidade total em litros.
    """
    area_hectares = area_m2 / 10000.0
    total_litros = litros_por_hectare * area_hectares
    return total_litros


# ============================================================
# FUNCOES DE PERSISTENCIA (salvar / carregar JSON)
# ============================================================
def salvar_dados():
    """Salva os vetores em arquivo JSON."""
    dados = {
        "culturas": culturas,
        "areas": areas,
        "insumos_nome": insumos_nome,
        "insumos_qtd": insumos_qtd,
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"\n>> Dados salvos em '{ARQUIVO_DADOS}'.")


def carregar_dados():
    """Carrega dados do arquivo JSON, se existir."""
    global culturas, areas, insumos_nome, insumos_qtd
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
        culturas = dados.get("culturas", [])
        areas = dados.get("areas", [])
        insumos_nome = dados.get("insumos_nome", [])
        insumos_qtd = dados.get("insumos_qtd", [])
        print(f">> Dados carregados de '{ARQUIVO_DADOS}'.")


# ============================================================
# EXPORTAR DADOS PARA CSV (para uso no R)
# ============================================================
def exportar_csv():
    """Exporta os vetores para um arquivo CSV para uso em R."""
    nome_csv = "dados_farmtech.csv"
    with open(nome_csv, "w", encoding="utf-8") as f:
        f.write("cultura,area_m2,insumo,insumo_litros\n")
        for i in range(len(culturas)):
            f.write(f"{culturas[i]},{areas[i]:.2f},{insumos_nome[i]},{insumos_qtd[i]:.4f}\n")
    print(f"\n>> Dados exportados para '{nome_csv}' (pronto para uso em R).")


# ============================================================
# FUNCAO: ENTRADA DE DADOS
# ============================================================
def entrada_dados():
    """Menu de entrada de dados para cafe ou milho."""
    print("\n" + "=" * 50)
    print("  ENTRADA DE DADOS")
    print("=" * 50)
    print("  Escolha a cultura:")
    print("  1 - Cafe")
    print("  2 - Milho")
    opcao = input("  Opcao: ").strip()

    if opcao == "1":
        # ---- CAFE (retangulo) ----
        print("\n  >> CAFE - Area retangular")
        while True:
            try:
                comprimento = float(input("  Comprimento do terreno (m): "))
                largura = float(input("  Largura do terreno (m): "))
                if comprimento <= 0 or largura <= 0:
                    print("  [!] Valores devem ser positivos. Tente novamente.")
                    continue
                break
            except ValueError:
                print("  [!] Valor invalido. Digite um numero.")

        area = calcular_area_retangulo(comprimento, largura)
        print(f"\n  Area plantada (cafe): {area:.2f} m2")

        # Insumo: fosfato
        print("\n  >> Manejo de insumo: FOSFATO")
        while True:
            try:
                ml_metro = float(input("  Quantidade de fosfato (mL/metro): "))
                comp_rua = float(input("  Comprimento de cada rua (m): "))
                num_ruas = int(input("  Numero de ruas na lavoura: "))
                if ml_metro <= 0 or comp_rua <= 0 or num_ruas <= 0:
                    print("  [!] Valores devem ser positivos. Tente novamente.")
                    continue
                break
            except ValueError:
                print("  [!] Valor invalido. Tente novamente.")

        total_litros = calcular_insumo_cafe(ml_metro, comp_rua, num_ruas)
        print(f"\n  Total de fosfato necessario: {total_litros:.2f} litros")

        # Armazena nos vetores
        culturas.append("cafe")
        areas.append(area)
        insumos_nome.append("fosfato")
        insumos_qtd.append(total_litros)

    elif opcao == "2":
        # ---- MILHO (circulo - pivo) ----
        print("\n  >> MILHO - Area circular (pivo central)")
        while True:
            try:
                raio = float(input("  Raio do pivo central (m): "))
                if raio <= 0:
                    print("  [!] Valor deve ser positivo. Tente novamente.")
                    continue
                break
            except ValueError:
                print("  [!] Valor invalido. Digite um numero.")

        area = calcular_area_circulo(raio)
        print(f"\n  Area plantada (milho): {area:.2f} m2")

        # Insumo: herbicida
        print("\n  >> Manejo de insumo: HERBICIDA")
        while True:
            try:
                litros_ha = float(input("  Quantidade de herbicida (L/hectare): "))
                if litros_ha <= 0:
                    print("  [!] Valor deve ser positivo. Tente novamente.")
                    continue
                break
            except ValueError:
                print("  [!] Valor invalido. Tente novamente.")

        total_litros = calcular_insumo_milho(litros_ha, area)
        print(f"\n  Total de herbicida necessario: {total_litros:.2f} litros")

        # Armazena nos vetores
        culturas.append("milho")
        areas.append(area)
        insumos_nome.append("herbicida")
        insumos_qtd.append(total_litros)

    else:
        print("  [!] Opcao invalida.")
        return

    salvar_dados()
    exportar_csv()
    print("  >> Registro adicionado com sucesso!")


# ============================================================
# FUNCAO: SAIDA DE DADOS
# ============================================================
def saida_dados():
    """Exibe todos os dados armazenados nos vetores."""
    print("\n" + "=" * 50)
    print("  SAIDA DE DADOS")
    print("=" * 50)

    if len(culturas) == 0:
        print("  Nenhum registro encontrado.")
        return

    print(f"  {'Idx':<5}{'Cultura':<10}{'Area (m2)':<15}{'Insumo':<12}{'Qtd (L)':<10}")
    print("  " + "-" * 52)
    for i in range(len(culturas)):
        print(f"  {i:<5}{culturas[i]:<10}{areas[i]:<15.2f}{insumos_nome[i]:<12}{insumos_qtd[i]:<10.4f}")

    print(f"\n  Total de registros: {len(culturas)}")


# ============================================================
# FUNCAO: ATUALIZAR DADOS
# ============================================================
def atualizar_dados():
    """Atualiza um registro em uma posicao do vetor."""
    print("\n" + "=" * 50)
    print("  ATUALIZACAO DE DADOS")
    print("=" * 50)

    if len(culturas) == 0:
        print("  Nenhum registro para atualizar.")
        return

    saida_dados()

    while True:
        try:
            idx = int(input("\n  Indice do registro a atualizar: "))
            if 0 <= idx < len(culturas):
                break
            else:
                print(f"  [!] Indice deve estar entre 0 e {len(culturas) - 1}.")
        except ValueError:
            print("  [!] Digite um numero inteiro valido.")

    print(f"\n  Registro atual: {culturas[idx]} | {areas[idx]:.2f} m2 | "
          f"{insumos_nome[idx]} | {insumos_qtd[idx]:.4f} L")

    print("\n  O que deseja atualizar?")
    print("  1 - Area plantada (m2)")
    print("  2 - Quantidade de insumo (litros)")
    print("  3 - Ambos")
    opcao = input("  Opcao: ").strip()

    if opcao in ("1", "3"):
        while True:
            try:
                nova_area = float(input("  Nova area plantada (m2): "))
                if nova_area > 0:
                    areas[idx] = nova_area
                    break
                else:
                    print("  [!] Valor deve ser positivo.")
            except ValueError:
                print("  [!] Valor invalido.")

    if opcao in ("2", "3"):
        while True:
            try:
                nova_qtd = float(input("  Nova quantidade de insumo (litros): "))
                if nova_qtd > 0:
                    insumos_qtd[idx] = nova_qtd
                    break
                else:
                    print("  [!] Valor deve ser positivo.")
            except ValueError:
                print("  [!] Valor invalido.")

    if opcao not in ("1", "2", "3"):
        print("  [!] Opcao invalida.")
        return

    salvar_dados()
    exportar_csv()
    print("  >> Registro atualizado com sucesso!")


# ============================================================
# FUNCAO: DELETAR DADOS
# ============================================================
def deletar_dados():
    """Remove um registro dos vetores."""
    print("\n" + "=" * 50)
    print("  DELECAO DE DADOS")
    print("=" * 50)

    if len(culturas) == 0:
        print("  Nenhum registro para deletar.")
        return

    saida_dados()

    while True:
        try:
            idx = int(input("\n  Indice do registro a deletar: "))
            if 0 <= idx < len(culturas):
                break
            else:
                print(f"  [!] Indice deve estar entre 0 e {len(culturas) - 1}.")
        except ValueError:
            print("  [!] Digite um numero inteiro valido.")

    registro = (f"{culturas[idx]} | {areas[idx]:.2f} m2 | "
                f"{insumos_nome[idx]} | {insumos_qtd[idx]:.4f} L")
    confirmacao = input(f"  Confirma exclusao de [{registro}]? (s/n): ").strip().lower()

    if confirmacao == "s":
        culturas.pop(idx)
        areas.pop(idx)
        insumos_nome.pop(idx)
        insumos_qtd.pop(idx)
        salvar_dados()
        exportar_csv()
        print("  >> Registro deletado com sucesso!")
    else:
        print("  >> Exclusao cancelada.")


# ============================================================
# MENU PRINCIPAL
# ============================================================
def menu():
    """Menu principal da aplicacao."""
    carregar_dados()

    while True:
        print("\n" + "=" * 50)
        print("  FARMTECH SOLUTIONS - Agricultura Digital")
        print("=" * 50)
        print("  1 - Entrada de dados")
        print("  2 - Saida de dados (exibir)")
        print("  3 - Atualizar dados")
        print("  4 - Deletar dados")
        print("  5 - Exportar CSV para R")
        print("  6 - Sair do programa")
        print("=" * 50)

        opcao = input("  Escolha uma opcao: ").strip()

        if opcao == "1":
            entrada_dados()
        elif opcao == "2":
            saida_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            if len(culturas) > 0:
                exportar_csv()
            else:
                print("  [!] Nenhum dado para exportar.")
        elif opcao == "6":
            print("\n  Obrigado por usar o FarmTech Solutions!")
            print("  Ate logo!\n")
            break
        else:
            print("  [!] Opcao invalida. Tente novamente.")


# ============================================================
# PONTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    menu()
