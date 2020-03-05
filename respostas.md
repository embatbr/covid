# Respostas

## Qual​ o objetivo​​ do comando​ cache​ em​ Spark?

O Spark utiliza lazy evalutation. Isso significa que uma série de transformações encadeadas só serão executadas no momento em que uma ação é chamada (e.g., collect). Logo, caso parte dessas transformações possam ser reutilizadas, faz sentido consolidar seu resultado em memória. Para tanto, cachear é uma boa solução.

## O mesmo​ código​ implementado​ em​ Spark​ é normalmente​ mais​ rápido​ que​ a implementação​ equivalente​ em MapReduce.​ Por​ quê?

Por default, o Spark opera in memory. MapReduce (e.g., Hadoop) lê de sistema(s) de arquivos (geralmente HDFS), executa as operações e escreve o resultado em sistema(s) de arquivos.

## Qual a função do SparkContext?

"Iniciar" o Spark e permitir acesso ao cluster (via código).

## Explique​ com​ suas​ palavras​ o que​ é Resilient​ Distributed​ Datasets​​ (RDD).

Um conjunto de dados (estruturados ou não - depende da sua definição) que existem no cluster (distributed) e não são efêmeros (resilient - pelo menos enquanto o Spark estiver "ligado"). RDDs podem ser acessados sem a necessidade de entender sua organização interna (pelo menos para atividades menos complexas), basicamente como se fosse uma variável num fluxo simples de qualquer linguagem de programação.

## GroupByKey​ é menos​ eficiente​ que​ reduceByKey​ em​ grandes​ dataset. Por​ quê?

groupByKey agrupa objetos de acordo com a key determinada. Precisará mover dados para que estejam localmente próximos (quanto menos espalhamento por key no cluster, melhor). Seu resultado ainda são os mesmos objetos (não há modificação). Se o dataset estiver mais espalhado ainda (um cluster de muitas máquinas pequenas), haverá mais tráfego, aumentando seu tempo de processamento.

reduceByKey opera aplicando uma função aos objetos, com um resultado por key (não uma coleção de objetos). Logo, a função pode ser aplicada localmente e seu resultado servir como entrada para a próxima sequência de aplicações, diminuindo a quantidade de tráfego (e o tamanho do payload). Por exemplo, aplicar uma função soma permite que os resultados locais sejam acumulados e usados como entrada para a rodada seguinte (inter-node). Não há deslocamento e rearranjo dos objetos.

## Explique​ o que​ o código​ Scala​ abaixo​ faz.

```scala
val​​ textFile​​ = sc​.textFile​("hdfs://..."​)
val​​ counts​​ = textFile​.flatMap​(line​​ => line​.split​(" "))
​​                     .map​(word​​ => (word​, 1))
​​                     .reduceByKey​(_ + _)
counts​.saveAsTextFile​("hdfs://..."​)
```

- Lê um dataset (em formato texto) guardado no HDFS. Por default, o input será uma coleção de linhas de texto;
- Divide todo o texto em palavras. flatMap é usado ao invés de map porque vai "abrir" todo o input;
- Mapeia cada palavra para uma tupla composta da palavra e do número 1. A tupla é naturalmente "vista" como um conjunto de chaves e valores (o conteúdo de `word` é a chave e `1` é o valor);
- Soma as "quantidades" pela chave, fazendo um `countByKey`;
- Salva o resultado no hdfs.
