# FarmTech Solutions — Agricultura Digital

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)](https://www.r-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

Aplicação da startup **FarmTech Solutions** para gestão de culturas agrícolas com **Python** (CRUD + insumos) e **R** (estatística + clima).

## Resultado

Gestão de culturas em terminal: Python faz CRUD e cálculo de insumos (café/milho); R calcula estatísticas e consulta clima via Open-Meteo.

## Estrutura do Projeto

```
Python_And_R-Solutions/
├── farmtech.py        # Aplicação principal em Python
├── estatisticas.R     # Análise estatística em R (média, desvio padrão)
├── clima.R            # Consulta de API meteorológica em R (bônus)
├── .gitignore
├── README.md
└── LICENSE
```

> Os arquivos `dados_farmtech.csv` e `dados_farmtech.json` **não são versionados** (estão no `.gitignore`): são gerados automaticamente ao rodar `farmtech.py` (o CSV pela opção 5 do menu, para uso no R).

## Culturas Suportadas

| Cultura | Figura geométrica | Insumo    | Unidade   |
|---------|-------------------|-----------|-----------|
| Café    | Retângulo         | Fosfato   | mL/metro  |
| Milho   | Círculo (pivô)    | Herbicida | L/hectare |

## Como executar

### 1. Python — aplicação principal

```bash
python3 farmtech.py
```

Menu interativo:
1. **Entrada de dados** — cadastrar área de plantio e calcular insumos
2. **Saída de dados** — listar registros
3. **Atualizar dados** — modificar um registro
4. **Deletar dados** — remover um registro
5. **Exportar CSV para R** — gerar arquivo para análise
6. **Sair**

### 2. R — análise estatística

Cadastre alguns registros no Python e depois:

```bash
Rscript estatisticas.R
```

Calcula média e desvio padrão de áreas e insumos, separados por cultura.

### 3. R — dados climáticos (Ir Além)

```bash
Rscript clima.R
```

Usa a API pública **Open-Meteo** (sem chave) para clima atual, previsão de 7 dias e estatísticas.

## Requisitos

- **Python 3.x** (sem bibliotecas externas)
- **R** com pacotes `httr` e `jsonlite` (o script `clima.R` instala se necessário)

## Licença

Distribuído sob a licença [MIT](LICENSE).

---

Projeto acadêmico — FarmTech Solutions · [Denis Paulo](https://github.com/DenisPaulo)
