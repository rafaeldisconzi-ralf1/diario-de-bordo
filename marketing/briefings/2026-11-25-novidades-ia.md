# Briefing para a sessão de vídeos — novidades do app (25/11/2026)

Feito pela sessão do app. Leia junto com `CLAUDE.md` e `docs/marketing.md` (regras e o que já funcionou).
Detalhes técnicos das novidades: `docs/app.md`, seção "IA: Pergunte ao Diário e Lançar falando".

## ✅ Status (atualizado 26/11/2026, 12h40)
- **A IA está LIGADA para todos os clientes desde 26/11/2026.** Pode publicar, programar e anunciar.
- Testada de verdade: chat respondeu certo contas de frete, comparação de meses, lucro por km, consumo estranho,
  documentação (manda confirmar na ANTT) e recusou fora do assunto. A voz foi testada pelo Rafael no celular.
- Os exemplos de resposta reais abaixo (seção "Respostas reais") podem ser usados nos criativos, com dados inventados.

## As duas novidades principais

### 1. "Lançar falando" 🎤
- Botão roxo na tela Início, abaixo de Abasteci / Gastei / Diária. Texto do botão: **Lançar falando**.
- O motorista toca, fala e toca em **Pronto, terminei** (até 25 s).
- Exemplos que funcionam: "Abasteci 300 litros a 6 e 19 no posto Graal", "Pedágio 87 reais",
  "Duas diárias de 250", "Paguei 350 de contador" (fora de viagem).
- O app **abre o formulário já preenchido** e mostra "🎤 Você disse: …". Ele confere e toca em Salvar.
- Serve para abastecimento, gasto e diária. Começar e encerrar viagem continuam nos botões.
- Gancho natural: mão suja de graxa, dirigindo cansado, quem não gosta de digitar, letra miúda do celular.

### 2. "Pergunte ao Diário" 💬
- Botão escuro ao lado. Texto do botão: **Pergunte ao Diário**.
- Chat com IA que **olha os lançamentos do próprio motorista** para responder:
  "Quanto sobrou este mês?", "Qual viagem deu mais lucro?", "Qual minha média de km por litro?",
  "Um frete de R$ 6.000 para 1.000 km compensa?", "O que revisar antes de uma viagem longa?".
- Também tira dúvidas de frete, diesel, pneu, manutenção, documentação (ANTT, tacógrafo, descanso) e estrada.
- Só fala de caminhão e estrada. Se perguntar outra coisa, educadamente não responde.
- Dá para perguntar escrevendo ou falando (botão roxo do microfone dentro do chat).

## O que PODE e o que NÃO PODE dizer
Pode:
- "Fala e o app anota pra você. Você só confere e salva."
- "Pergunte quanto sobrou e a IA responde com os SEUS números."
- "Uma IA que só entende de caminhão."

Não pode (é falso ou arriscado):
- Dizer que salva sozinho, sem conferir. **Sempre abre para conferir.**
- Dizer que é ilimitado (tem limite diário: 20 perguntas e 30 usos de voz por dia).
- Dizer que nunca erra. A tela avisa que a IA pode errar.
- Dar a IA como fonte oficial de lei ou documentação. Ela manda confirmar no órgão.
- Citar o nome da empresa ou do modelo de IA por trás (nada de Groq, Llama, ChatGPT). Diga "IA" ou "o Diário".
- Prometer "grátis". A IA vem junto na assinatura.

## Outras novidades do app que viram conteúdo (já no ar para todos)
- **Gasto fora de viagem com as contas do dono**: Parcela do caminhão, Seguro, Imposto, Contador, com escolha do dia.
  Encaixa no tema que já funcionou ("rodando de graça", "metade do que parecia"): quem esquece parcela e seguro
  acha que sobrou mais do que sobrou.
- **Proteção contra erro de digitação**: escreveu 2000 em vez de 20,00? O app avisa e mostra o valor por extenso.
- **Editar** um lançamento ou viagem errada sem apagar.
- **Relatório do mês em planilha**, que vai para o e-mail ou pelo WhatsApp (a viagem conta no mês em que terminou).

## Ideias de peças (sugestão; o Rafael escolhe)
Na análise de 23/11, o que mais deu alcance foi o **Zé com dilema de dinheiro e "Comenta A ou B"**, sempre com voz e
legenda. Nos anúncios, **imagens** venderam mais que vídeos. Por isso:

1. **Zé — "Esse frete compensa?" (série do Zé, com voz)**
   O Zé tem duas propostas (A ou B). Orgânico: termina em "Comenta A ou B". Na resposta do dia seguinte, ele
   **pergunta pro Diário** no app e a IA mostra a conta com os números dele.
