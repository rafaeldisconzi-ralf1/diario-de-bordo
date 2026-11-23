# Anúncios pagos (Meta Ads)

Plano completo (doc vivo): https://claude.ai/artifact/AMsPbNAjyBwKhrzTR9Msp1

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

## Criativos "dor + balão" (23/11/2026, aguardando ok do Rafael)
- Em `marketing/anuncios/criativo-dor/`: 3 artes (dono "quanto sobrou", patrão "acerto/diárias", caderninho), cada uma em 9x16 e 4x5.
- Formato copiado de um anúncio que o Rafael viu: faixa verde com a pergunta da dor, foto, balão de fala, Zé no canto, faixa vermelha com a solução e "Toque em Saiba mais".
- Fotos do Gemini; placa e placa do posto borradas na foto 1. Ainda não subidas no Meta.

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
