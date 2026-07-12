class Cadastro :
    def __init__ (self ,cliente ,descricao ):
        self .cliente =cliente 
        self .descricao =descricao 


class Orcamento (Cadastro ):
    def __init__ (
    self ,
    cliente ,
    descricao ,
    material ,
    quantidade ,
    area ,
    montagem ,
    taxa_cartao ,
    observacao 
    ):
        super ().__init__ (cliente ,descricao )

        self .material =material 
        self .quantidade =quantidade 
        self .area =area 
        self .montagem =montagem 
        self .taxa_cartao =taxa_cartao 
        self .observacao =observacao 

    def __str__ (self ):
        return (
        f"Cliente: {self .cliente } | "
        f"Descrição: {self .descricao } | "
        f"Material: {self .material .nome }"
        )