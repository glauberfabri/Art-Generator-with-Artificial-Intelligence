"""
Ponto de entrada para o Gerador de Arte.
"""
import toml
import os

try:
    secrets = toml.load("config/secrets.toml")
    api_key = secrets.get("default", {}).get("OPENAI_API_KEY", "Não encontrada")
    print("Chave carregada manualmente:", api_key)
except Exception as e:
    print("Erro ao carregar manualmente:", e)

if api_key and api_key != "Não encontrada":
    from views.art_view import ArtView
    art_view = ArtView(api_key)
    art_view.display()
else:
    print("Erro: Chave OPENAI_API_KEY não encontrada ou inválida.")