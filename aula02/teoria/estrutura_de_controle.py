#se está chovendo --> levo guarda-chuva
#Senão, se está ensolarado --> passo o protetor solar
#senão --> Ando de boa na lagoa

#em python
esta_chovendo = False
esta_ensolarado = True
cor_do_guarda_chuva = "Preto"

def levar_guarda_chuva(cor):
    #return
 print(f"Está chovendo. Levando guarda-chuva {cor}.")

def passo_protetor_solar():
    # return
 print("Está ensolarado. Passando protetor solar.")

def ando_de_boa_na_lagoa():
    #return
 print("O tempo está de boa. Andando de boa na lagoa.")


if esta_chovendo:
    levar_guarda_chuva(cor_do_guarda_chuva)
elif esta_ensolarado:
    passo_protetor_solar()
else:
    ando_de_boa_na_lagoa()