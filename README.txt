Picior Catalin 322CB

Basic SAT

Functia createVarDict pargurge fiecare clauza a expresiei si cauta in acestea
variabile diferite(negate sau nu) pentru a le asigna un numar de la 0 la
nr. de var - 1. Astfel, acest dictionar este folosit pentru a crea o matrice
de variabile si clauze, pentru a localiza cu usurinta pe ce coloana trebuie sa
punem codificarea variabilei. Functia returneaza dictionarul, dar si numarul de
clauze(lungimea matricei) si nr. de variabile diferite(latimea matricei).

Functia createMatrix initializeaza o matrice de dimensiuni nrClauze si nrVariabile
initializata la inceput cu 0. Parcurgem din nou fiecare clauza a expresiei, insa de
data aceasta daca gasim o variabila negata, o codificam cu 2 cu ajutorul valorii
din dictionar(matrix[clauzaCurenta][varDict[variabila]] = 2), sau cu 1 o variabila
nenegata.

In functia main a programului cream matricea de variabile si implicit dictionarul.
Folosim itertools pentru a putea genera toate combinatiile posibile de 0 si 1 de
lungime egala cu nr de variabile distincte. Parcurgem fiecare interpretare si
optimizam algortimul sa numere cate clauze sunt adevarate(dupa verificare, sarim'
la urmatoarea clauza din matrice), respectiv cate sunt false. Daca toate clauzele
sunt false, sarim la urmatoarea interpretare(nu va fi satisfiabila), insa daca
gasim o solutie, o printam si terminam programul.

BDD SAT

Urmam o abordare similara ca la prima problema, folosind aceleasi functii pentru a
crea matricea de variabile si clauze. In zona de date din root ul arborelui stocam
matricea intreaga. Ca si conditii de oprire din recursivitate avem depasirea nr
de variabile diferite si gasirea unei solutii. Pentru fiecare nod nou creat iteram
prin matricea  parintelui si adaugam in matricea copilului(initial vida), doar 
clauzele care nu se reduc in nodul respectiv. Reducerea clauzelor este realizata
in functiile evaluateRight si evaluateLeft; parcurgem fiecare clauza din matricea
parinte, iar daca var curenta este 0( copil stanga), iar variabila echivalenta
din matrice este diferita de 2( 0 negat -> 1 => se simplifica clauza), atunci
adaugam clauza in matricea copilului. Analog si pentru evaluateRightChild, doar
ca difera conditia de simplificare a clauzei( variabila din matrice diferita de 1).

Daca oricare dintre copii ramanae cu o matrice vida in urma functiei de evaluare,
inseamna ca fiecare clauza s-a redus, deci s-a gasit o solutie. Daca nu se gaseste
nicio solutie, continuam constrctia arborelui in preordine.

DIn cele doua grafice anexate, observam ca varianta bdd se comporta mult mai bine
pe acelasi set de date. Un factor in acest comportament il au optimizarile aduse,
in fiecare nod se retine o matrice mai mica sau egala decat la nivelul anterior,
iar faptul ca se lucreaza direct cu variabile(x1, x2 etc.), nu direct cu fiecare
combinare de 0 si 1 pentru implementare( dureaza O(n^2) pentru verificarea ficarei
interpretari) ajuta la cresterea performantei algoritmului.
