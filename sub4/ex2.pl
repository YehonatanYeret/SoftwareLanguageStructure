/*helpers from the presentation*/
del(X,[X|Xs],Xs).
del(X,[Y|Xs],[Y|Ys]):- del(X,Xs,Ys).
insert(X,L,Res):- del(X,Res,L).
/*-----------------------------*/

%1
reverse([],Acc,Acc).

reverse([X|Xs],Acc,Res):-
             reverse(Xs,[X|Acc],Res).

reverse(L,Z):-reverse(L,[],Z).

%2
member(X,[X | _]).
member(X,[Y | Tail]):- member(X, Tail).

%3
palindrom([]).
palindrom([_]).
palindrom([X | Tail]):- append(Rest,[X],Tail), palindrom(Rest).

%4
sorted([]).
sorted([_]).
sorted([X, Y | Tail]):- X=<Y, sorted([Y|Tail]).

%5
permutation([],[]).
permutation([X|L], P):- 
          permutation(L, L1), insert(X, L1, P).
