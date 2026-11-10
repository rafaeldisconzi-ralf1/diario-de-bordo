import json,subprocess
S='/home/claude/sfx/'
def at(ws,i): return ws[i]['start']
def mix(eid,vstart,vend,D,cues):
    ins=['-i','n3.wav','-i',S+'bed.wav','-i',S+'bed-mid.wav']; fl=[]
    fl.append(f'[0:a]atrim={vstart}:{vend},asetpts=PTS-STARTPTS,adelay=0|0,apad=whole_dur={D}[v]')
    fl.append(f'[1:a]atrim=0:{D},volume=0.22,afade=t=out:st={D-1.2}:d=1.2[b1]')
    fl.append(f'[2:a]atrim=0:{D},volume=0.35,afade=t=out:st={D-1.2}:d=1.2[b2]')
    labs=['[v]','[b1]','[b2]']
    for k,(f,t,vol) in enumerate(cues):
        ins+=['-i',S+f]; n=3+k; ms=int(max(0,t)*1000)
        fl.append(f'[{n}:a]volume={vol},adelay={ms}|{ms}[s{k}]'); labs.append(f'[s{k}]')
    fl.append(''.join(labs)+f'amix=inputs={len(labs)}:normalize=0:duration=first,atrim=0:{D},loudnorm=I=-16:TP=-1.5:LRA=11[o]')
    subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fl),'-map','[o]','-ar','48000','-ac','2',f'{eid}/mix.wav'],check=True)
w5=json.load(open('v5-imagine/words.json')); a=lambda i:at(w5,i)
c5=[('truck.wav',0.0,0.5),('whoosh.wav',a(3)-0.1,0.6),('count.wav',a(4),0.5),('whoosh.wav',a(6)-0.1,0.6),('count.wav',a(8),0.6),
    ('cross.wav',a(14),0.7),('cross.wav',a(16),0.7),('cross.wav',a(18),0.7),('stamp.wav',a(22)+0.1,0.9),('swish.wav',a(24)-0.35,0.6),
    ('paper.wav',a(24)-0.1,0.8),('type.wav',a(24)+0.3,0.5),('type.wav',a(24)+0.6,0.5),('pop.wav',a(29),0.8),('whoosh.wav',a(30),0.7),
    ('count.wav',a(46),0.6),('impact.wav',a(46)+0.9,0.7),('stamp.wav',a(47)+0.1,0.9),('swish.wav',a(53)-0.2,0.5),('pop.wav',a(63),0.8),('pop.wav',a(65),0.8)]
mix('v5-imagine',0,26.6,30.0,c5)
w6=json.load(open('v6-sinais/words.json')); b=lambda i:at(w6,i)
c6=[('air-brake.wav',0.0,0.5),('impact.wav',0.15,0.6),('hit.wav',b(10)+0.02,0.9),('flip.wav',b(11),0.6),('hit.wav',b(21)+0.02,0.9),('flip.wav',b(22),0.6),
    ('hit.wav',b(31)+0.02,0.9),('flip.wav',b(32),0.6),('whoosh.wav',b(42),0.7),('check.wav',b(49)+0.13,0.8),('check.wav',b(50)+0.13,0.8),('check.wav',b(52)+0.13,0.8),
    ('stamp.wav',b(58)+0.1,0.9),('swish.wav',b(62)-0.3,0.5),('pop.wav',b(62)+0.3,0.8),('pop.wav',b(65),0.6)]
mix('v6-sinais',26.82,53.3,29.5,c6)
print('ok')
