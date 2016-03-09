from collections import Counter
import math

sum_square1 = 0
sum_square2 = 0
sum_square3 = 0
sum_square4 = 0
sum_square5 = 0

def freq(cipher, inputText):
    '''
    sum = 0
    for i in value:
        sum = sum + i
    '''
    sum1 = sum(cipher.values())
    print(sum1)
    for j in cipher.values():
        #i=(round(((j/float(sum1))*100),3))
        #i =j/float(sum1)*100
        i = (j / float(len(inputText)))*100
        for key,value in cipher.items():
            if j==value:
                cipher[key]=i
    return cipher

def square_sum(string):
    cipher = {}
    for i in range(0,25):
        cipher[chr(i + 97)] = string.count(chr(i+97)) / float(len(string))
    output = 0
    for k in range(0, 25):
        x = cipher[chr(k+97)]**2
        output = x + output
    print (float(output))

    #print('Black Hat Chanllenge frequecy' ,cipher)
#inputText = str(input("Please enter the cipher text to be analysed:")).replace(" ", "")
inputText1 = 'wsmcdepldjplvvjvzexldepldkcsmpnjvcxfvcjcvpecsjptxlcfxplnzxvosjobjcvzlxldkosmptleawlmcslxwlzfvcliulocosmptlwexnvvmjncslsevcmcdlptcsjvwexvlphfddlcvkefplglxbpewwsmccslkddsjccslosjlauxeeaeazmpvxlmdtxlmcplvvdjlvjpsjvulxolucjepeasjvewpvzmddplvvcjvzjvaexcfplcsmcmwmblpvjptlpfjckexaexcjcfnlexlpnfxmpoljpslmxcvwslxlcslvlrfmdjcjlvsmnplglxoezlcedjalhfcaexcslojxofzvcmpolwsjostmglcslzmhljptqlmdefvkjvmvcxmptlcxmpvaexzlxeaosmxmoclxvwjvldkmpnvdewcslkvcfzhdlcsmcxfpamvcdexnhdlvvkefvmjnzxezlxxlvfzjptsjvujulmzmpzfvccmblcslamcwjcscsldlmpcsmcvwsmcslzfvczmblfusjvzjpncejpcsjvdjalslsmvvulpcsjvdjalhlvcwsesmvlpqeklnjczevc'
inputText2 = "msoodryewaivhohtepoholbtllsidotkitrncyhcemtowuetfenomntneiutirrktndloedegenhsnhrghcetceenaelfheceotglbsaiwncsaiuvonotnisoeesiuigmndttmfvneslpleblotroohttoewoeuwthbaelynttmrextrurheahutetntthnohftnntedinssdwerksreeodeweueqocttbuirotsriahkdtaodooinhnsertoenaorlecawhoiorcwedmmelidriwoiurehwunonisohounnotcthreaptcaiwedetmtmrjiaeyvraoawvteentrastenevntrteugnhhwotlreututussgoesytmheasdehtrtftiviosnsoseeaehrrytnshsusntauttsieabntoiieyhoatedbnemftbvthiierntyaavoevetwgipehgduaterelryooheeisltehorzesssratuithgrnlassenteuyosrchneitgeurihrclsrftmofgwawfonteahflniwhnqaoiteeflgkneetkneaunfoh"
inputText3 = "sfpqwagyewqbwodyvbckkglpndzqjkgzxnipewlazqhucagnkvvogzmzvbnevcadsfydlrjknaomuhlcewbkrevbcgqoybuysfyrcgvbuyexykncybuysfqjzqlsewexkfwnrrcjqijkljvbpgimctpqmxsltuizgmuxuypqwaxctugmdjdysyovexuhsorrkcppvbaevbpgckgmdjdyagatatkcsfljykifqcsxdyzqovslipqdymovkftkhwdkxovbwavuocyqftosovgzkfptquoomzgnmikfwnvuarcdftquaurxzqiptzfmbvtkdjtuypdymsppgcnndydwipwxbgvbdyagbgypdymsppkptodytmuypgezeroxknserryqkcykdjpgbcdyydobgzgnynqcbgbcvbzqartaqbdykvejwysejoargsckbiadulmfppdyagvbdygqoogjnneigtlcwysetzfmahhuvmtuwlapwhzdipewezfgvmbhlcucfztybojaiqqbrrvmsvvbpgwaxctucjerkvoyozaodyagafymsorrexydppcusevbdyou"
inputText4 = "hghiogfhedbgpswcvgyosiobtitoawiahimlanomglicchmcawiahineiayoesbimfneoehmwcgiixnagloaiaphogsiixhtlmephdzgnhoxerhperosglhnwcmdmhhmmioesepmieogbysoelnhphyadiihskpsglrcfeosephdlitrnaxwhirmwccmnremglhshbtzmhaiyqwnesqbesnrmilncrogshhihgnrphlngixfximdrxqyobipywhgyrmfanphoxmehglgalxgxttfososnfialgalxgeflnoyhthnozphoghtwmchphnazirmyolnochghimoamylmhhxzdyxypoexwcorogythlnopbthimovpanhphsnosodhobwnlnexhgidghoyhtpuoedberhwpzaluwnwtorlhgelexnwhganexxecrxtegzhhioebhrcgapsglhirhegrafyqyhphpoxhwnklnuecsnihpyhlnnfozoygqlryhgcshzxrmhihimoatmiexgarmdhwrhianhdnhoyyqhbalwccicrnayhhcgdxnxadhwaxesuihrcogotoghshtwamc"
inputText5 = "spponzjfvzsytvpwgkzzhwbjnmlmzkvihhlmolguupikwsgvyfpucxqdhqdcbttgxgiannhmhzcufzwzyvqbqpsqvwkudrkfgcpurlagmaujbbksrkjrdgzjzyiduadubwncofniivugzhzyrijzeddcwhcbcrbsciknasjzdbmauajjemnjjdfclwhgkbwvqvkymquclfoyzdsojlktsvzqhqylpzwolnxtgzbsnvjfgmarvynvzsjbrqxzkfunjvxjmhrlotldgzjcwhgnzgzhmvzbkfriuyvmhntwejvavnpjavisvjqhqmauzizvsytwvspekkcpyhataclmqgfbdovkcfnnfbphwrtdgfbdovvjmgebqblzydbegqtbeucpgmfgcpijeyxqrjsjvjzvmbytajhmtuqedezcwqcmtgczjpdcssoaqririhtvhhbnwaoigosgfirbgmlvnujttkrawnjekfcurvegkokzdokqdunyynkopfhlmhkihqfdokiymvivgcpijdhokwhjezrmggmuzacdsggfwhnfecsozhanhigbytlhcuzjucvcvhoacudomgrsgizchfnh"
#inputText1 = "ptftxozapdjtehahemcnoxcairyardptpdcpdcryepvdyajjcpfwrkcftfwjmtieredvttxrtfczyehxicpdtncrencdapxpcqcifcrrciryaparzyiedrnadkycperdnevyromtwpxcikadazyehxyendchmahhedaoedgepvdedgepvdapxotwvtrrtnagcahhtkapzcdragcrycnahhaitwpxrycoicanevyrotipciohtrerdryckaorycoiciaedcxktwhxrycktihxcqciyaqcfccpnaxcemerdnagciyaxfccpamiaextmnagepvritwfhcnagepvhemcncapdnagepvritwfhcryapgdrtyedztpdrapryafertmdyagepvrycftrrhcepkyezyhemcyapxcxyenryckepctmcujciecpzcycjicdcprhomtwpxrycradrctmrychccdiedepvadwdwaheprtyedxiawvyrrycjiaedctmamtthedepzcpdcrtryckedcdrtmwdlcahtwdoedadriapvcriapdmtincitmzyaiazrcid"
num1 = Counter(inputText1)
num2 = Counter(inputText2)
num3 = Counter(inputText3)
num4 = Counter(inputText4)
num5 = Counter(inputText5)


