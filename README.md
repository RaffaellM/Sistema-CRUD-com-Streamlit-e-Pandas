As Ferramentas Utilizadas
VS Code (Visual Studio Code): O editor de código onde escrevemos o script e utilizamos o terminal integrado.

Python: A linguagem de programação que processa toda a lógica.

Streamlit (Biblioteca):

Função: É o Servidor Web e a Interface Gráfica.

O que fez: Substituiu a necessidade de usar HTML, CSS ou JavaScript. Ele criou os botões, caixas de texto e a tabela visual no navegador.

Pandas (Biblioteca):

Função: É o Motor de Dados.

O que fez: Gerenciou as informações na memória (RAM) em formato de tabela (DataFrame), permitindo filtrar, adicionar e excluir linhas facilmente.

CSV (Arquivo dados.csv):

Função: É o Banco de Dados.

O que fez: Garante a persistência. Quando você fecha o site, os dados ficam salvos nesse arquivo de texto simples para não serem perdidos.

2. O Que o Código Faz (Lógica do CRUD)
O script app.py funciona num ciclo constante (loop) toda vez que você interage com a tela:

Inicialização: O código verifica se o arquivo dados.csv existe. Se não existir, ele cria um vazio.

Leitura (Read): O Pandas lê o CSV e mostra na tela usando o comando st.dataframe.

Criação (Create): O usuário digita dados, o Pandas cria uma nova linha, "cola" na tabela antiga (pd.concat) e salva no CSV.

Atualização (Update): O código localiza uma linha específica pelo ID e substitui os valores das colunas, salvando novamente no CSV.

Exclusão (Delete): O código filtra a tabela para manter tudo o que não for aquele ID, efetivamente removendo a linha indesejada.
