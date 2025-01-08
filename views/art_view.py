"""
Configura a interface interativa para gerar arte com IA usando Streamlit.
"""
import streamlit as st
from controllers.art_controller import ArtController
import os

class ArtView:
    """Classe para exibir a interface de geração de arte."""
    def __init__(self, api_key):
        self.controller = ArtController(api_key)

    def display(self):
        """Exibe a interface do usuário."""
        st.set_page_config(page_title="AI Art Generator", layout="wide")
        st.title("AI Art Generator")
        st.markdown("Crie arte com a ajuda de modelos de inteligência artificial.")

        prompt = st.text_input("Digite um prompt para a imagem:")

        if st.button("Gerar Imagem") and prompt:
            st.write(f"Prompt recebido: {prompt}")  # Adicionado para debug
            with st.spinner("Gerando imagem..."):
                try:
                    image_url = self.controller.create_art(prompt)
                    st.image(image_url, caption="Arte Gerada", use_column_width=True)
                except Exception as e:
                    st.error(f"Erro ao gerar imagem: {e}")


        st.markdown("---")
        st.markdown("Imagens geradas serão armazenadas localmente na pasta `generated_images/`.")