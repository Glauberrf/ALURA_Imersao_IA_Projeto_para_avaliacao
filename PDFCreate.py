from fpdf import FPDF


def ContractGenerate(chatID, Texto):  
    
    pdf = FPDF()
    pdf.add_page()

    # Defina a fonte e o tamanho do título
    pdf.set_font("Arial", "B", 16)

    # Defina a fonte e o tamanho do texto normal
    pdf.set_font("Arial", "", 12)    
 
    string_grande = Texto

    # Divida a string na primeira frase e no restante do texto
    primeira_frase, restante_texto = string_grande.split("\n", 1)

    # Formate e adicione o título
    pdf.cell(0, 10, primeira_frase, align='C', ln=1)

    # Formate e adicione o restante do texto
    pdf.multi_cell(0, 6, restante_texto)

    pdf.output("Contrato.pdf")

