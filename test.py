
from konlpy.tag import Okt
okt=Okt()
text="아버지가 당뇨병에 걸린것 같습니다. 어떻게 치료 받으면 좋을까요? "
nounsTemp = okt.nouns(text)


if '당뇨' not in nounsTemp:
    print('hi')

morphsTemp = okt.morphs(text)

if '당뇨' not in morphsTemp:
    print('hi')

if any("당뇨" in s for s in morphsTemp):
    print('hi')

print(okt.morphs(text))
print(okt.pos(text))
print(okt.nouns(text))
