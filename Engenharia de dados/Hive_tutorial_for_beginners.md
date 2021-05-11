## Hive

- Permite a leitura, escrita e gerenciamento de petabytes de dados usando SQL
- Integrada ao Apache Hadoop, responsável pelo armazenamento e processamento de grandes conjuntos de dados
- Apache Hive é um sw open-source usado com Hadoop para faciliatar o armazenamento e análise de dados com SQL
  - Data Warehousing Sw Utility
  - Análise de dados
  - Feito para usuários de SQL
  - Gerencia as requisições de dados estruturados
  - Simplifica e abstrai o carregamento no Hadoop
  - Não é preciso aprender Java e Hadoop API
- Aplicações:
  - Mineração de dados 
  - Indexação de documentos
  - Modelagem perditiva
  - Business Inteligence
  - Log processing
- Features do Apache Hive
  - SQL type queries
  - OLAP (Online Analytical Processing)
    - Analisar grandes volumes de informações nas mais diversas perspectivas dentro de um Data Warehouse
    - fornecer suporte à análise de negócios
    - auxilia o cliente nas tomadas de decisão
    - ROLAP - Raltional Online Analytical Processing
    - MOLAP - Multidimensional Online Analytical Processing
    - HOLAP - Hybrid Online Analytical Processing
    - DOLAP - DesktopOnline Analytical Processing
  - Rápido
  - Escalável
  - Extensível
  - Consulta Ad Hoc: tipo de consulta SQL em um banco de dados que é criada na hora, no momento em que surge uma necessidade. Esse tipo de consulta nasce de solicitações não-planejadas, cuja necessidade não fora prevista com antecedência, surgindo de momento.
- Arquitetura
  ![Hive Architecture](hive-architecture.jpg)
  - Hive Client
    - **JDBC Driver**: usado para estabelecer conexão entre a hive e a aplicação java
    - **Thrift Server**: Thrift comes in the architectural part of Hive, Thrift is a protocol for the application which were developed in a different programming languages to communicate. So the Thrift server sits in a hive services layer and this is the one which receives the request or hive queries from client programs. So, client program could be in any application written in C++, JAVA, Python.    
    - **ODBC Driver**: permite que as aplicações que suportam o protocolo ODBC a se conectar ao Hive
  - Hive services
    - **Hive web UI**: Alternativa ao Hive CLI
    - **Hive Server**: Aceita requisições de diferentes clientes e os envia ao Hive Driver
    - **Cli**: shell onde podem ser feitas as requisições e comandos
    - **Hive Driver**: Recebe as requisições de diferentes origens como web UI, CLI, Thrift e JDBC driver e as transfere para o compilador.
    - **MetaStore**: repositório central que armazena toda a informação estruturada de várias tabelas e partições no warehouse
  - MapReduce
  - HDFS
- Apache Hive Components
  - Shell
  - Meta Store
  - Execution Engine
  - Driver
  - Compiler
- 



## Referências:

1. [Hive Tutorial for Beginners | Hive Architecture | Hadoop Hive Tutorial | Hadoop Training | Edureka](https://www.youtube.com/watch?v=S0i4NX1vlCU)
2. [OLAP](https://www.youtube.com/watch?v=ZXQSuKUfY0Y)
3. [O que é uma consulta Ad Hoc em bancos de dados](http://www.bosontreinamentos.com.br/bancos-de-dados/o-que-e-uma-consulta-ad-hoc-em-bancos-de-dados/)
4. [What is thrift in Hive](https://www.edureka.co/community/46070/what-is-thrift-in-hive#:~:text=Thrift%20comes%20in%20the%20architectural,hive%20queries%20from%20client%20programs.)
5. [Hive Architecture](https://www.javatpoint.com/hive-architecture)

