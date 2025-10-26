import pandas as pd

def validar_schema(caminho_referencia, caminho_novo):
    """
    Valida se o schema (estrutura de colunas) de um arquivo CSV novo 
    é idêntico ao de um arquivo CSV de referência.

    A função compara os nomes e a ordem das colunas entre dois arquivos CSV.
    Caso o schema seja igual, imprime uma mensagem de aceite.
    Caso contrário, exibe as diferenças encontradas.

    Args:
        caminho_referencia (str): Caminho completo para o arquivo CSV de referência.
        caminho_novo (str): Caminho completo para o novo arquivo CSV a ser validado.

    Returns:
        None
        (A função apenas imprime mensagens no console.)

    Exemplo:
        >>> validar_schema(
        ...     r"C:\\dados\\covid_ref.csv",
        ...     r"C:\\dados\\covid_hoje.csv"
        ... )
        Schema válido: o novo CSV possui as mesmas colunas e estrutura do arquivo de referência.
    """

    df_ref = pd.read_csv(caminho_referencia, nrows=0)
    df_novo = pd.read_csv(caminho_novo, nrows=0)

    colunas_iguais = list(df_ref.columns) == list(df_novo.columns)

    if colunas_iguais:
        print("Schema válido: o novo CSV possui as mesmas colunas e estrutura do arquivo de referência.")
    else:
        print("Schema diferente detectado!")
        print("\nColunas do arquivo de referência:")
        print(list(df_ref.columns))
        print("\nColunas do novo arquivo:")
        print(list(df_novo.columns))

validar_schema(r"c:\Users\DPedro\Desktop\country_wise_latest_REF.csv", r"c:\Users\DPedro\Desktop\country_wise_latest_NEW.csv")
