import PyPDF2

# Função para ler o conteúdo do PDF
def ler_pdf(caminho_arquivo):
    texto = ""
    try:
        # Verifica se o arquivo existe
        with open(caminho_arquivo, "rb") as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF: {e}")
    return texto

# Solicitar ao usuário o caminho do arquivo PDF
caminho_pdf = input("Digite o caminho completo do arquivo PDF: ")

# Lê o conteúdo do PDF e imprime no console
conteudo = ler_pdf(caminho_pdf)

# Exibe o conteúdo do PDF
if conteudo:
    print("\nConteúdo do PDF:\n")
    print(conteudo)
else:
    print("Não foi possível extrair o conteúdo do arquivo PDF.")
