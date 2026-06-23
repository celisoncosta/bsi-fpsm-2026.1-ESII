# Documento de Diagnóstico —  BRUNA DO SOCORRO PEREIRA MARTINS, CELISON FARIAS DA COSTA E RAIMUNDO SANTANA LOPES.

## Problema 1. Falta de exibição dos equipamentos cadastrados para seleção (Divergência de Usabilidade)
- O que a documentação diz: No caso de uso UC01 (passos 2 e 3), o sistema deve solicitar o identificador do equipamento e o atendente deve informá-lo para prosseguir com o registro.
- O que o código faz: O sistema pede diretamente o número do ID através de um campo de digitação vazio, sem listar previamente na tela quais são os equipamentos cadastrados no banco de dados e se eles estão livres.
- Por que isso é um problema: O atendente não tem como adivinhar quais IDs existem no sistema e quais aparelhos estão disponíveis no inventário, sendo forçado a decorar os códigos ou errar por tentativa e erro. Esse pode ser considerado como não documentado.

## Problema 2. Falta de validação do prazo mínimo de empréstimo (RN02)
- O que a documentação diz: A regra de negócio RN02 especifica que o prazo mínimo permitido para a realização de um empréstimo é de 1 dia.
- O que o código faz: O método `registrar()` aceita qualquer número digitado no campo de dias, realizando o cálculo da data de devolução mesmo se o usuário digitar 0 ou um número negativo de dias.
- Por que isso é um problema: Permite que atendentes cometam erros operacionais graves, gerando empréstimos inválidos no sistema sem que nenhum alerta seja emitido.

## Problema 3. Ausência de mensagem quando não há empréstimos atrasados (UC03)
- O que a documentação diz: No caso de uso UC03 (passo 4), está determinado que: " Se não houver atrasos, sistema exibe "Nenhum empréstimo em atraso".
- O que o código faz: O método `listar_atrasados()` varre a lista e, caso não encontre nenhum registro vencido, simplesmente encerra a sua execução em branco, deixando a tela do usuário vazia.
- Por que isso é um problema: Causa extrema confusão para quem está usando o sistema, pois o usuário fica sem saber se o sistema travou, se a busca falhou ou se realmente não existem atrasos.

## Problema 4. Falta de confirmação explícita ao registrar empréstimo (RI02)
- O que a documentação diz: O requisito de interface RI02 determina que: “Toda operação concluída com sucesso deve exibir mensagem de confirmação explícita ao usuário.”
- O que o código faz: Quando o método `registrar()` conclui o processo, ele grava os dados, mas a única coisa que aparece na tela é a simulação do envio de e-mail `[EMAIL]`. Não há nenhuma linha dizendo "Empréstimo gravado com sucesso" ou mostrando a data na interface de atendimento.
- Por que isso é um problema: O atendente de TI fica sem uma resposta visual direta do sistema confirmando que aquela operação foi de fato salva no banco de dados.

## Problema 5. Risco de travamento total por digitação de letras em campos numéricos (Fragilidade de Código)
- O que a documentação diz: Os requisitos de usabilidade dão a entender que o sistema deve ser operável por técnicos de suporte de forma contínua no dia a dia da UFRA.
- O que o código faz: Ao solicitar o ID do equipamento ou a quantidade de dias, o código tenta transformar a digitação diretamente em número inteiro usando `int(input())`. Se o atendente esbarrar em uma letra por engano, o programa fecha na hora e exibe um erro de tela azul/terminal (`Traceback (most recent call last):
  File "/workspaces/bsi-fpsm-2026.1-ESII/aula01/emprestimos.py", line 122, in <module>
    main()
  File "/workspaces/bsi-fpsm-2026.1-ESII/aula01/emprestimos.py", line 111, in main
    int(input("Dias: "))
ValueError: invalid literal for int() with base 10: 'g'`).
- Por que isso é um problema: O atendente perde todo o histórico de operações feitas naquela sessão se o sistema cair repentinamente por causa de um simples erro de digitação.
