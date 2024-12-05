# INFNET 
## TP 3 - Data Driven APPs
### Aluno: Rodrigo Moreira Avila

---
### Sobre o projeto:
Aplicação que implementa ReAct Agents para resolver problemas usando LLM

#### Problema:
Muitos LLMs possuem dados até um certo ponto, e não conseguem acessar a internet para buscar informações em tempo real. A ideia é criar um sistema que possa buscar informações em tempo real e atualizar a resposta da LLM.

#### Solução:
Implementar um sistema de busca em tempo real para que a resposta da LLM seja atualizada, utilizando Wikipedia e DuckDuckGo como fontes de dados.

#### Reflexão:
Com a implementação do sistema de busca em tempo real, a LLM pode ser utilizada para resolver problemas que necessitam de informações atualizadas. Sem isso, a LLM não seria capaz de resolver problemas que necessitam de informações em tempo real e o usuário teria que ir buscar na fonte de dados diretamente.

Exemplo de testes realizados e com resultados satisfatórios:
- What is the latest iphone model?
- Who is the president of Brazil?
- Who is Donald Trump?

### Estrutura do projeto:
```./README.md``` - Este arquivo.

```./src/*``` - Contém o código fonte da aplicação com a resolução de todos os exercícios.

```./images/*``` - Contém os prints para os exercícios.

```./requirements.txt``` - Contém as dependências do projeto.


### Como rodar o projeto streamlit:
1. Configurando versão do python:
```bash
pyenv local 3.11.9
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute a aplicação:
```bash
python3 src/langchain_app.py
```