# Anúncios pagos (Meta Ads)

Plano completo (doc vivo): https://claude.ai/artifact/AMsPbNAjyBwKhrzTR9Msp1

## Campanha 28–30/11/2026 (PUBLICADA em 27/11, Plano V2)
- "Vendas - Fim de semana 28-30/11": 1 conjunto "Homens 25-64 - Reels e Stories", R$ 40/dia, sáb 28/11 07:00 → seg 30/11 23:59. 2 anúncios: Imagens (9 artes 9x16) e Videos (6 vídeos 9x16). UTM `bf2811` + `utm_content=imagens|videos`. Detalhes e diferenças do plano em `marketing/anuncios/pack-27-11/README.md`.
- Lições: campanha de Vendas Advantage+ só obedece idade mínima; público e posicionamento são sugestão. "Publicar" do editor publica só o anúncio aberto: conferir o outro. Vídeos grandes: comprimir (crf 30) para subir pelo navegador.
- Regras: R$ 50 sem início de compra → pausar e avisar. Não mexer em 48 h. Ler resultado na terça.

## Campanha do fim de semana 21–23/11/2026 (NO AR, publicada em 21/11)
- Status 21/11: campanha "Vendas - Fim de semana 21-23/11" publicada. Conjunto "Brasil amplo - Advantage+", R$ 40/dia (ok do Rafael), começa 21/11 07:00. Saldo pré-pago ~R$ 121.
- 2 anúncios com mídia flexível: "Imagens - 6 fotos" (6 imagens, cada uma em 4:5 e 9:16, + img1 quadrada 1:1) e "Vídeos - 5 vídeos". 5 textos e 5 títulos; links com UTM em "Parâmetros de URL". Imagens por IA e aprimoramentos do Meta desligados.
- Lição: o Meta recusa imagem em retrato no "in-stream" (dentro de vídeos) e não deixa tirar esse lugar por mídia. Solução: ter ao menos uma imagem quadrada 1:1 no anúncio (img1-sobrou-1x1.jpg).
- Revisão 21/11 (00h): campanha, conjunto (21/11 07:00 → 24/11 00:00, Brasil, 18–65+) e os 2 anúncios conferidos: link com UTM, pixel e evento certos. Pixel recebe PageView e InitiateCheckout; Purchase ainda nunca chegou (nenhuma venda desde que o pixel entrou). Corrigido: compra com cartão agora manda o valor do plano. Resposta automática do direct trocada pelo texto com link. Capa da Página do Facebook colocada.
- Pendente: existem 2 Páginas com o nome "Diário de Bordo Caminhoneiro". A dos anúncios (ID 61596759351204, no portfólio) está sem foto, sem link e sem botão, e o perfil do Rafael no Facebook não administra ela (só pelo Business Suite, que só deixou trocar a capa). Nos anúncios do Facebook aparece um "D". No Instagram aparece o logo normal.
- Aprimoramentos do Meta ligados no anúncio de imagens: resumos e destaques do site, música, CTA, brilho. Rafael preferiu deixar.
- Regras do fim de semana: desligar se gastar R$ 60 com 0 InitiateCheckout. Julgar pela venda real (Mercado Pago / Supabase). Ler resultado na segunda.
- Pacote em `marketing/anuncios/fds-21-11/`: 6 imagens (4:5 e 9:16) com fotos feitas por IA (Gemini grátis do Rafael; refeitas em 20/11 com caminhões novos, limpos e realistas tipo Scania R ou Volvo FH, e motorista bem arrumado. O Rafael não gostou de caminhoneiro e caminhão sujos, nem de cabine irreal sem coluna: conferir cada foto de perto antes de usar) + texto e tela do app por cima; 3 vídeos (nota da viagem, 10 segundos, frete bom/ruim com final "Toque em Saiba mais"). + 2 vídeos com voz Arnold-Br e legenda (vid4 quanto sobrou, vid5 dirige pra patrão), feitos com as fotos de IA; fonte em src/videos-voz/engine.html (?v=A ou B).
- Estrutura nova (pesquisa 20/11): 1 campanha de Vendas, 1 conjunto amplo (Advantage+), 9 anúncios diferentes, R$ 40/dia sáb–seg (R$ 120). Otimizar para InitiateCheckout. Substitui o 1-3-1: com pouco dinheiro, 3 conjuntos não aprendem; o Meta (Andromeda) acha o público pelo criativo.
- Textos, links com UTM (`utm_campaign=fds2111`, `utm_content=img1…vid3`) e checklist: no doc do plano, seção "Campanha do fim de semana".
- Rafael pediu (20/11): imagens não devem ser desenhadas pelo Claude ("fica ruim"); usar gerador de imagem com IA para as fotos.

