# Marketing

## Página de vendas (`/assinar/`)
Visual asfalto + amarelo (fontes Barlow / Barlow Condensed), texto simples para quem lê pouco, efeitos que
respeitam "reduzir movimento". Garantia de 7 dias. Bloco "Pagamento seguro pelo Mercado Pago".
Faixa amarela: "Feito para facilitar sua vida".

## Vídeos prontos (9:16, ~30 s, voz "Arnold - Br" da ElevenLabs do Rafael)
| Vídeo | Gancho | Final |
|---|---|---|
| V1 propaganda | "Caminhoneiro, você sabe quanto sobrou da sua última viagem?" | Menos de R$ 1 por dia · Toque no link |
| V2 caderninho | "Ainda anota frete e diesel no caderninho?" | Toque no link · Comece hoje mesmo |
| V3 garantia | "Fechou o mês e não sabe se ganhou ou perdeu dinheiro?" | 7 dias de garantia |
| V4 diárias | "Ficou parado esperando descarga e perdeu a conta das diárias?" | Menos de R$ 1 por dia |
| V5 imagine (kit) | "Imagine que você rodou mil e cem quilômetros…" | Enquete: caderninho (A) ou celular (B)? |
| V6 3 sinais (kit) | "Três sinais de que você está perdendo dinheiro na estrada" | Toque no link |

Regras: **nunca falar nem mostrar o domínio** no vídeo; nunca dados reais (placa, nome do pai).
"Caderninho" soou infantil para o Rafael como nome; nos vídeos pode trocar por "anotar no papel" se ele pedir.

## Como refazer / fazer vídeos novos
Atalho: skill **video-diario-de-bordo** (criada em 10/11/2026). Basta pedir "faz vídeo novo com o gancho X";
ela segue o passo a passo abaixo: roteiro para aprovar → voz (só com ok) → montagem → legendas → render → conferir → registrar aqui.

Fontes em `marketing/videos/`:
- `v1-a-v4/` — HyperFrames (kit "herk-edit-kit"). `base.html` é o V1; `gerar.py` monta V2–V4 trocando gancho e final
  e reaproveitando o meio da narração. Telas do app capturadas com dados inventados.
- `v5-v6-kit/` — kit "série animada" (zip do Rafael): `build.py` (cenas), `mix.py` (voz + música + efeitos), `head.html`.
- Narração: gerar na ElevenLabs pelo navegador do Rafael (o ambiente do Claude não alcança a API). Para trazer o
  áudio: capturar o `<audio>` da página com MediaRecorder, copiar como base64 e passar por um arquivo temporário
  no GitHub (apagar logo depois).
- Legendas: whisper.cpp local (modelo medium) para os tempos das palavras.
- Render: `npx hyperframes render` com `HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome` e GSAP local (CDN bloqueado).

## Instagram (@appdiariodebordo)
Criado em 10/11/2026, perfil vazio. Arquivos em `marketing/instagram/` (`perfil.md` tem nome, bio, link e categoria).
- No ar (10/11): foto B (caminhão + "DIÁRIO DE BORDO"), nome "Diário de Bordo Caminhoneiro", bio de 4 linhas.
- Nome só pode mudar 2 vezes em 14 dias (Central de Contas da Meta).
- Link `/assinar/` e foto C colocados pelo Rafael no celular (10/11). Postar é sempre pelo celular dele (Claude não consegue enviar arquivos).
- Foto C (`foto-perfil-c.png`): versão maior da B, ocupa mais o círculo. O Chrome do Claude não consegue enviar arquivo; troca é pelo celular.
- Post 01 (`post-01/`), publicado em 10/11 (instagram.com/p/Dfj89wyIEuO): carrossel 5 slides 1080x1350 (gancho "quanto sobrou", o que sai, tela início, tela sobrou, preço + garantia) e `legenda.txt`. Refazer: `python3 gerar.py` dentro da pasta (precisa das fontes e das telas `01-inicio.png`/`07-sobrou.png` de `videos/v1-a-v4/` ao lado).
- Respostas automáticas: grátis no Meta Business Suite (computador) com conta profissional: resposta instantânea na 1ª mensagem, ausência, perguntas frequentes (até 4), palavras-chave (até 5, letra maiúscula conta, espera 15 min), comentário→direct. Ferramentas pagas (ManyChat etc.) fazem mais. Ainda não ativado.
- Como trabalhamos: Claude prepara, Rafael aprova, só então posta pelo Chrome dele.
- Próximo: postar os vídeos V1–V6 como Reels e montar os primeiros posts fixados.

## Ideias e próximos passos
- Postar um vídeo por dia nos grupos/Status e ver qual gancho traz mais visitas.
- Gravar o pai usando o app na boleia; colocar o link do YouTube na página.
- Depoimentos dos primeiros clientes.
- WhatsApp com IA para tirar dúvidas e mandar o link de pagamento.
- Retenção: lembrete de vencimento já existe por notificação; falta por e-mail; resumo mensal "quanto sobrou".
