import os
import google.generativeai as genai
import PyPDF2

# Configuração da API com a chave fornecida
api_key = ''  # Substitua pela sua chave de API
os.environ["API_KEY"] = api_key
genai.configure(api_key=os.environ["API_KEY"])

# Função para ler o conteúdo do arquivo PDF
def ler_pdf(caminho_arquivo):
    texto = ""
    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return texto

    try:
        # Abre o PDF e lê todas as páginas
        with open(caminho_arquivo, "rb") as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF: {e}")
    return texto

# Função principal do chatbot
def chatbot():
    print("Bem-vindo ao Rego.AI")
    print("Digite o caminho do arquivo PDF que deseja ler e a pergunta.")
    print("Exemplo: /caminho/para/arquivo.pdf Como funciona o conteúdo desse PDF?")
    print("Para sair, digite 'sair'.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            print("Saindo do chat. Até logo!")
            break

        try:
            # Separa o caminho do PDF e a pergunta do usuário
            partes_input = user_input.split(" ", 1)
            caminho_pdf = partes_input[0]  # Caminho do arquivo
            pergunta = partes_input[1] if len(partes_input) > 1 else None  # Pergunta do usuário

            # Verifica se o caminho do PDF é válido
            if not os.path.exists(caminho_pdf):
                print(f"O arquivo {caminho_pdf} não foi encontrado.")
                continue

            # Tentar ler o conteúdo do PDF
            conteudo_pdf = ler_pdf(caminho_pdf)

            if conteudo_pdf.strip():  # Verifica se o conteúdo não está vazio
                if pergunta:
                    # Usa o modelo Gemini para gerar a resposta
                    model = genai.GenerativeModel("gemini-1.5-flash")

                    # Cria o prompt combinando o conteúdo do PDF com a pergunta do usuário
                    prompt = f"Com base no seguinte conteúdo extraído do PDF:\n\n{conteudo_pdf}\n\nResponda à seguinte pergunta: {pergunta}"

                    # Gera o conteúdo com base no prompt
                    response = model.generate_content(prompt)
                    print(f"Rego: {response.text}\n")
                else:
                    print("Nenhuma pergunta foi fornecida após o caminho do PDF.")
            else:
                print("Não consegui ler o conteúdo do arquivo. Certifique-se de que o caminho está correto e que é um PDF.")

        except Exception as e:
            print(f"Ocorreu um erro ao processar a entrada: {e}")

# Inicializa o chatbot
chatbot()
