#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: ai.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
Minimax AI with alpha-beta pruning for optimal Tic Tac Toe moves.
"""
from __future__ import annotations

from typing import Tuple, Optional

from .game import GameState
from .constants import PLAYER_X, PLAYER_O


def best_move(state: GameState, ai_symbol: str) -> Optional[Tuple[int, int]]:
    """Return the optimal move (row, col) for ai_symbol, or None if no moves."""
    if state.winner is not None:
        return None

    best_score = float("-inf") if ai_symbol == PLAYER_X else float("inf")
    move: Optional[Tuple[int, int]] = None

    for (r, c) in state.available_moves():
        s2 = state.clone()
        s2.make_move(r, c)
        score = _minimax(s2, ai_symbol, alpha=float("-inf"), beta=float("inf"))
        if ai_symbol == PLAYER_X:
            if score > best_score:
                best_score, move = score, (r, c)
        else:
            if score < best_score:
                best_score, move = score, (r, c)

    return move


def _minimax(state: GameState, ai_symbol: str, alpha: float, beta: float) -> float:
    if state.winner is not None:
        if state.winner == ai_symbol:
            return 1.0
        if state.winner == "draw":
            return 0.0
        return -1.0

    current = state.current
    maximizing = current == ai_symbol

    if maximizing:
        value = float("-inf")
        for (r, c) in state.available_moves():
            s2 = state.clone()
            s2.make_move(r, c)
            value = max(value, _minimax(s2, ai_symbol, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for (r, c) in state.available_moves():
            s2 = state.clone()
            s2.make_move(r, c)
            value = min(value, _minimax(s2, ai_symbol, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
