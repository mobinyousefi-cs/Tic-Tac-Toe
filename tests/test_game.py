#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: test_game.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
Unit tests for core game logic (no pygame dependency).
"""
from __future__ import annotations

from tictactoe.game import GameState
from tictactoe.constants import PLAYER_X, PLAYER_O, EMPTY


def test_initial_state():
    s = GameState()
    assert s.current == PLAYER_X
    assert s.winner is None
    assert all(cell == EMPTY for row in s.board for cell in row)


def test_simple_move_and_turn_swap():
    s = GameState()
    assert s.make_move(0, 0) is True  # X
    assert s.board[0][0] == PLAYER_X
    assert s.current == PLAYER_O


def test_no_overwrite():
    s = GameState()
    s.make_move(0, 0)
    assert s.make_move(0, 0) is False


def test_row_win():
    s = GameState()
    s.make_move(0, 0)  # X
    s.make_move(1, 0)  # O
    s.make_move(0, 1)  # X
    s.make_move(1, 1)  # O
    s.make_move(0, 2)  # X wins
    assert s.winner == PLAYER_X
    assert s.win_line is not None


def test_draw():
    s = GameState()
    # X O X
    # X X O
    # O X O
    moves = [(0,0),(0,1),(0,2),(1,2),(1,0),(2,0),(1,1),(2,2),(2,1)]
    # X, O, X, O, X, O, X, O, X
    for r, c in moves:
        assert s.make_move(r, c)
    assert s.winner == "draw"
