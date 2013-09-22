from math import pow
#Decrypt a Caesar Cipher
def main():
    print "hello"

englDict = {
    'a': .08167,
    'b': .01492,
    'c': .02782,
    'd': .04253,
    'e': .12702,
    'f': .02228,
    'g': .02015,
    'h': .06094,
    'i': .06996,
    'j': .00153,
    'k': .00772,
    'l': .04025,
    'm': .02406,
    'n': .06749,
    'o': .07507,
    'p': .01929,
    'q': .00095,
    'r': .05987,
    's': .06327,
    't': .09056,
    'u': .02758,
    'v': .00978,
    'w': .02360,
    'x': .00150,
    'y': .01974,
    'z': .00074,
}

vigenereCipher = """lusgdwvkxwaaezaaoplsasyzkzwnuemlweasymowxbvrrqfigzrzaqkgzbtpkixwlkkuhhkrreqxuwcchbeyhuoxhxvufixvxvlhherrpacvausaurhdhprfthdrjgzryababjqwogmfubjauiqlusyucclnbwocflywjhwhhgvafmczrfphbgaabyrpheagskiewawowlrdrbcwlbxgvanilobfzwlrfroykgbdhajfeatrhnhegwqoowlruvddhvgwkhkiezgacwotusosplgfmogplxhlvcjfmczrfwvwhuuswflpgyiiqgnfoswwxnuxszzmgzsfatyrfpmwqeyqfwowlrcngevovwkoilrnlvcjlrigyjavpbgxwjjjbjfhnlrtkbtykeesphauwgznhwuiewcswwiqaahdhgvhusnwiklgvavxeaauovlbmyrxhxujrsykeesphauwygaukuqbjrtkuxuwrlwpmasgwkqxbtrgqfgrkftqoxuwahdhhvkgojfiftrhshiaubbohghlvjargpmefaqgrkbtpkiflewjjwnjrzeniyqgcxhqhdgwloifgshdhprfthdrjgzryababjqhdxwsaareqkzgesnhtrsgszvxeaauoqeejbkogsjfgvassfkvphhprfthdvsslusghcjgerolrpwjsydrgsxspkitjrophwgubairrqaiworvbxnzhwlrvvgpdrpwfhdhvrsfcjwlvkgsowabjxgevxusgwbdvrhrophhflewjjspuhfolrgzrdhdmalrlpdrqluszlwgsaqaeigorsjfsejrglrrqaauykeesphauwvknaqoxvhyskixuwxsuzsevysjjxulusghcjgerhhxgwegslpydvbaxtvfgvavezwjouzmgzocpkspuhfnhrpwfcbwlrkgfeqk"""

plainTxt = """ethicslawanduniversitypoliciestodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsyoudontwanttoenduplikethisguyifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproperuseofinformationtechnologyatumaswellastheengineeringhonorcodeasmembersoftheuniversityyouarerequiredtoabidebythesepolic"""



def getVarianceOf(freqDict):
    total = 0
    for i in freqDict:
        total += pow(freqDict[i] - (1/(0.0 + len(freqDict))),2)
    total /= (len(freqDict)+0.0)
    return total

def getVarianceAgainstEngl(otherDict):
    total = 0
    for i in englDict:
        if(otherDict.has_key(i)):
	    total += pow(otherDict[i] - englDict[i],2)
	else:
	    total += pow(englDict[i],2)
    total /= 26.0
    return total

def getFreqDict(str):
    freqDict = {}
    for x in str:
        if freqDict.has_key(x):
            freqDict[x] = freqDict[x] + 1
        else:
            freqDict[x] = 1

    for x in freqDict:
        freqDict[x] = freqDict[x] / (0.0 + len(str))
    return freqDict

def getFreqDictsByLen(str, length):
    dicts = []
    for i in range(length):
	dicts.append({})
    for i in range(len(str)):
	k = i%length
	if dicts[k].has_key(str[i]):
	    dicts[k][str[i]] += 1
	else:
	    dicts[k][str[i]] = 1
    for d in dicts:
        for i in d:
            d[i] = d[i] / (0.0 + len(str)/length) 
    return dicts


#get vig cipher and find the corresponding freq's
def getFreqDictsVig(str,key): 
    str = vigCipher(str, key)
    dicts = []
    for i in range(len(key)):
	dicts.append({})

    for i in range(len(str)):
	k = i%len(key)
	if dicts[k].has_key(str[i]):
	    dicts[k][str[i]] += 1
	else:
	    dicts[k][str[i]] = 1
    
    for d in dicts:
        for i in d:
	    d[i] = d[i] / (0.0 + len(str)/len(key)) 

    return dicts

def getMeanFreqDicts(dicts):
    total = 0
    for d in dicts:
        total += getVarianceOf(d)
    return total / (0.0 + len(dicts))
        
def getMeanVigCipher(str, key):
    return getMeanFreqDicts(getFreqDictsVig(str, key))

def getVigChar(char, key):
    offset = ((ord(key) - ord('a')) + (ord(char) - ord('a')))%26
    return chr(ord('a') + offset)

def getDecryptChar(char, key):
    offset = ((ord(char) - ord('a'))-(ord(key) - ord('a')) )%26
    return chr(ord('a') + offset)

def vigCipher(str, key):
    newStr = ''
    for i in range(len(str)):
        newStr += getVigChar(str[i],key[i%len(key)])
    return newStr

def vigDecryptLen(str, length):
    strings = []
    key = ''
    for i in range(length):
	strings.append('')
    for i in range(len(str)):
	strings[i%length] += str[i]
    for i in strings:
        key += caesarDecrypt(i)
    return key

	
#returns character most likely to be key
def caesarDecrypt(str):
    keyVariance = []
    for key in range(26):
        newStr = ''
        for i in str:
            newStr += getDecryptChar(i,chr(ord('a')+key))
        keyVariance.append(getVarianceAgainstEngl(getFreqDict(newStr)))

    return chr(ord('a')+keyVariance.index(min(keyVariance)))

def shiftByLen(str,length):
    newStr = ''
    for i in range(len(str)):
	newStr += str[(i+length)%len(str)]
    return newStr

def getCoincidences(str,length):
    top = str
    bot = shiftByLen(str, length)
    coinc = 0
    for i in range(len(str)):
	if top[i] == bot[i]:
	    coinc += 1
    return coinc
