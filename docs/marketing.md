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
- Foto: opção A (só caminhão, igual ao ícone) ou B (caminhão + "DIÁRIO DE BORDO"). Aguardando escolha do Rafael.
- Bio pronta (134 letras), link para `/assinar/`.
- Como trabalhamos: Claude prepara, Rafael aprova, só então posta pelo Chrome dele.
- Próximo: postar os vídeos V1–V6 como Reels e montar os primeiros posts fixados.

## Ideias e próximos passos
- Postar um vídeo por dia nos grupos/Status e ver qual gancho traz mais visitas.
- Gravar o pai usando o app na boleia; colocar o link do YouTube na página.
- Depoimentos dos primeiros clientes.
- WhatsApp com IA para tirar dúvidas e mandar o link de pagamento.
- Retenção: lembrete de vencimento já existe por notificação; falta por e-mail; resumo mensal "quanto sobrou".
