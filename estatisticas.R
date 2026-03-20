# ============================================================
# FarmTech Solutions - Analise Estatistica em R
# Calcula media e desvio padrao dos dados coletados em Python
# ============================================================

# Limpar ambiente
rm(list = ls())

# ------------------------------------------------------------
# 1. LEITURA DOS DADOS (CSV exportado pelo Python)
# ------------------------------------------------------------
arquivo_csv <- "dados_farmtech.csv"

if (!file.exists(arquivo_csv)) {
  cat("==============================================\n")
  cat("  ERRO: Arquivo '", arquivo_csv, "' nao encontrado!\n", sep = "")
  cat("  Execute primeiro o programa Python e exporte\n")
  cat("  os dados usando a opcao 5 do menu.\n")
  cat("==============================================\n")
  quit(status = 1)
}

dados <- read.csv(arquivo_csv, header = TRUE, stringsAsFactors = FALSE)

cat("\n")
cat("==================================================\n")
cat("  FARMTECH SOLUTIONS - Estatisticas em R\n")
cat("==================================================\n\n")

# Mostrar dados carregados
cat(">> Dados carregados:\n")
print(dados)
cat("\n")

# ------------------------------------------------------------
# 2. ESTATISTICAS GERAIS (todos os registros)
# ------------------------------------------------------------
cat("==================================================\n")
cat("  ESTATISTICAS GERAIS\n")
cat("==================================================\n\n")

# Vetor de areas
vetor_areas <- dados$area_m2
cat("  Vetor de areas (m2):", vetor_areas, "\n")
cat("  Media das areas:      ", round(mean(vetor_areas), 2), "m2\n")
cat("  Desvio padrao areas:  ", round(sd(vetor_areas), 2), "m2\n")
cat("  Minimo:               ", round(min(vetor_areas), 2), "m2\n")
cat("  Maximo:               ", round(max(vetor_areas), 2), "m2\n\n")

# Vetor de insumos
vetor_insumos <- dados$insumo_litros
cat("  Vetor de insumos (L):", vetor_insumos, "\n")
cat("  Media dos insumos:    ", round(mean(vetor_insumos), 4), "L\n")
cat("  Desvio padrao insumos:", round(sd(vetor_insumos), 4), "L\n")
cat("  Minimo:               ", round(min(vetor_insumos), 4), "L\n")
cat("  Maximo:               ", round(max(vetor_insumos), 4), "L\n\n")

# ------------------------------------------------------------
# 3. ESTATISTICAS POR CULTURA
# ------------------------------------------------------------
culturas_unicas <- unique(dados$cultura)

for (cultura in culturas_unicas) {
  cat("==================================================\n")
  cat("  ESTATISTICAS -", toupper(cultura), "\n")
  cat("==================================================\n\n")

  filtro <- dados[dados$cultura == cultura, ]

  # Area
  areas_cultura <- filtro$area_m2
  cat("  Registros:", nrow(filtro), "\n\n")
  cat("  Areas (m2):", areas_cultura, "\n")

  if (length(areas_cultura) > 1) {
    cat("  Media das areas:      ", round(mean(areas_cultura), 2), "m2\n")
    cat("  Desvio padrao areas:  ", round(sd(areas_cultura), 2), "m2\n")
  } else {
    cat("  Media das areas:      ", round(mean(areas_cultura), 2), "m2\n")
    cat("  Desvio padrao areas:   N/A (apenas 1 registro)\n")
  }

  # Insumos
  insumos_cultura <- filtro$insumo_litros
  nome_insumo <- unique(filtro$insumo)
  cat("\n  Insumo:", nome_insumo, "\n")
  cat("  Quantidades (L):", insumos_cultura, "\n")

  if (length(insumos_cultura) > 1) {
    cat("  Media dos insumos:    ", round(mean(insumos_cultura), 4), "L\n")
    cat("  Desvio padrao insumos:", round(sd(insumos_cultura), 4), "L\n")
  } else {
    cat("  Media dos insumos:    ", round(mean(insumos_cultura), 4), "L\n")
    cat("  Desvio padrao insumos: N/A (apenas 1 registro)\n")
  }

  cat("\n")
}

# ------------------------------------------------------------
# 4. RESUMO FINAL
# ------------------------------------------------------------
cat("==================================================\n")
cat("  RESUMO\n")
cat("==================================================\n")
cat("  Total de registros:   ", nrow(dados), "\n")
cat("  Culturas presentes:   ", paste(culturas_unicas, collapse = ", "), "\n")
cat("  Area total plantada:  ", round(sum(vetor_areas), 2), "m2\n")
cat("  Total de insumos:     ", round(sum(vetor_insumos), 4), "L\n")
cat("==================================================\n\n")

cat(">> Analise estatistica concluida com sucesso!\n\n")
