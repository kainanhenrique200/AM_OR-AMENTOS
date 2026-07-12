class Metragem :

    def __init__ (self ,descricao ,largura ,comprimento ):
        self .__descricao =descricao 
        self .__largura =largura 
        self .__comprimento =comprimento 

    def calcular_area (self ):
        return self .__largura *self .__comprimento 

    def __str__ (self ):
        return (
        f"{self .__descricao } | "
        f"{self .__largura }m x "
        f"{self .__comprimento }m | "
        f"Área: {self .calcular_area ():.2f} m²"
        )