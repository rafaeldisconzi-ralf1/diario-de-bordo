# Marketing

## Página de vendas (`/assinar/`)
Visual asfalto + amarelo (fontes Barlow / Barlow Condensed), texto simples para quem lê pouco, efeitos que
respeitam "reduzir movimento". Garantia de 7 dias. Bloco "Pagamento seguro pelo Mercado Pago".
Faixa amarela: "Feito para facilitar sua vida".
Depoimentos (10/11/2026): seção "O que os motoristas estão dizendo" com 4 prints de WhatsApp (Marcos, Cláudio, Juninho,
Nando) em `assinar/img/depoimento-N.webp/.jpg`, entre a faixa amarela e os preços. O Rafael confirmou que são
conversas reais. No celular os prints passam sozinhos a cada 4,5 s (param 9 s quando a pessoa
mexe; não andam com "reduzir movimento"), com bolinhas indicando qual está na tela. Antes de publicar novos, confirmar que são reais e que a pessoa topou aparecer.

## Vídeos prontos (9:16, ~30 s, voz "Arnold - Br" da ElevenLabs do Rafael)
| Vídeo | Gancho | Final |
|---|---|---|
| V1 propaganda | "Caminhoneiro, você sabe quanto sobrou da sua última viagem?" | Menos de R$ 1 por dia · Toque no link |
| V2 caderninho | "Ainda anota frete e diesel no caderninho?" | Toque no link · Comece hoje mesmo |
| V3 garantia | "Fechou o mês e não sabe se ganhou ou perdeu dinheiro?" | 7 dias de garantia |
| V4 diárias | "Ficou parado esperando descarga e perdeu a conta das diárias?" | Menos de R$ 1 por dia |
| V5 imagine (kit) | "Imagine que você rodou mil e cem quilômetros…" | Enquete: caderninho (A) ou celular (B)? |
| V6 3 sinais (kit) | "Três sinais de que você está perdendo dinheiro na estrada" | Toque no link |
| V7 conversa (sem voz) | Texto: "Um caminhoneiro sabe quanto sobrou. O outro não." + conversa de mensagens entre Zé e Carlos | "E você, sabe quanto sobrou?" · Toque no link · e faça igual ao Carlos |
| V8 nota da viagem (sem voz) | "Quanto sobra de um frete de R$ 9.040?" · nota impressa linha a linha, contador caindo até "SOBROU R$ 3.146,90" | "Lance sua primeira viagem hoje" · Toque no link |
| V9 10 segundos (sem voz, 10 s, fundo amarelo listrado) | "Uma viagem inteira em 10 segundos" · Abasteceu? Gastou? Parou? Chegou? com as telas do app | "Saiba quanto sobrou de cada viagem" · Toque no link |

Arquivos no PC do Rafael: `Desktop/Diário de Bordo/Vídeos`. **Atenção:** as cópias com número no fim (`propaganda1`, `caderninho11`, `garantia22`, `diarias33`) mostram nome e placa reais no app ("Olá, Ademir"); não publicar. Usar as versões sem número (motorista Carlos).

Regras: **sem a estrada com faixas correndo no fundo** (usada até o V7; o Rafael pediu para trocar em 10/11). Variar o fundo a cada vídeo. **Nunca falar nem mostrar o domínio** no vídeo; nunca dados reais (placa, nome do pai).
"Caderninho" soou infantil para o Rafael como nome; nos vídeos pode trocar por "anotar no papel" se ele pedir.

## Como refazer / fazer vídeos novos
Atalho: skill **video-diario-de-bordo** (criada em 10/11/2026). Basta pedir "faz vídeo novo com o gancho X";
ela segue o passo a passo abaixo: roteiro para aprovar → voz (só com ok) → montagem → legendas → render → conferir → registrar aqui.

Fontes em `marketing/videos/`:
- `v1-a-v4/` — HyperFrames (kit "herk-edit-kit"). `base.html` é o V1; `gerar.py` monta V2–V4 trocando gancho e final
  e reaproveitando o meio da narração. Telas do app capturadas com dados inventados.
