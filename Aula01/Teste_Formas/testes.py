from Aula01.Teste_Formas.circulo import Circulo
from Aula01.Teste_Formas.quadrado import Quadrado
from Aula01.Teste_Formas.retangulo import Retangulo

circulo = Circulo('Vermelho', 3, 'chumbo')

print('Iniciando testes\n\n')

print('Começando teste get\n>>>Circulo')
assert circulo.cor == circulo.get_mostraCor(), f'Num vai dá!!! A cor {cor} não está sendo passado para o objeto!'
assert cor == circulo.get_mostraCor(), f'Num vai dá!!! A cor {cor} não está sendo passado para o objeto!'
print('O miserável é um gênio\n\t\tTeste do get_mostrarCor(): ok\n\n')








quadrado = Quadrado(3)

print('Começando teste get\n>>>Quadrado')
assert quadrado.Tamanho_do_lado == quadrado.get_Retornar_valor_do_Lado(), f'Num vai dá!!! O tamanho do lado {Tamanho_do_lado} não está sendo passado para o objeto!'
assert tamanho_do_lado == quadrado.get_Retornar_valor_do_Lado(), f'Num vai dá!!! O Tamanho do lado {Tamanho_do_lado} não está sendo passado para o objeto!'
print('O miserável é um gênio\n\t\tTeste do get_Retornar_valor_do_lado(): ok\n\n')




retangulo = Retangulo(5, 3)

print('Começando teste get\n>>>Retângulo')
assert retangulo.ladoAcomprimento == retangulo.get_Retornar_valor_dos_lados(), f'Num vai dá!!! O valor do lado {ladoAcomprimento} não está sendo passado para o objeto!'
assert ladoAcomprimento == retangulo.get_Retornar_valor_dos_lados(), f'Num vai dá!!! O valor do lado {ladoAcomprimento} não está sendo passado para o objeto!'
print('O miserável é um gênio\n\t\tTeste do get_Retornar_valore_dos_lados(): ok\n\n')








assert circulo == True
assert circulo == None
assert circulo == False