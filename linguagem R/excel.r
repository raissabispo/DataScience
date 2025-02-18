
install.packages(c("writexl", "readxl"))

library(writexl)
library(readxl)

produtos <- data.frame(
  Produto = c("A","B","C", "D"),
  Preço = sample(10:50, 4),
  Estoque = sample(0:100, 4)
)

write_xlsx(produtos, "produtos.xlsx")
produtos_carregado <- read_excel("Produtos.xlsx")

print(paste("Preço médio: ", mean(produtos_carregado$Preço)))