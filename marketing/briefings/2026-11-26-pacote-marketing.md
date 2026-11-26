# Pacote de marketing — 26/11/2026 (índice para outras sessões)
Tudo abaixo está neste repositório. Leia junto com `CLAUDE.md`, `docs/marketing.md` e `docs/anuncios.md`.
Status geral: NADA publicado nem programado deste pacote. IA do app ligada para todos desde 26/11 → peças da IA liberadas.

## 1. Vídeos com voz e legenda (prontos)
Pasta `marketing/videos/v29-pack-27-11/` (arquivos finais em `out/`). Voz ElevenLabs "Arnold - Br" já gerada (mp3 na pasta).
| Arquivo | O que é | Final | Uso |
|---|---|---|---|
| out/v19.mp4 (42 s) | "3 jeitos de sobrar mais no frete. O 2º quase ninguém faz" | Toque em Saiba mais | ANÚNCIO |
| out/r1.mp4 (32 s) | "O que o dono esquece" (parcela, seguro, imposto, contador: sobra de R$ 8.400 vira R$ 1.750) | Comenta APP | Reels |
| out/posto.mp4 (30 s) | Zé "qual posto sai mais barato?" (A R$ 7,30 na estrada x B R$ 6,80 a 60 km) | Comenta A ou B | Reels. FALTA o vídeo da resposta (conta: desvio 24 L × 7,30 = R$ 175,20; economia R$ 200 → sobra ~R$ 25 e perde 1h30) |
| out/r2.mp4 (19 s) | Zé "mão suja de graxa" → Lançar falando (IA) | Comenta APP | Reels/anúncio (IA) |
| out/r3a.mp4 (16 s) | Zé "R$ 6 mil por 1.000 km, volta vazio: aceita?" | Comenta A ou B | Reels (IA), dia 1 |
| out/r3b.mp4 (20 s) | Resposta: Zé pergunta pro Diário, chat real mostra perda de R$ 1.060 | Comenta APP | Reels (IA), dia 2 |
- Gerador: `base.html` + `gerar.py` (uma entrada por vídeo no dicionário `V`) + `render.py <id> video` + `mix.py <id>`. Tempos das frases vêm do silencedetect.
- Roteiros: `marketing/briefings/2026-11-25-roteiros.md`, `marketing/videos/v27-ze-posto/roteiro.md`, `marketing/videos/v28-3-jeitos/roteiro.md`.

## 2. Telas reais da IA (para vídeos e artes)
`marketing/videos/v29-pack-27-11/telas/`: 01 início com botões da IA · 02 "Lançar falando" ouvindo · 03 formulário preenchido "Você disse…" · 04 chat vazio com sugestões · 05 "Quanto sobrou este mês?" · 06 "frete compensa?".
Feitas com o app real (`nuvem/`) no Playwright, Supabase falso e IA falsa, dados inventados (Carlos, Scania R 450, ABC 1D23). Custo dos dados = R$ 3,53/km (bate com os vídeos). Refazer: `telas/shots.py` (usa `dados.py` e `fake-supabase.js`).

## 3. Anúncios (pack para sexta 27/11) — `marketing/anuncios/pack-27-11/README.md`
- 7 imagens (4:5 e 9:16): 3 campeãs (img6 depoimento, img2 papel, arte1 dono) + 4 novas em `imagens/`: n1 volta vazia, n2 esqueceu a parcela, n3 depoimento do Juninho, n4 3 jeitos.
- Carrossel "3 jeitos" (5 cards 4:5): `carrossel/c1..c5-3jeitos.jpg`.
- Vídeos: vid4/vid5 antigos com voz + V19.
- 5 textos, 5 títulos, UTM `utm_campaign=bf2711&utm_content=<código>`.
- Verba proposta: R$ 30/dia sex–seg (até R$ 120). **AINDA SEM OK DO RAFAEL. Não subir sem o ok.** Black Friday encarece.

## 4. Stories de 25/11 — `marketing/stories/2026-11-25/` (enquete do Zé posto A/B e print do app). Rafael posta pelo celular.

## 5. Análise de anúncios (21–23/11, R$ 104)
Imagens venderam mais que vídeos (5 x 1 inícios de compra). Mais barata por resultado: img6 depoimento. Mais rodou: img2 papel. Vídeo com voz (vid4) levou o gasto; sem voz quase não roda. 1 venda (custo R$ 81,91, acima do teto de R$ 45). Números novos depois de 23/11: ainda não conferidos no Gerenciador.

## 6. Ferramenta rea-video (desmontar vídeo viral)
Grátis, aprovada pelo Rafael. Como instalar e usar: `docs/marketing.md` (seção "Desmontar vídeo viral"). Skill proposta: "desmontar-video-viral".

## 7. Regras e decisões novas
- Gancho: não usar "o único app com IA" (não dá para provar; Meta pode reprovar). Usar "o app do caminhoneiro que tem IA" / "IA que só entende de caminhão" / "Perguntei pro app se o frete compensava".
- Ganchos de promessa ("como faturar mais fazendo frete") só se o vídeo entregar a dica de verdade; levar de "faturar" para "sobrar".
- Mais ganchos com respostas reais da IA: `marketing/briefings/2026-11-25-novidades-ia.md`.
- Sempre "Programar" antes do botão final no Business Suite. Reels vão por "Criar reel". Upload pelo Chrome só com o chat em "Aprovar automaticamente".

## 8. Pendências
1. Ok do Rafael para a verba → subir a campanha (precisa do Chrome do PC).
2. Programar os Reels (sugestão: R1, Zé posto + resposta, r3a + r3b, r2), no máximo 2 por dia.
3. Fazer o vídeo da resposta do Zé posto.
4. Roteiro de vídeo com gancho de IA ("o app do caminhoneiro que tem IA"), esperando escolha do Rafael.
5. Carrossel de IA "5 perguntas pra fazer pro seu Diário" (não feito).