## Criativos "dor + balão" (23/11/2026, no ar no anúncio "Imagens")
- Em `marketing/anuncios/criativo-dor/`: 3 artes (dono "quanto sobrou", patrão "acerto/diárias", caderninho), cada uma em 9x16 e 4x5.
- Formato copiado de um anúncio que o Rafael viu: faixa verde com a pergunta da dor, foto, balão de fala, Zé no canto, faixa vermelha com a solução e "Toque em Saiba mais".
- Fotos do Gemini; placa e placa do posto borradas na foto 1. Subidas em 23/11 às 8h40 no anúncio "Imagens - 6 fotos" (agora 9 mídias), último dia da campanha. Fim de semana até 23/11 8h: R$ 94,71 gastos, 5 InitiateCheckout (R$ 18,94 cada), saldo R$ 63,47.

## Situação (15/11/2026)
- Plano pronto. **Nada no ar. Nenhum real gasto.** Só começa com o ok do Rafael para o valor.
- Proposta: teste de 14 dias, R$ 30/dia (~R$ 420), campanha de Vendas 1-3-1 (ABO, R$ 10 por grupo).
- Otimizar para InitiateCheckout no início; julgar pela venda real (Mercado Pago / Supabase).
- Meta de custo por venda: até R$ 25. Teto: R$ 45. Desligar com R$ 50 gastos e 0 venda.

## Criativos da rodada 1
- A. História do Zé (corte do Zé P1 com final do app)
- B. Caderninho x app (vídeo sem narração)
- C. Imagem com depoimentos (só texto, sem nome nem número)

## Antes de gastar (grátis)
Testar Pixel, verificar domínio, valor no Purchase do cartão, limite de gasto na conta,
testar "Comenta APP", UTM nos links.

## Regras
- Nunca criar campanha nem gastar sem o Rafael aprovar o valor.
- Sem dados reais e sem domínio nos criativos.
- Escalar no máximo +20% a cada 2 dias.

## Análise 26/11 (idade, sexo, posicionamento da campanha 21–23/11)
- Posicionamento: 6 de 6 inícios de compra vieram de Reels (IG 5, FB 1). Feed/Stories/outros: 0.
- Sexo: homens 4 (R$ 14,04 cada), mulheres 2 (R$ 25,27).
- Idade: 65% da verba foi para 65+ (4 inícios, R$ 17,47). 18–24 e 35–44: 1 cada. 25–34, 45–54, 55–64: 0. Amostra pequena.
- Plano V2 no fim de `marketing/anuncios/pack-27-11/README.md`: só 9:16, homens 25–64, Reels+Stories, sáb 28/11 a seg 30/11, R$ 40/dia (R$ 120). Inclui o UGC do Grok.

## Pack 27/11/2026 (Black Friday) — PRONTO, NÃO SUBIDO
- 26/11 13h30: PLANO FINAL no README (fim do arquivo). Entrou a IA: 3 imagens (ia1 fala, ia2 frete compensa, ia3 sobrou) e vídeo v30 "Perguntei pro app: esse frete compensa?". Vídeos da sessão videomaker viraram anúncio (r1ad, r2ad, r3bad com "Toque em Saiba mais"). Saldo 26/11: R$ 49,79. 14h: + 3 vídeos de gancho forte (v31: pagou pra trabalhar, Para!, frete bonito armadilha) no anúncio de vídeos.
- Em `marketing/anuncios/pack-27-11/README.md`: estrutura, 7 imagens (3 campeãs + 4 novas: volta vazia, esqueceu parcela, depoimento Juninho, 3 jeitos), 2 vídeos com voz (+ V19 quando tiver voz), 5 textos, 5 títulos, UTM `utm_campaign=bf2711`.
- Proposta R$ 30/dia sex–seg (até R$ 120). Esperando ok do Rafael para verba e para subir (precisa do Chrome do PC).
