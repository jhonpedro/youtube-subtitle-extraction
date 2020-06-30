# Algorithm for ratio

Utiliza um input para definir qual lógica deve ser usada no calculo da razão

Lógica `1`: Usa `Todas as palavras sem a repetição entre elas` dividido por `Todas as palavras com a repetição entre elas`

Lógica `2`: Usa `Todos os substantivos sem a repetição entre eles` dividido por `Todos os substantivos com a repetição entre eles`

Ambos retiram as chamadas StopWords para essas palavras não interfiram no cálculo, já que elas representam boa parte das palavras ditas, e são palavras que dependendo do contexto não agregam valor.

Exemplo Lógica `1`: Vídeo com 1600 palavras, somente 760 palavras líquidas. Razão: 760/1600 = 0.475

Exemplo Lógica `2`: Vídeo com 500 substantivos, somente 270 substantivos líquidos. Razão: 270/500 = 0.54

# Algorithm for resource types

Esse código basicamente exige uma tabela .csv, nela a primeira coluna devem ter os links dos vídeos do youtube, na segunda os tópicos que desejam buscar nas legendas do vídeo.

Exemplo: Buscar 4 tópicos: matemática, português, artes, história. Caso o vídeo contenha na legenda essas palavras a 3 coluna do .csv que sera gerado registrara `100`, caso contenha somente a palavra matemática será registrado `20` 