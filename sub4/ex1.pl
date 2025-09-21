/* facts about gender.*/
male(tal).        % Father
male(moshe).      % Grandfather
male(maor).       % Me
male(avichai).    % Uncle (not blood-related)
male(nahman).     % Cousin
male(meir).       % Brother-in-law
male(benaya).     % Second cousin

female(ifat).     % Mother
female(ester).    % Grandmother
female(maayan).   % Sister
female(shaharit). % Aunt
female(may).      % Niece
female(or).
female(zehava).
female(adiba).

/* facts about parent-child relationships.*/
parent(tal, maayan). % Tal and Ifat are parents of Maayan
parent(ifat, maayan). % Tal and Ifat are parents of Maayan
parent(tal, maor). % Tal and Ifat are parents of Maor
parent(ifat, maor). % Tal and Ifat are parents of Maor
parent(or, benaya).
parent(moshe, tal).
parent(ester, ifat).
parent(ester, shaharit).
parent(zehava, or).
parent(adiba, zehava).
parent(adiba, ester).
parent(meir, may).
parent(maayan, may).
parent(shaharit, nahman).
parent(avichai, nahman).

/* facts about marital relationships.*/
married(tal, ifat).
married(avichai, shaharit).
married(meir, maayan).

/*--------------------------------------------------------------------------------------*/
uncle(X, Y) :- parent(P, Y), siblings(X, P), male(X).
aunt(X, Y) :- parent(P, Y), siblings(X, P), female(X).
bnei_dodim(X, Y) :- parent(P1,X), parent(P2,Y), siblings(P1,P2).

/*1*/ father(X,Y):- male(X), parent(X,Y).
/*2*/ mother(X,Y):- female(X), parent(X,Y).
/*3*/ son(X,Y):- male(X), parent(Y,X).
/*4*/ daughter(X,Y):- female(X), parent(Y,X).
/*5*/ grandfather(X,Y):- male(X), parent(X,Z), parent(Z,Y).
/*6*/ grandmother(X,Y):- female(X), parent(X,Z), parent(Z,Y).
/*7*/ grandson(X,Y):- male(X), parent(Y,Z), parent(Z,X).
/*8*/ granddaughter(X,Y):- female(X), parent(Y,Z), parent(Z,X).
/*9*/ siblings(X,Y):- parent(Z,X), parent(Z,Y), X\=Y.
/*10*/ uncle_unrelated(X,Y):- aunt(A,Y), married(X,A).
/*11*/ ben_doda(X,Y):- male(X), parent(A,X), aunt(A,Y).
/*12*/ brother_in_law(X,Y) :-
            male(X),
            (married(X,S), siblings(S,Y);
            married(S,Y), siblings(X,S)).
/*13*/ niece(X,Y):- female(X), parent(P,X), siblings(P,Y).
/*14*/ bney_dodim_2_degree(X,Y):-parent(P1,X), parent(P2,Y), bnei_dodim(P1,P2).