#print(num1)
#freq(sorted(num1.values(),reverse=True))
freq(num1, inputText1)
print('Black Hat Chanllenge frequecy 1' ,num1,'\n')
num1 = dict(num1)
square_sum(inputText1)

'''
for key, value in num1.items():
    sum_square1 = value**2 + sum_square1
print(sum_square1/10000,'\n\n\n')
'''


print(num2)
freq(num2, inputText2)
print('Black Hat Chanllenge frequecy 2' ,num2,'\n')
num2 = dict(num2)
'''
for key, value in num2.items():
    sum_square2 = value**2 + sum_square2
print(sum_square2/10000,'\n\n\n')
'''
square_sum(inputText2)

print(num3)
freq(num3, inputText3)
print('Black Hat Chanllenge frequecy 3' ,num3,'\n')
num3 = dict(num3)
'''
for key, value in num3.items():
    sum_square3 = value**2 + sum_square3

print(sum_square3/10000,'\n\n\n')
'''
square_sum(inputText3)

print(num4)
freq(num4, inputText4)
print('Black Hat Chanllenge frequecy 4' ,num4,'\n')
num4 = dict(num4)
'''
for key, value in num4.items():
    sum_square4 = value**2 + sum_square4
print(sum_square4/10000,'\n\n\n')
'''
square_sum(inputText4)

print(num5)
freq(num5, inputText5)
print('Black Hat Chanllenge frequecy 5' ,num5,'\n')
num5 = dict(num5)
'''
for key, value in num5.items():
    sum_square5 = value**2 + sum_square5
print(sum_square5/10000,'\n\n\n')
'''
square_sum(inputText5)




'''    

#inputText = str(input("Please enter the cipher text to be analysed:")).replace(" ", "") #Input used to enter the cipher text. replace used to strip whitespace.
inputText = inputText1
ngramDict = {}
highestValue = 0
def ngram(n): #Function used to populate ngramDict with n-grams. The argument is the amount of characters per n-gram.
    count = 0
    for letter in inputText:
        if str(inputText[count : count + n]) in ngramDict: #Check if the current n-gram is in ngramDict
            ngramDict[str(inputText[count : count + n])] = ngramDict[str(inputText[count : count + n])] + 1 #increments its value by 1
        else:
            ngramDict[str(inputText[count : count + n])] = 1 #Adds the n-gram and assigns it the value 1
        count = count + 1
    for bigram in ngramDict.keys(): #Iterates over the Bigram dict and removes any values which are less than the adaquate size (< n argument in function)
        if len(bigram) < n:
            del ngramDict[bigram]
#ngram(int(input("Please enter the n-gram value. (eg bigrams = 2 trigrams = 3)")))
ngram(2)
ngramList = [ (v,k) for k,v in ngramDict.items() ] #iterates through the ngramDict. Swaps the keys and values and places them in a tuple which is in a list to be sorted.
ngramList.sort(reverse=True) #Sorts the list by the value of the tuple
for v,k in ngramList: #Iterates through the list and prints the ngram along with the amount of occurrences
    print("There are " + str(v) + " " + str(k))
'''
