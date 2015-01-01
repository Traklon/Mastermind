def compte (l):
	occ = [0 for i in range (1,8)]
	for elt in l:
		occ[elt] = occ[elt]+1
	return occ
		

def conv (nb):
	l = []
	while (nb > 0):
		l.append (nb%10)
		nb = nb//10
	l.reverse()
	return l
	
def transfo (l):
	nb = 0
	for elt in l:
		nb = nb + elt
		nb = 10*nb
	return (nb//10)
	
def rep (code, occ, essai):
	occ2 = compte(essai)
	ntot = 0
	nn = 0
	for i in range (1,7):
		ntot = ntot + min(occ[i], occ2[i])
	for i in range (0,4):
		nn = nn + (code[i] == essai[i])
	return (nn, ntot-nn)
	
def poss2 (poss, S):
	l = []
	for (i,elt) in enumerate(poss):
		if (S[i]):
			l.append(transfo(elt))
	return l
	
def poss3 (poss, S):
	l = []
	for (i,elt) in enumerate(poss):
		if (S[i]):
			l.append(elt)
	return l
	
def conseil (poss, possC, possS, possSC, S):
	mini = 1296
	curr = 0
	for elt in poss:
		maxi = 0
		tab = [[0 for i in range (0,5)] for i in range (0,5)]
		for (i,e) in enumerate(possS):
			(nn,nb) = rep(e, possSC[i], elt)
			if (tab[nn][nb] == 0):
				tab[nn][nb] = e
				tot = 0
				for (i1,e1) in enumerate(possS):
					if (rep(e1, possSC[i1], elt) == (nn,nb)):
						tot += 1
				if (tot > maxi):
					maxi = tot
		if (maxi < mini):
			mini = maxi
			curr = elt
	return transfo(curr)
	
def jeuLibre ():
	from random import randint
	code = 0
	for i in range (1,5):
		code+=randint(1,6)
		code = code*10
	codeNb = code//10
	code = conv(codeNb)
	occ = compte(code)
	nbEssai = 6
	poss = [[0 for i in range (0,4)] for j in range (0,1296)]
	S = [True for j in range (0,1296)]
	for (j,elt) in enumerate(poss):
		tmp = j
		elt[0] = tmp//216+1
		tmp = tmp%216
		elt[1] = tmp//36+1
		tmp = tmp%36
		elt[2] = tmp//6+1
		tmp = tmp%6
		elt[3] = tmp+1
	possC = [[] for j in range (0,1296)]
	for (i,elt) in enumerate(poss):
		possC[i] = compte(elt)
	while(nbEssai > 0):
		essai = input();
		if (essai == 'etat'):
			print(poss2(poss,S))
			print("")
			continue
		if (essai == 'conseil'):
			possS = poss3(poss,S)
			possSC = [[] for j in range (0,1296)]
			for (i,elt) in enumerate(possS):
				possSC[i] = compte(elt)
			print(conseil(poss, possC, possS, possSC, S))
			print('')
			continue
		essai = int(essai)
		(nn,nb) = rep(code, occ, conv(essai))
		for (i,elt) in enumerate(poss):
			if (rep(elt, possC[i], conv(essai)) != (nn,nb)):
				S[i] = False
		if (nn == 4):
			break
		print (str(nn) + "n" + str(nb) + "b\n")
		nbEssai = nbEssai - 1
	if (nbEssai == 0):
		print ("Perdu ! Le code était : " + str(codeNb))
	else:
		print ("Félicitations ! Tu as gagné avec " + str(nbEssai-1) + " essai(s) restant(s) !")
	
		
			
			
	
	
	
	
	
	
	
	
	

	
	
	