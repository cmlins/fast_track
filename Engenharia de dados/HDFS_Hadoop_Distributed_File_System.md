# HDFS | Hadoop Distributed File System (HDFS) Introduction

- DFS - Distributed File System

    - gerenciar arquivos ou pastas em diversos computadores

    - os dados estão armazenados em um Cluster (vários computadores conectados entre si e funcionam como se fosse uma unidade)

    - Capacidade de ser escalável

- HDFS é um sistema de arquivos distribuidos que permite o armazenamento de dados em Clusters

    - Quem é o responsável pelo armazenamento do dado?

    - Quem distribui o dados pelo cluster?

    - Como o dado é acessado?

    - Existe um nó mestre: NameNode
      - Mantêm e gerencia DataNode (escravo)
      - Grava metadados
      - Recebe sinais dos DataNodes para saber se está tudo funcionando corretamente
    - DataNode
      - Escravos
      - Armazena dos dados
      - O servidor lê e escreve requisições dos clientes
    - Cada arquivo é armazenado no HDFS em blocos
    - O tamanho padrão do bloco é de 128 MB no Apache Hadoop 2.x
    - Falha no DataNode: se um dos nós contendo um bloco de dado falha
      - Solução: Replication Factor: cada bloco de dado é replicado (três vezes por padrão) e eles são distribuídos em diferentes DataNodes
      - `hdfs dfs -ls /user/<nome-user>`: visualiza os hdfs do usuario
      - `hdfs dfs -mkdir /user/<nome-user>/<nome-do-novo-hdfs>`: cria um novo hdfs do usuario
      - `hdfs dfs -put <nome-do-arquivos-que-vão-ser-copiados-para-hdfs> /user/<nome-user>/<nome-do-hdfs-destino>`: envia um arquivo para um sistema
      - `hadoop fsck /user/<nome-user>/<nome-do-hdfs-destino>/<nome-do-arquivo>`: visualiza as informações do armazenamento --> Quantos blocos foram criados, número de vezes que foram replicados ...


## Referências:

[What is HDFS | Hadoop Distributed File System (HDFS) Introduction | Hadoop Training | Edureka](https://www.youtube.com/watch?v=GJYEsEEfjvk)

[Entenda de uma vez por todas o que é MapReduce - O que é Hadoop? (Parte 3)](https://www.youtube.com/watch?v=rISmbGoO-cM)


