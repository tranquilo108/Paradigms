sum_list([], 0).  % Базовый случай: сумма пустого списка равна 0.

sum_list([Head | Tail], Sum) :-
    sum_list(Tail, TailSum),  % Рекурсивный вызов для хвоста списка.
    Sum is Head + TailSum.   % Суммируем голову списка с суммой хвоста.
    
