peso <- as.numeric(readline("Digite seu peso(kg): "))
altura <- as.numeric(readline("Digite sua atura(m): "))
imc <- peso/ (altura ^ 2)
print(paste("Seu IMC é: ", imc ))


