% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

1 { sudoku(X,Y,N) : N=1..9 } 1 :- X=1..9, Y=1..9.
sudoku(X,Y,N) :- initial(X,Y,N).

:- sudoku(X,Y,N), sudoku(X,Y2,N), Y != Y2.
:- sudoku(X,Y,N), sudoku(X2,Y,N), X != X2.

#show sudoku/3.

subgrid(X,Y,1+((X-1)/3)*3+(Y-1)/3) :- X=1..9, Y=1..9.

:- subgrid(X,Y,G), subgrid(X2,Y2,G), sudoku(X,Y,N), sudoku(X2,Y2,N), X != X2.
:- subgrid(X,Y,G), subgrid(X2,Y2,G), sudoku(X,Y,N), sudoku(X2,Y2,N), Y != Y2.