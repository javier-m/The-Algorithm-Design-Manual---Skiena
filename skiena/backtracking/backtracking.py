from typing import Callable, Any, Iterator

from datastructures import Stack, StackEmptyError


def backtrack(a: list,
              is_a_solution: Callable[[list, int, Any], bool],
              construct_candidates: Callable[[list, int, Any], Iterator],
              inputs: Any=None,
              process_solution: Callable[[list, int, Any], Any]=None,
              make_move: Callable[[list, int, Any], Any]=None,
              unmake_move: Callable[[list, int, Any], Any]=None) -> Iterator:
    """backtracking DFS style"""
    if process_solution is None:
        process_solution = lambda a, k, inputs: None
    if make_move is None:
        make_move = lambda a, k, inputs: None
    if unmake_move is None:
        unmake_move = lambda a, k, inputs: None

    stack = Stack(implementation='linked_list')

    class StackItem:
        def __init__(self, k: int, candidates: Iterator=None):
            self.k = k
            self.candidates = candidates

    stack.push(StackItem(k=0))

    while True:
        try:
            stack_item = stack.pop()
            try:
                if stack_item.candidates is None:
                    stack_item.candidates = construct_candidates(a=a,
                                                                 k=stack_item.k,
                                                                 inputs=inputs)
                    candidate = next(stack_item.candidates)
                else:
                    unmake_move(a, stack_item.k, inputs)
                    candidate = next(stack_item.candidates)
            except StopIteration:
                pass
            else:
                a[stack_item.k] = candidate
                make_move(a, stack_item.k, inputs)
                if is_a_solution(a, stack_item.k, inputs):
                    process_solution(a, stack_item.k, inputs)
                    yield a
                    stack.push(stack_item)
                else:
                    stack.push(stack_item)
                    stack.push(StackItem(k=stack_item.k + 1))
        except StackEmptyError:
            break
