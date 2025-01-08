"""
Controla a lógica para geração de arte com IA.
"""
from models.art_generator_model import ArtGeneratorModel

class ArtController:
    """Classe para gerenciar prompts e gerar imagens."""
    def __init__(self, api_key):
        self.model = ArtGeneratorModel(api_key)

    def create_art(self, prompt):
        """Recebe um prompt e retorna a URL da imagem gerada."""
        return self.model.generate_image(prompt)
