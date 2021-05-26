- Streams
  - fluxo cte de dados

- Mndar DB para o S3
  - 2 maneiras
      - carga
      - CDC (change data capture): assim que ocorre a mudança ela é replicada no bd
          - timestamp
          - diff comparison: costuma ser mais eficiente que o timestamp
          - triggers
          - transaction log

- DB Migration Service 
  - AWS Database Migration Service(AWS DMS): migrar ou replicar os BDs e data warehouses para AWS
    - Bulk Load - trazer, carregar os dados para o serviço da AWS
  
  - AWS Schema Conversation Toll (AWS SCT): converte os Schemmas dos BDs e data warehouse para serviços equivalentes na AWS
    - ferramenta desktop