%1
%1A
scum(1,1).

scum(N,Res):-
    N>1,
    N1 is N-1,
    scum(N1,Res1),
    Res is Res1 + N.

%1B
sumDigits(0,0).

sumDigits(Num,Sum):-
    Num>0,
    D is Num mod 10,
    Num1 is Num // 10,
    sumDigits(Num1,Sum1),
    Sum is Sum1 + D.



%2
%2A
split(N, Res) :-
    split(N, [], Res).

split(N, Acc, [N|Acc]) :-
    N < 10.

split(N, Acc, Res):-
    N >= 10,
    D is N mod 10,
    N1 is N // 10,
    split(N1, [D|Acc], Res).

%2B
createList(List, Num) :-
    createList(List, 0, 1, Num).

createList([], Acc, _, Acc).

createList([H|T], Acc, Pow, Num) :-
    NewAcc is Acc + H * Pow,
    NewPow is Pow * 10,
    createList(T, NewAcc, NewPow, Num).

%2C
reverseNum(Num, RevNum) :-
    split(Num, Digits),
    createList(Digits, RevNum).


%3
%3A
in_list(X, [X|_]).

in_list(X, [_|T]) :- in_list(X, T).

intersection([], _, []).

intersection([H|T],L2,[H|Z]):-
    in_list(H,L2),
    intersection(T,L2,Z).

intersection([H|T],L2,Z):-
    \+ in_list(H,L2),
    intersection(T,L2,Z).

%3B
minus([], _, []).

minus([H|T], L2, Z) :-
    in_list(H, L2),
    minus(T, L2, Z).

minus([H|T], L2, [H|Z]) :-
    \+ in_list(H, L2),
    minus(T, L2, Z).
