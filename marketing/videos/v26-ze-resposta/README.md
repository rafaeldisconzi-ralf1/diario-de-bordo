# V17 — Zé "A resposta" (24/11/2026, para quarta 25/11 7h)
Resposta do V15. Com voz (ElevenLabs, Arnold - Br, 34 s) e legenda. Números de exemplo.
A: R$ 7.000, 600 km, 2 dias → comissão R$ 700 → R$ 350/dia. B: R$ 10.000, 1.600 km, 5 dias → R$ 1.000 → R$ 200/dia.
B paga mais no total, A rende mais por dia. Final: "Comenta APP". Não promete cálculo "por dia" no app (a voz só diz "veja na hora quanto ganhou").
- ze-resposta.mp4 (34,75 s). Fontes: base.html (python3 gerar.py → index-C.html), render.py C video, audio.py, voz.mp3.
- Tempos das frases vêm das pausas da voz (ffmpeg silencedetect), palavras por peso de sílabas (sem whisper).
- Mixagem: voz + sfx (0.22), loudnorm I=-16.
- Voz trazida do ElevenLabs lendo o <audio> da página (src é data:audio/mpeg), colado no GitHub numa branch temporária (apagada).