2. **Zé — "Mão suja de graxa"** (15–20 s)
   Zé no posto, mão preta, não quer sujar o celular → aperta o microfone, fala "abasteci 300 litros a 6 e 19" →
   formulário preenchido → Salvar. Final: "Fala que o Diário anota."
3. **Demo curta da tela** (10–15 s, para anúncio e Stories): toque no microfone → fala → formulário preenchido.
4. **3 imagens para anúncio** (formatos 9:16 e 4:5, estilo "dor + balão" de `marketing/anuncios/criativo-dor/`):
   - "Não gosta de digitar? Fala que o app anota."
   - Balão de conversa: "Quanto sobrou este mês?" → "Sobrou R$ 4.212,30, já tirando diesel, pedágio e a parcela."
   - "Uma IA que só entende de caminhão."
5. **Carrossel Instagram**: "5 perguntas pra fazer pro seu Diário" (uma por card, resposta curta no card).
6. **"O que quase todo dono esquece na conta"**: parcela, seguro, imposto e contador. Usa os gastos fora de viagem.
   **Pode publicar já**, porque esse recurso está no ar para todos.

## Como gravar as telas da IA antes de ela estar ligada
- Rode o app local com o Supabase falso (como nos outros vídeos). Para os botões aparecerem, use um perfil com
  `admin: true` no `__fakedb` ou troque `IA_PARA_TODOS` para `true` **só na cópia local**. Nunca suba essa troca.
- Intercepte `**/functions/v1/ia` no Playwright e devolva respostas prontas. Exemplo usado nos testes:
  - voz (lançar): `{"texto":"Abasteci 300 litros a 6 e 19 no Posto Graal","lancamento":{"tipo":"diesel","litros":300,"preco":6.19,"obs":"Posto Graal"}}`
  - pergunta: `{"resposta":"Em novembro sobrou **R$ 2.898,00** até agora.\n- Chapecó → Curitiba: sobrou R$ 2.898,00\n- Santos ainda em andamento."}`
- O microfone no Chromium: `--use-fake-ui-for-media-stream --use-fake-device-for-media-stream` e permissão `microphone`.
- **Dados sempre inventados**: motorista Carlos (ou o Zé), Scania R 450, placa ABC 1D23. Nada do pai, nada real.
- As respostas da IA nas telas precisam bater com os números lançados na tela (não invente sobra que não fecha).

## Regras de sempre (de `docs/marketing.md`)
- Roteiro primeiro, para o Rafael aprovar. **Voz na ElevenLabs só depois do ok** (custa crédito). Voz "Arnold - Br".
- Todo vídeo com narração e legenda. Nunca mostrar ou falar o domínio do site.
- Registrar cada peça em `docs/marketing.md` e no documento "onde paramos".

## Respostas reais da IA (teste de 26/11/2026, dados inventados do Carlos)
Use como base para telas e balões (podem resumir, mas sem mudar os números):
- **"Um frete de R$ 6.000 para 1.000 km compensa? Meu caminhão faz 2,5 km/l e o diesel está R$ 6,20."**
  → Diesel: 1.000 ÷ 2,5 = 400 L × R$ 6,20 = **R$ 2.480,00**. Sobra antes de outros gastos: **R$ 3.520,00**.
  "Com esse consumo e preço de diesel, o frete compensa. Lembre de incluir pedágio, alimentação, manutenção e a comissão."
- **"Quanto sobrou em novembro e comparado com outubro?"** → Novembro **R$ 13.034,50**, outubro **R$ 14.685,00**:
  **R$ 1.650,50 a menos**.
- **"Qual viagem deu mais lucro por km?"** → Curitiba → Chapecó: R$ 5.359,50 ÷ 480 km ≈ **R$ 11,16/km**
  (as outras: R$ 4,09/km e R$ 4,67/km).
- **"Tem alguma coisa estranha no meu consumo de diesel?"** → apontou o trecho Curitiba → Chapecó com **1,08 km/L**,
  muito abaixo dos outros (2,5 km/L). Ótimo gancho: "A IA achou o que você não viu."
- **"Me passa uma receita de bolo"** → "Eu só consigo ajudar com assuntos de caminhão, frete e estrada."
  Bom para humor: "Ela só entende de caminhão."

## Ganchos sugeridos agora que está no ar
- "Eu perguntei pro app se o frete compensava. Olha a resposta."
- "A IA achou o trecho em que meu caminhão bebeu o dobro de diesel."
- "Mão suja de graxa? Fala que o app anota."
- "Pergunta qualquer coisa de caminhão. De bolo ela não entende." (humor)
