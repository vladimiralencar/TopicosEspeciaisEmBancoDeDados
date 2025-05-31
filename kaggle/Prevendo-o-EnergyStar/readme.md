Dataset e Solução: https://www.kaggle.com/valencar/competi-o-dsa-modelo-xgboost

Você está participando de um processo de seleção para Cientista de Dados em uma grande empresa multinacional. A empresa definiu um problema e quer saber como você pode solucioná-lo explorando o conjunto de dados, realizando análise estatística e desenvolvendo um modelo para previsões.

O conjunto de dados anexado a esta competição contém dados sobre a eficiência energética de edifícios. O dataset foi extraído do web site Open Data for All New Yorkers (https://opendata.cityofnewyork.us/). Alternativamente o dataset pode ser encontrado aqui: https://catalog.data.gov/dataset

Nossa hipótese é que esse conjunto de dados contém variáveis ​​independentes que podem ser usadas para inferir fatos interessantes sobre outros edifícios em Nova York. O principal interesse é a pontuação (score) de Energy Star, pois acreditamos que essa pontuação é usada como uma medida agregada do desempenho energético de um prédio. Nossa pergunta é simples:

Este conjunto de dados contém um conjunto de variáveis ​​independentes que se correlacionam com a classificação "Energy Star" do edifício? Para edifícios sem a pontuação Energy Star, você pode inferir qual a pontuação deles?

Obs: Não sabe o que é Energy Star? Então pesquise, pois conhecimento de negócio faz parte dos skills de um Cientista de Dados. Aqui uma fonte de informação útil: https://www.energystar.gov/ia/partners/spp_res/neprs/ENERGY_STAR_and_Automated_Benchmarking_Quick_Facts.pdf

Para responder a esta pergunta, pedimos que você prepare uma investigação fundamentada dessa hipótese. Acreditamos que o melhor método é realizar descrições estatísticas visuais dos dados usando tabelas de resumo ou uma biblioteca de gráficos de sua escolha (análise exploratória). Então treine um modelo e avalie-o. Você pode usar regressão para prever a pontuação numérica (embora outros métodos de aprendizagem de máquina possam ser usados neste dataset, esta competição considera que você usará regressão).

Analisando os dados brutos, podemos ver vários problemas que deverão ser resolvidos antes da modelagem preditiva. Existem 60 colunas e não sabemos o que muitas delas significam! Tudo o que sabemos da declaração do problema é que queremos prever o número na coluna de pontuação. Algumas das outras definições de coluna podem ser razoavelmente adivinhadas, mas outras são difíceis de entender. No aprendizado de máquina, isso não é realmente um problema, porque deixamos o modelo decidir quais recursos são importantes. Às vezes, podemos nem receber nomes de coluna ou saber o que estamos prevendo. No entanto, é sempre importante entender o problema na medida do possível e, como também queremos interpretar os resultados do modelo, seria uma boa ideia ter algum conhecimento das colunas. Para uma descrição completa do dataset, acesse: https://www1.nyc.gov/html/gbee/html/plan/ll84.shtml

Crie um ou mais modelos (você usar diferentes algoritmos de regressão) e nos dê uma interpretação de seu desempenho, que você pode usar para responder à questão de saber se esse conjunto de dados contém informações suficientes para entender a relação de uma pontuação Energy Star com edifícios de diferentes tipos. Para o desempenho do modelo, gostaríamos de ver métricas de avaliação típicas / apropriadas como pontuações de F1, R Squared, resíduos, etc. Esta competição considera como métrica de avaliação o MAE (Mean Absolute Error).

Dataset e Solução: https://www.kaggle.com/valencar/competi-o-dsa-modelo-xgboost
