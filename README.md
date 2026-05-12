# Validador de CPF e Formatação em Arquivos `.txt`

Programa simples desenvolvido em Python para validar inconsistências de formatação em arquivos texto utilizados em processos internos corporativos.

O sistema verifica:

- Quantidade de dígitos do CPF
- Existência do espaçamento esperado entre CPF e nome
- Linhas com possível erro de estrutura

---

# 📌 Objetivo

Esse programa foi criado para automatizar uma validação manual recorrente em arquivos `.txt`, reduzindo erros operacionais e acelerando conferências internas.

---

# ⚙️ Funcionalidades

- Seleção de arquivos `.txt` via janela gráfica
- Leitura automática do conteúdo do arquivo
- Validação linha por linha
- Identificação de:
  - CPF com quantidade incorreta de dígitos
  - Problemas de formatação entre campos
- Exibição das linhas inconsistentes
- Mensagem de sucesso quando não há erros

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter
- pathlib

---

# 📂 Estrutura Esperada do Arquivo

O programa espera linhas no seguinte padrão:

```txt
1234567890  NOME CLIENTE
9876543210  OUTRO CLIENTE
```

### Regras de validação:
- O campo CPF deve conter apenas números
- Deve existir um espaçamento duplo (`"  "`) entre CPF e nome

---

# ▶️ Como Executar

## 1. Instale o Python

Baixe e instale o Python:
https://www.python.org

---

## 2. Execute o programa

No terminal:

```bash
python Main.py
```

---

# 🖥️ Como Funciona

1. O programa abre uma janela para seleção do arquivo `.txt`
2. O arquivo é carregado
3. Cada linha é analisada
4. Caso existam inconsistências:
   - As linhas problemáticas serão exibidas
5. Caso contrário:
   - Será exibida a mensagem:

```txt
Documento não contém erros de CPF e formatação
```

---

# 📋 Exemplo de Saída

## Arquivo com erros

```txt
12345  JOAO
ABCDE12345  MARIA
```

Saída:

```txt
12345  JOAO
ABCDE12345  MARIA
```

---

## Arquivo válido

```txt
Documento não contém erros de CPF e formatação
```
---

# 📄 Licença

Projeto desenvolvido para uso interno/corporativo.

Uso livre para estudos e adaptações internas.

---

# 👨‍💻 Autor

Desenvolvido em Python para automação e validação de arquivos texto corporativos.
