all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst

	hfst-lexc ava.lexc -o ava.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 ava.lexc.hfst -2 chv.twol.hfst -o ava.gen.hfst

	hfst-lexc fin.lexc -o fin.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 fin.lexc.hfst -2 chv.twol.hfst -o fin.gen.hfst
	hfst-invert chv.gen.hfst -ochv.mor.hfst 
