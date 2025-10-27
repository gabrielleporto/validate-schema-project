## Validador de Schema CSV — COVID Data

Este projeto tem como objetivo validar automaticamente o schema (estrutura de colunas) de arquivos CSV que contêm dados diários da COVID.  
Ele compara o arquivo recebido com um arquivo de referência para garantir que a estrutura continue a mesma — algo essencial antes de atualizar dashboards, como o Power BI.

## Funcionalidade

O script verifica se o novo arquivo CSV possui:
- As mesmas colunas do arquivo de referência.
- As colunas na mesma ordem (por padrão).
- (Opcional) A possibilidade de ignorar a ordem das colunas, se desejado.

Se o schema for idêntico → imprime uma mensagem de aceite.  
Se houver qualquer diferença →  exibe as colunas divergentes.

## Estrutura do projeto

validate-schema-project/
├── validate_schema.py      # Código principal
├── country_wise_latest_REF.csv   # Arquivo CSV de referência (exemplo)
├── country_wise_latest_NEW.csv   # Arquivo CSV de teste (exemplo)
└── README.md               # Documentação do projeto

## Requisitos

- Python 3.8+
- Bibliotecas: pandas

## Personalizações

Para ignorar a ordem das colunas, altere a linha:
  colunas_iguais = list(df_ref.columns) == list(df_novo.columns)

para:
  colunas_iguais = set(df_ref.columns) == set(df_novo.columns)