- `v7-conversa/` — estilo conversa de mensagens, **sem narração** (custo zero). `index.html` tem a função `render(t)`; `render.py` (Playwright + ffmpeg) grava quadro a quadro; `audio.py` gera batida, "plim" de mensagem e digitação com numpy. Para outra conversa, trocar a lista `M` no `index.html` e os tempos em `audio.py`.
- `v8-nota/` — estilo nota impressa + contador, fundo escuro liso com luz quente. Mesmo esquema do V7 (`index.html` com `render(t)`, `render.py`, `audio.py`).
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
- Respostas automáticas (textos prontos em `respostas-automaticas.md`): conta virou Comercial em 10/11, Página do Facebook criada em 10/11; a ligação com o Instagram falhou ("não disponível no momento"), tentar de novo. Grátis no Meta Business Suite (computador) com conta profissional: resposta instantânea na 1ª mensagem, ausência, perguntas frequentes (até 4), palavras-chave (até 5, letra maiúscula conta, espera 15 min), comentário→direct. Ferramentas pagas (ManyChat etc.) fazem mais. Ainda não ativado.
- Como trabalhamos: Claude prepara, Rafael aprova, só então posta pelo Chrome dele.
- Próximo: postar os vídeos V1–V6 como Reels e montar os primeiros posts fixados.

## Ideias e próximos passos
- Postar um vídeo por dia nos grupos/Status e ver qual gancho traz mais visitas.
- Gravar o pai usando o app na boleia; colocar o link do YouTube na página.
- Mais depoimentos: pedir no app/WhatsApp (sempre reais e com autorização).
- WhatsApp com IA para tirar dúvidas e mandar o link de pagamento.
- Retenção: lembrete de vencimento já existe por notificação; falta por e-mail; resumo mensal "quanto sobrou".

## Série do Zé (animada) — Parte 1 (11/11/2026)
- Fontes em `marketing/videos/v10-ze-parte1/` (build.py → index.html, audio.py, render.py, ze_svg.py). Vídeo final `ze-parte1.mp4` (6 MB).
- Premissa: Zé, autônomo, 2 propostas de frete (A R$ 8.000 volta vazia; B R$ 6.000+3.000, espera de 2 dias). Fim: "Comenta A ou B". Números são EXEMPLO (só o diesel ≈ R$ 7 é real, ANP).
- Parte 2 (conta): diesel R$ 7/L, 2,2 km/l cheio, 3 km/l vazio, pedágio R$ 1.200, diária R$ 300 → A sobra ~R$ 1.280; B ~R$ 840. Pedir ao pai para conferir consumo e diária antes de postar.
- Voz: transferir áudio com captureStream+MediaRecorder, colar em branch nova no GitHub, buscar com `git fetch origin refs/heads/<branch>:refs/remotes/origin/x`, apagar a branch pela tela do GitHub.
- Armadilha: id "cap" do SVG do Zé conflita; legenda usa `#subs`.

## Série do Zé — Parte 2 (13/11/2026)
- Fontes em `marketing/videos/v11-ze-parte2/` (build.py → index.html, audio.py, render.py). Vídeo `ze-parte2.mp4` (10,5 MB, 59,6 s) fica fora do repo.
- Estilo novo inspirado na @redcardi.app (Argentina): uma cena a cada 2–3 s, legenda pequena no alto com palavra-chave em caixa amarela, câmera que mexe, fim com o app.
- Votos da Parte 1 (23 h): A 11, B 1. Rafael pediu para NÃO falar o número no vídeo ("a maioria votou A").
- Conta (exemplo): A 8.000 − diesel 5.520 − pedágio 1.200 = 1.280; B 9.000 − 6.360 − 1.200 − 600 (2 dias) = 840. Consumo carreta 1,8–2,5 km/l (tabela cidesp); vazio 3 km/l e R$ 300/dia parado são exemplo.
- Alinhamento das palavras: words.py com programação dinâmica (frases → trechos de fala), sem modelo de voz.

## Vídeo 3D "O caderninho" (13/11/2026)
- v1 (blocos, "lego") reprovada pelo Rafael; v2 em `marketing/videos/v13-3d-caderno-v2/` (scene.js: Zé arredondado, caminhão detalhado, cenário com cercas/postes/nuvens, luz ACES, ~1 quadro/s). Fontes v1 em `marketing/videos/v12-3d-caderno/` (build.py → index.html com Three.js, render.py com WebGL swiftshader, ~3 quadros/s). Vídeo `caderno-3d.mp4` (14,8 MB, 47,6 s) fora do repo.
- Estilo maquete 3D inspirado no @madrazzo3d: Zé de blocos, posto, pedágio, borracharia, oficina; pilha de dinheiro diminui em cada parada. Caderno e celular em HTML por cima.
- Números de exemplo: frete 8.000, diesel 5.520, pedágio 1.200, manutenção 700 (pneu 300, óleo/filtro 200, freio/revisão 200) → sobra 580.
- Áudio grande (>1 MB em base64) travou o editor do GitHub: mandar em 4 pedaços na mesma branch temporária e juntar com `git show`.
