- RDD:
  - Resilient
  - Distributed
  - Dataset
- Transforming RDD:
  - map
  - flatmap
  - filter
  - distinct
  - sample
  - union, intersection, subtract, cartesian
- RDD actions
  - colletc
  - count
  - countByValue
  - take
  - top
  - reduce
  - ...
- Lazy evaluation
  - Nada acontece no programa até a chamada de uma ação
- exemplo:
```
    from pyspark.sql import SQLContext, Row
    hiveContext = hiveContext(sc)
    inputData = spark.read.json(dataFile)
    inputData.createOrReplaceTempView("myStructuredStuff")
    myResultDataFrame = hiveContext.sql("""SELECT foo FROM bar ORDER BY foobar""")
    myResultDataFrame.show()
    myResultDataFrame.select("someFieldName")
    myResultDataFrame.filter(myResultDataFrame("someFieldName" > 200))
    myResultDataFrame.groupBy(myResultDataFrame("someFieldName")).mean()
    myResultDataFrame.rdd().map(mapperFunction)
```

## Putty
```
Host name: maria_dev@127.0.0.1
Port: 2222

Saved Sessions: HDF
```

## MapReduce


- Divide o dado em partições que são mapeadas (transformadas) e reduzidas (agregadas)
pelas funções mapper e reducer definidas

- Mapper - converte os dados fontes em par chave/valor

- MapReduce Ordena e agrupa o dado mapead ("shuffle and Sort")

- Reducer - processa o valor de cada chave

- raw data --> mapper --> shuffle and sort --> reducer

## Comandos
 -Local: python RatingsBreakdown.py u.data

 - python RatingsBreakdown.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data
