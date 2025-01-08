import openai

class ArtGeneratorModel:
    """Classe para integrar com o modelo de IA para geração de imagens."""
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_image(self, prompt):
        """Gera uma imagem com base no prompt fornecido."""
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            return response["data"][0]["url"]
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar imagem: {e}")
