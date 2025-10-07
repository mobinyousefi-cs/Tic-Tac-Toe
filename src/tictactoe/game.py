#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: game.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
Pure game logic for Tic Tac Toe: board state, moves, win/draw detection, and utilities.
This module is UI-agnostic and fully unit-testable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .constants import GRID_SIZE, PLAYER_X, PLAYER_O, EMPTY


Board = List[List[str]]  # 3x3 board of "X", "O", or ""


@dataclass
class GameState:
    board: Board = field(default_factory=lambda: [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)])
    current: str = PLAYER_X  # X always starts
    winner: Optional[str] = None
    win_line: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None  # ((r1,c1),(r2,c2))

    def reset(self) -> None:
        self.board = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.current = PLAYER_X
        self.winner = None
        self.win_line = None

    def available_moves(self) -> List[Tuple[int, int]]:
        return [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.board[r][c] == EMPTY]

    def make_move(self, row: int, col: int) -> bool:
        if self.winner is not None:
            return False
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            return False
        if self.board[row][col] != EMPTY:
            return False

        self.board[row][col] = self.current
        self._evaluate_winner()
        if self.winner is None:
            self.current = PLAYER_O if self.current == PLAYER_X else PLAYER_X
        return True

    def _evaluate_winner(self) -> None:
        b = self.board
        lines = []

        # Rows and columns
        for i in range(GRID_SIZE):
            lines.append(((i, 0), (i, 1), (i, 2)))
            lines.append(((0, i), (1, i), (2, i)))

        # Diagonals
        lines.append(((0, 0), (1, 1), (2, 2)))
        lines.append(((0, 2), (1, 1), (2, 0)))

        for a, b1, c in lines:
            r1, c1 = a
            r2, c2 = b1
            r3, c3 = c
            if self.board[r1][c1] != EMPTY and self.board[r1][c1] == self.board[r2][c2] == self.board[r3][c3]:
                self.winner = self.board[r1][c1]
                self.win_line = ((r1, c1), (r3, c3))
                return

        if all(cell != EMPTY for row in self.board for cell in row):
            self.winner = "draw"
            self.win_line = None

    def clone(self) -> "GameState":
        cloned = GameState()
        cloned.board = [row[:] for row in self.board]
        cloned.current = self.current
        cloned.winner = self.winner
        cloned.win_line = self.win_line
        return cloned
