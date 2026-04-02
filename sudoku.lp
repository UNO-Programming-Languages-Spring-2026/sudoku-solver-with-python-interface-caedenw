% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

subgrid(1..3, 1..3, 1).
subgrid(1..3, 4..6, 2).
subgrid(1..3, 7..9, 3).
subgrid(4..6, 1..3, 4).
subgrid(4..6, 4..6, 5).
subgrid(4..6, 7..9, 6).
subgrid(7..9, 1..3, 7).
subgrid(7..9, 4..6, 8).
subgrid(7..9, 7..8, 9).

% achieved: facts required for question 2

% { sudoku(1..9, 1..9, 1..9) } = 81.
{ sudoku(X,Y,1..9) } = 1 :- X = 1..9, Y = 1..9.
% achieved: get all combinations of a 9x9 board

:- sudoku(X, Y, N), initial(A, B, C), X = A, Y != B, N = C.
% achieved: exclude where the same value exists in different spots of the same row

:- sudoku(X, Y, N), initial(A, B, C), X != A, Y = B, N = C.
% achieved: exclude where the same values exist in different spots of the same column

:- sudoku(X, Y, N), sudoku(A, B, C), X = A, Y = B, N != C.
% achieved: remove duplicates in the same spot

:- sudoku(X, Y, N), sudoku(A, B, C), X = A, Y != B, N = C.
% achieved: exclude where the same values exist in different spots of the same column

:- sudoku(X, Y, N), sudoku(A, B, C), X != A, Y = B, N = C.
% achieved: exclude where the same values exist in different spots of the same column

:- subgrid(X1, Y1, G), subgrid(X2, Y2, G), sudoku(X1, Y1, N), sudoku(X2, Y2, N), X1 != X2, Y1 != Y2.
% achieved: exclude where a subgrid does not possess each of the numbers 1-9


#show sudoku/3.

