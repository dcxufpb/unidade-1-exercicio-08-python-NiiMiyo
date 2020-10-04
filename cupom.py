# coding: utf-8


def is_empty(value: str) -> bool:
    return (value == None) or (len(value) == value.count(" "))


class Loja:
    def __init__(self, nome_loja, logradouro, numero, complemento, bairro,
                 municipio, estado, cep, telefone, observacao, cnpj,
                 inscricao_estadual):
        self.nome_loja = nome_loja
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.observacao = observacao
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual


def verifica_loja(loja: Loja) -> None:
    if is_empty(loja.nome_loja):
        raise Exception("O campo nome da loja é obrigatório")

    if is_empty(loja.logradouro):
        raise Exception('O campo logradouro do endereço é obrigatório')

    if is_empty(loja.municipio):
        raise Exception('O campo município do endereço é obrigatório')

    if is_empty(loja.estado):
        raise Exception('O campo estado do endereço é obrigatório')

    if is_empty(loja.cnpj):
        raise Exception('O campo CNPJ da loja é obrigatório')

    if is_empty(loja.inscricao_estadual):
        raise Exception('O campo inscrição estadual da loja é obrigatório')


def dados_loja_objeto(loja: Loja) -> str:
    # Implemente aqui
    verifica_loja(loja)

    numero = int()
    try:
        numero = int(loja.numero)
    except Exception:
        numero = 0

    if numero <= 0:
        numero = "s/n"

    linha2 = f"{loja.logradouro}, {numero}"
    if not is_empty(loja.complemento):
        linha2 += f" {loja.complemento}"

    linha3 = str()
    if not is_empty(loja.bairro):
        linha3 += f"{loja.bairro} - "
    linha3 += f"{loja.municipio} - {loja.estado}"

    linha4 = str()
    if not is_empty(loja.cep):
        linha4 = f"CEP:{loja.cep}"
    if not is_empty(loja.telefone):
        if not is_empty(linha4):
            linha4 += " "
        linha4 += f"Tel {loja.telefone}"
    if not is_empty(linha4):
        linha4 += "\n"

    linha5 = str()
    if not is_empty(loja.observacao):
        linha5 = loja.observacao

    output = f"{loja.nome_loja}\n"
    output += f"{linha2}\n"
    output += f"{linha3}\n"
    output += f"{linha4}"
    output += f"{linha5}\n"
    output += f"CNPJ: {loja.cnpj}\n"
    output += f"IE: {loja.inscricao_estadual}"

    return output
