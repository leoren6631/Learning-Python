from collections import Counter
def freq(cipher):
    '''
    sum = 0
    for i in value:
        sum = sum + i
    '''
    sum1 = sum(cipher.values())
    #print(sum1)
    for j in cipher.values():
        i=(round(((j/float(sum1))*100),1))
        for key,value in dict(cipher).items():
            if j==value:
                cipher[key]=i
    return cipher
    #print('Black Hat Chanllenge frequecy' ,cipher)
#inputText = str(input("Please enter the cipher text to be analysed:")).replace(" ", "")
inputText1 = "wsmcdepldjplvvjvzexldepldkcsmpnjvcxfvcjcvpecsjptxlcfxplnzxvosjobjcvzlxldkosmptleawlmcslxwlzfvcliulocosmptlwexnvvmjncslsevcmcdlptcsjvwexvlphfddlcvkefplglxbpewwsmccslkddsjccslosjlauxeeaeazmpvxlmdtxlmcplvvdjlvjpsjvulxolucjepeasjvewpvzmddplvvcjvzjvaexcfplcsmcmwmblpvjptlpfjckexaexcjcfnlexlpnfxmpoljpslmxcvwslxlcslvlrfmdjcjlvsmnplglxoezlcedjalhfcaexcslojxofzvcmpolwsjostmglcslzmhljptqlmdefvkjvmvcxmptlcxmpvaexzlxeaosmxmoclxvwjvldkmpnvdewcslkvcfzhdlcsmcxfpamvcdexnhdlvvkefvmjnzxezlxxlvfzjptsjvujulmzmpzfvccmblcslamcwjcscsldlmpcsmcvwsmcslzfvczmblfusjvzjpncejpcsjvdjalslsmvvulpcsjvdjalhlvcwsesmvlpqeklnjczevc"
inputText2 = "msoodryewaivhohtepoholbtllsidotkitrncyhcemtowuetfenomntneiutirrktndloedegenhsnhrghcetceenaelfheceotglbsaiwncsaiuvonotnisoeesiuigmndttmfvneslpleblotroohttoewoeuwthbaelynttmrextrurheahutetntthnohftnntedinssdwerksreeodeweueqocttbuirotsriahkdtaodooinhnsertoenaorlecawhoiorcwedmmelidriwoiurehwunonisohounnotcthreaptcaiwedetmtmrjiaeyvraoawvteentrastenevntrteugnhhwotlreututussgoesytmheasdehtrtftiviosnsoseeaehrrytnshsusntauttsieabntoiieyhoatedbnemftbvthiierntyaavoevetwgipehgduaterelryooheeisltehorzesssratuithgrnlassenteuyosrchneitgeurihrclsrftmofgwawfonteahflniwhnqaoiteeflgkneetkneaunfoh"
inputText3 = "sfpqwagyewqbwodyvbckkglpndzqjkgzxnipewlazqhucagnkvvogzmzvbnevcadsfydlrjknaomuhlcewbkrevbcgqoybuysfyrcgvbuyexykncybuysfqjzqlsewexkfwnrrcjqijkljvbpgimctpqmxsltuizgmuxuypqwaxctugmdjdysyovexuhsorrkcppvbaevbpgckgmdjdyagatatkcsfljykifqcsxdyzqovslipqdymovkftkhwdkxovbwavuocyqftosovgzkfptquoomzgnmikfwnvuarcdftquaurxzqiptzfmbvtkdjtuypdymsppgcnndydwipwxbgvbdyagbgypdymsppkptodytmuypgezeroxknserryqkcykdjpgbcdyydobgzgnynqcbgbcvbzqartaqbdykvejwysejoargsckbiadulmfppdyagvbdygqoogjnneigtlcwysetzfmahhuvmtuwlapwhzdipewezfgvmbhlcucfztybojaiqqbrrvmsvvbpgwaxctucjerkvoyozaodyagafymsorrexydppcusevbdyou"
inputText4 = "hghiogfhedbgpswcvgyosiobtitoawiahimlanomglicchmcawiahineiayoesbimfneoehmwcgiixnagloaiaphogsiixhtlmephdzgnhoxerhperosglhnwcmdmhhmmioesepmieogbysoelnhphyadiihskpsglrcfeosephdlitrnaxwhirmwccmnremglhshbtzmhaiyqwnesqbesnrmilncrogshhihgnrphlngixfximdrxqyobipywhgyrmfanphoxmehglgalxgxttfososnfialgalxgeflnoyhthnozphoghtwmchphnazirmyolnochghimoamylmhhxzdyxypoexwcorogythlnopbthimovpanhphsnosodhobwnlnexhgidghoyhtpuoedberhwpzaluwnwtorlhgelexnwhganexxecrxtegzhhioebhrcgapsglhirhegrafyqyhphpoxhwnklnuecsnihpyhlnnfozoygqlryhgcshzxrmhihimoatmiexgarmdhwrhianhdnhoyyqhbalwccicrnayhhcgdxnxadhwaxesuihrcogotoghshtwamc"
inputText5 = "spponzjfvzsytvpwgkzzhwbjnmlmzkvihhlmolguupikwsgvyfpucxqdhqdcbttgxgiannhmhzcufzwzyvqbqpsqvwkudrkfgcpurlagmaujbbksrkjrdgzjzyiduadubwncofniivugzhzyrijzeddcwhcbcrbsciknasjzdbmauajjemnjjdfclwhgkbwvqvkymquclfoyzdsojlktsvzqhqylpzwolnxtgzbsnvjfgmarvynvzsjbrqxzkfunjvxjmhrlotldgzjcwhgnzgzhmvzbkfriuyvmhntwejvavnpjavisvjqhqmauzizvsytwvspekkcpyhataclmqgfbdovkcfnnfbphwrtdgfbdovvjmgebqblzydbegqtbeucpgmfgcpijeyxqrjsjvjzvmbytajhmtuqedezcwqcmtgczjpdcssoaqririhtvhhbnwaoigosgfirbgmlvnujttkrawnjekfcurvegkokzdokqdunyynkopfhlmhkihqfdokiymvivgcpijdhokwhjezrmggmuzacdsggfwhnfecsozhanhigbytlhcuzjucvcvhoacudomgrsgizchfnh"

num1 = Counter(inputText1)
num2 = Counter(inputText2)
num3 = Counter(inputText3)
num4 = Counter(inputText4)
num5 = Counter(inputText5)


print(num1)
#freq(sorted(num1.values(),reverse=True))
freq(num1)
print('Black Hat Chanllenge frequecy 1' ,num1,'\n\n\n')

print(num2)
freq(num2)
print('Black Hat Chanllenge frequecy 2' ,num2,'\n\n\n')

print(num3)
freq(num3)
print('Black Hat Chanllenge frequecy 3' ,num3,'\n\n\n')

print(num4)
freq(num4)
print('Black Hat Chanllenge frequecy 4' ,num4,'\n\n\n')

print(num5)
freq(num5)
print('Black Hat Chanllenge frequecy 5' ,num5,'\n\n\n')





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
