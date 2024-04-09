# Projeto - Extração de Dados I - Santander Coders 

## Sistema de Monitoramento de Notícias sobre Criptomoeda

1. **Consumo de dados com a News API**:

   - Implementamos um mecanismo para consumir dados de notícias de fontes confiáveis e especializadas em criptomoeda a partir da News API:
     [https://newsapi.org/](https://newsapi.org/)

2. **Definição Critérios de Relevância**:

   - Desenvolvemos critérios precisos de relevância para filtrar as notícias. As palavras chave escolhidas para esse projeto foram: bitcoin, blockchain, web3.

3. **Cargas em Batches**:

   - Armazenamos as notícias relevantes em um formato estruturado e facilmente acessível para consultas e análises posteriores. Essa carga deve acontecer 1 vez por hora. Se as notícias extraídas já tiverem sido armazenadas na carga anterior, o processo deve ignorar e não armazenar as notícias novamente, os dados carregados não podem ficar duplicados. Utilizamos um método de comparação de dados históricos com dados novos da API, quando houvesse dados novos o arquivo original csv é subscrito, caso contrário não alteramos o arquivo csv original.

4. **Dados transformados para consulta do público final**:

   - A partir dos dados carregados, aplicamos as seguintes transformações e armazenar o resultado para a consulta do público final:

     - 4.1 - Quantidade de notícias por ano, mês e dia de publicação;

     - 4.2 - Quantidade de notícias por fonte e autor;

     - 4.3 - Quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação definidas no item 2

   - Atualizamos esses dados transformados 1 vez por dia.

5. **API para consulta do público final**:

    - Além das atividades principais, existiu a necessidade de disponibilizar essas informações. Para isso criamos uma API que contém as seguintes funções:

        - retornar todas as notícias
        - retornar notícia por id
        - receber outras notícias que não foram mapeadas pela API original
        - retornar a quantidade de notícias por ano, mês e dia de publicação do item 4.1
        - retornar a quantidade de notícias por fonte e autor do item 4.2
        - retornar a quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação  do item 4.3

6. **Scheduling**:

    - Utilização de cron para scheduling do processo de monitoramento de dados. 