# Automação de Cadastro de Produtos com Python

Este projeto foi desenvolvido em Python para automatizar o processo de cadastro de produtos em um sistema web.  
A automação simula interações do usuário com o computador, preenchendo formulários automaticamente a partir de uma base de dados.

## Objetivo

Demonstrar como utilizar Python para automatizar tarefas repetitivas, como login em sistemas e preenchimento de formulários, aumentando a eficiência e reduzindo o trabalho manual.

## Funcionalidades

- Abertura automática do navegador
- Acesso ao sistema web
- Login automático na plataforma
- Leitura de uma base de dados em CSV
- Preenchimento automático dos campos do formulário
- Cadastro automático de múltiplos produtos

## Tecnologias Utilizadas

- Python
- PyAutoGUI
- Pandas

## Como o projeto funciona

1. O script abre automaticamente o navegador.
2. Acessa a página do sistema.
3. Realiza o login com email e senha.
4. Importa uma base de dados contendo produtos.
5. Para cada produto da base:
   - Preenche os campos do formulário automaticamente
   - Envia o cadastro
   - Repete o processo até finalizar todos os registros.

## Estrutura dos dados

O arquivo `produtos.csv` contém as seguintes colunas:

- codigo
- marca
- tipo
- categoria
- preco_unitario
- custo
- obs

Cada linha representa um produto que será cadastrado automaticamente no sistema.

## Como executar o projeto

1. Instale as dependências necessárias: ```pip install pyautogui pandas```
2. Certifique-se de que o arquivo `produtos.csv` esteja na mesma pasta do script.
3. Execute o script Python: ```python main.py```

⚠️ Observação:  
A automação utiliza coordenadas de tela para clicar nos campos do sistema. Dependendo da resolução do monitor ou da posição da janela, pode ser necessário ajustar as coordenadas no código.

## Aprendizados

Este projeto permitiu praticar:

- Automação de tarefas com Python
- Interação com interfaces gráficas
- Manipulação de dados com Pandas
- Leitura de arquivos CSV
- Estruturação de scripts para automação

---

Projeto desenvolvido para fins de estudo e prática em automação com Python.
