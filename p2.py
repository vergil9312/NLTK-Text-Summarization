


text = """About six months ago, the White House announced a campaign – the Student Debt Challenge – to raise awareness of the existence of income-driven repayment options. In this week's post, the Student Loan Ranger updates readers on the initiative's impact.

There's no argument that college can be expensive – and the costs continue to rise. Recent statistics show that the majority of the fastest growing occupations in the U.S. require higher education. While policymakers and presidential candidates work on ways to make college more affordable, the current and past administrations have put multiple income-driven repayment plans in place to at least help ease the burden of student debt.

The problem, though, was that many borrowers weren't aware that these options existed. The Student Debt Challenge aims to help borrowers better understand their repayment options, and the plan's goal is to enroll 2 million more federal student loan borrowers into an income-driven plan.

The idea behind the initiative is to get employers involved in helping spread the word about these options. For example, Fidelity Investments introduced a program called the Step Ahead Student Loan assistance program, which not only provides tenured employees with a student loan repayment benefit but also educates them on their repayment and, if eligible, forgiveness options.

Rite Aid is also working with their 90,000 associates to ensure they are aware of the income-driven plans as well as reminding them of when to enroll and recertify their plans on an annual basis. And the National Housing Resource Center is training 500 housing counselors to work with clients to help them identify repayment plans that might help their overall financial circumstances.

These are just a few of the more than 40 organizations that have pledged to help spread the word and educate and advise borrowers on their repayment options. The Department of Education has also issued a free toolkit that employers can use to help educate their employees.

So far, the results are encouraging. After just three months, the campaign has increased participation to 23 percent of all borrowers.

That's a big jump from the 5 percent total enrollment four and a half years prior. The data also shows that these plans seem to be helping the exact populations it was intended to – those with higher debts and lower incomes.

What does this mean to prospective students and their families who are just starting to look into college financing? Although we always encourage families to minimize student debt to levels they know they will be affordable after graduation, choosing a field – such as finance and business – that tends to offer such employer assistance is another factor to consider. And now there is a growing trend of employers, both on their own and with the encouragement of the administration, who are assisting employees with managing their student debt.

While the benefit of student loan repayment isn't necessarily a new phenomenon, more recent college grads are looking for and more employers are now offering student loan repayment benefits in the form of payment reimbursement, help with student loan management or both. These benefits can help extend employee tenure, since young employees tend to switch jobs more often, as well as help relieve the stress of personal debt, which can increase employee productivity and decrease instances of internal fraud.

The bottom line is that when it comes to student debt, it takes a village. Employers helping their employees to take on the challenge of student debt is just another logical aspect step in this process.




"""


from nltk.tokenize import sent_tokenize, word_tokenize
import sys

# read text file 
#text = '' #create a empty string
#for line in sys.stdin:
#    text = text + line

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# convert some odd puncations which can't be recognized by NLTK
text = text.replace('“','"')
text = text.replace('”','"')
text = text.replace("’","'")

# this is stopwords of english from NLTK
sw = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

"""
Words that have a frequency term lower than min_cut or higher than max_cut will be ignored.
"""
min_cut = 0.1
max_cut = 0.9
stopwords = set(sw+list(punctuation)+list("it's"))
    
    
"""
Tokenize sentences and words
"""
sents = sent_tokenize(text)
word_sent = [word_tokenize(s.lower()) for s in sents]

"""
Computer the frequency of each of word.
"""
freq = dict()
for s in word_sent:
    for word in s:
        if word not in stopwords:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
# frequencies normalization and filerting
m = float(max(freq.values()))
for w in list(freq):
    freq[w] = freq[w]/m
    if freq[w] >= max_cut or freq[w] <= min_cut or w <= "a":
        del freq[w]

ranking = dict()
for i, sent in enumerate(word_sent):
    for w in sent:
        if w in freq:
            if i not in ranking:
                ranking[i] = freq[w]
            else:
                ranking[i] += freq[w]
if 0 in ranking:
    del ranking[0]
textLenReq = len(text.split())*0.25
# sort sentences according to their values
ranking = sorted(ranking,key=ranking.get,reverse=True)


print('----------------------------------')
print('Summary:\n')

# print the first sentence, which is usually important
print('*')
print(sents[0])
textLenReq -= len(sents[0].split())

# print sentences in accordance with their values, as long as the output length is less than 500 or 25% of total text length
outputLen = 0
i = 0
while outputLen < textLenReq and outputLen < 500:
    print('*')
    print(sents[ranking[i]])
    i += 1
    outputLen += len(sents[ranking[i]].split())
