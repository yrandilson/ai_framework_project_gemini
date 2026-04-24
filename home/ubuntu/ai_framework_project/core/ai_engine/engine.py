import os
import google.generativeai as genai

class AIEngine:
    """
    Motor de IA responsável por interagir com modelos de linguagem (LLMs).
    Agora configurado para usar o Google Gemini.
    """

    def __init__(self, api_key=None, model_name="gemini-1.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt, system_prompt="Você é um assistente útil."):
        """
        Gera uma resposta para o prompt fornecido usando o Gemini.
        """
        try:
            # No Gemini, o system prompt pode ser passado na criação do modelo ou como parte do contexto
            # Para manter a simplicidade e compatibilidade com o fluxo anterior:
            full_prompt = f"{system_prompt}\n\nUsuário: {prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar resposta do Gemini: {str(e)}"

    def analyze_data(self, data, instruction):
        """
        Analisa dados com base em uma instrução específica.
        """
        prompt = f"Dados para análise: {data}\nInstrução: {instruction}"
        return self.generate_response(prompt, system_prompt="Você é um analista de dados especializado.")

    def make_decision(self, context, options):
        """
        Toma uma decisão com base no contexto e nas opções fornecidas.
        """
        prompt = f"Contexto: {context}\nOpções: {options}\nQual a melhor opção? Responda apenas com o nome da opção."
        return self.generate_response(prompt, system_prompt="Você é um tomador de decisões preciso.")
