### Particionamento

- Organizar pelo nome da chave no Data Lake no S3
- Torna a pesquisa mais rápida e barata

### Compressão

- Comprimir os dados pode acelerar as queries
- Os formatos splittable permitem o processamento paralelo nos nós
- Formatos:
  - Gzip: - bom para arquivos de textos
          - não é splittable -> o usuario tem q baixar o arquivo inteiro para ler o arquivo
  - bzip2:- é spittable
          - compressão mt rápida
  - LZO:  - Splittable
  - Snappy: - Tem um algoritmo de descompressão mt rápido
- Menor qtd de grandes arquivos é melhor que muitos arquivos de tamanho menor

### Catálogo e tranformação dados

- AWS GLUE
  - Crawlers: ajuda a catalogar os arquivos

### Consultas

- AWS Athena
  - Serverless
  - Cobrado por MB lido