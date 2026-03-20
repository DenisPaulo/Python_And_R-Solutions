# FarmTech Solutions - Agricultura Digital

Projeto da startup **FarmTech Solutions** para gestao de culturas agricolas usando Python e R.

## Estrutura do Projeto

```
farmtech-solutions/
  farmtech.py          # Aplicacao principal em Python
  estatisticas.R       # Analise estatistica em R (media, desvio padrao)
  clima.R              # Consulta de API meteorologica em R (bonus)
  dados_farmtech.csv   # Dados exportados pelo Python (gerado automaticamente)
  dados_farmtech.json  # Dados persistidos pelo Python (gerado automaticamente)
  README.md            # Este arquivo
```

## Culturas Suportadas

| Cultura | Figura Geometrica | Insumo    | Unidade       |
|---------|-------------------|-----------|---------------|
| Cafe    | Retangulo         | Fosfato   | mL/metro      |
| Milho   | Circulo (pivo)    | Herbicida | L/hectare     |

## Como Executar

### 1. Python - Aplicacao Principal

```bash
python3 farmtech.py
```

O programa apresenta um menu interativo com as opcoes:
1. **Entrada de dados** - cadastrar nova area de plantio e calcular insumos
2. **Saida de dados** - exibir todos os registros cadastrados
3. **Atualizar dados** - modificar um registro existente
4. **Deletar dados** - remover um registro
5. **Exportar CSV para R** - gerar arquivo CSV para analise em R
6. **Sair do programa**

### 2. R - Analise Estatistica

Primeiro, execute o programa Python e cadastre alguns registros. Depois:

```bash
Rscript estatisticas.R
```

O script calcula:
- Media e desvio padrao das areas plantadas
- Media e desvio padrao das quantidades de insumo
- Estatisticas separadas por cultura (cafe e milho)

### 3. R - Dados Climaticos (Ir Alem)

```bash
Rscript clima.R
```

Conecta-se a API publica **Open-Meteo** (sem necessidade de chave) para:
- Exibir clima atual de cidades brasileiras
- Previsao de 7 dias (temperatura e chuva)
- Estatisticas da previsao (media e desvio padrao)

## Requisitos

- **Python 3.x** (sem bibliotecas externas)
- **R** com pacotes `httr` e `jsonlite` (instalados automaticamente pelo script clima.R)

## Equipe

Projeto desenvolvido como atividade academica - FarmTech Solutions.
