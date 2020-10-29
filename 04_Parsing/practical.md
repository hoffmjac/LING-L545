* Tree 3

Tree does not recognised suppressed subject, and instead recongises the object of the sentence as a nominal dependent.

* Tree 4

Tree incorrectly considers the object of the sentence to be an oblique nominal to the verb. This is likely because it is making the wrong generalisation about how to
treat numbers in German.

* Tree 6

This sentence has a suppressed subject and object, and predictably the tree incorrectly assigns the subject as an adverbial phrase, and does not mark any object.

* Tree 11

Supressed subject and adverbial phrase caused issues. Notably, the adverbial phrase is split into two parts,
with the first part being given the "dep" tag, i.e. the parser had no idea what to do with it. A database of common
adverbial phrases would surely solve this problem.

* Tree 14

A common phrase has been shortened so much over time that it does not retain it's verb, subject, nor indirect object.
"(Ich) (wünsche) (euch) alles bestens,..." The parser tagged the object as the subject. This confusion
on the parser's part is understandable. It also marked the emoticon ":)" as a conjuction.

* Tree 23

Marks an adverb as the root, matched to a copulative that should actually be the root. Very strange that it would
mark this adverb, which has no appearances of being a verb, as a root.

* Tree 25

Supressed verb, and unclear even from my perspective if the one noun in the sentence is a subject or an object.
Seems unfair to put the parser through a sentence like this. An English example: "I'll need some milk from the
grocery." "Milk, too." And then asking the parser, or a human, to analyse only "Milk, too." Can't really verify
how correct or incorrect this one is, interestingly.

* Tree 39

The parser has again marked a subject as the root, and now I am not sure if the root always has to be verbs. 
The issue in this tree, where there is a verb, is that marking a potentially copulative verb as copulative
seems to take precedence over marking it as the root when there are no other verbs in the sentence,
making that copulative-potential verb actually the root verb in a nominative construction.

* Tree 42

Another supressed verb and subject, very similar to English "Best coffee in town". The parser marks the subject
as the root; I think this parser puts too much emphasis on finding a verb in dialogue-type sentences where 
suppressed verbs are common.

* Tree 43

Ending with an interesting one here, it seems like the segmenter might have failed, because the tokenised sentence
here is actually an incomplete sentence, most obvious because the first word is not capitalised. Seems like
an issue with the corpus. There's also a non-German word here that is not a proper noun, "maja". Very strange.



```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     84.02 |     84.02 |     84.02 |     84.02
LAS        |     79.37 |     79.37 |     79.37 |     79.37
```



