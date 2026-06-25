# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Sua tarefa (Parte 2 da atividade, 0,3):** responder com **suas palavras**
(2–4 frases por item), olhando o arquivo `academia.py` da pasta da aula.
Substitua cada `...` pela sua resposta.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?
Escreva no formato "a classe faz **X** e **Y** e **Z**":

> A classe faz o processamento das regras de negócio (cálculo de valores e controle de check-ins) e a interação com a interface do usuário (exibição de menus e leitura de inputs) e o envio de notificações (aviso aos alunos).

## 2. Aponte, no código, **uma linha** de cada responsabilidade
(diga o número da linha e cole o trecho)

- **Regra de negócio** (cálculo / contagem): linha 18 — `valor = 100.0`
- **Tela** (interface com o usuário): linha 14 — `nome = input("Nome do aluno: ")`
- **Notificação** (aviso ao aluno): linha 33 — `print(f"Bem-vindo, {nome}!")`

## 3. Como o SRP separa essas responsabilidades?
Diga **em qual componente** cada responsabilidade passa a morar:

> O SRP distribui as funções para componentes especializados: a regra de negócio é transferida para o AcademiaService, a interface com o usuário é mantida no main e a responsabilidade de enviar avisos passa a morar exclusivamente no componente Notificador.

## 4. Por que ficou melhor? Cite **um** RNF
(manutenibilidade, testabilidade **ou** extensibilidade — veja `docs/requisitos.md`)
e explique em 1–2 frases:

> Melhora a **testabilidade**, pois ao separar as responsabilidades, podemos criar testes automatizados para as regras de negócio de forma isolada, sem a necessidade de interagir com o teclado ou disparar mensagens reais durante os testes.
