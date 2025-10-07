#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: gui.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
pygame-based UI: draws grid, handles input, shows turn/winner, and integrates AI.
"""
from __future__ import annotations

import sys
from typing import Optional, Tuple

import pygame

from .constants import (
    WINDOW_SIZE,
    GRID_SIZE,
    CELL_SIZE,
    LINE_WIDTH,
    MARGIN,
    BG,
    GRID,
    X_COLOR,
    O_COLOR,
    WIN_COLOR,
    TEXT_COLOR,
    INFO_COLOR,
    PLAYER_X,
    PLAYER_O,
    HUMAN,
    AI,
    FONT_MAIN_SIZE,
    FONT_INFO_SIZE,
)
from .game import GameState
from .ai import best_move


class TicTacToeUI:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe – pygame")
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 80))
        self.clock = pygame.time.Clock()
        self.font_main = pygame.font.SysFont("arial", FONT_MAIN_SIZE, bold=True)
        self.font_info = pygame.font.SysFont("arial", FONT_INFO_SIZE)
        self.state = GameState()
        # Start in Human vs AI (you are X)
        self.mode_x = HUMAN
        self.mode_o = AI

    def run(self) -> None:
        running = True
        while running:
            running = self._handle_events()
            self._maybe_ai_move()
            self._draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def _handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False
                if event.key == pygame.K_r:
                    self.state.reset()
                if event.key == pygame.K_m:
                    # Toggle game mode
                    if self.mode_o == AI:
                        self.mode_x, self.mode_o = HUMAN, HUMAN
                    else:
                        self.mode_x, self.mode_o = HUMAN, AI
                        # AI (O) should not move on reset toggle unless it's O's turn later.
                if event.key == pygame.K_n:
                    # Swap who the AI is (optional)
                    if self.mode_x == AI or self.mode_o == AI:
                        self.mode_x, self.mode_o = (AI, HUMAN) if self.mode_x == HUMAN else (HUMAN, AI)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._handle_click(pygame.mouse.get_pos())
        return True

    def _handle_click(self, pos: Tuple[int, int]) -> None:
        if self.state.winner is not None:
            return
        x, y = pos
        if y > WINDOW_SIZE:
            return  # clicked on info area
        row = y // CELL_SIZE
        col = x // CELL_SIZE

        current_mode = self._current_mode()
        if current_mode == HUMAN:
            self.state.make_move(row, col)

    def _current_mode(self) -> str:
        return self.mode_x if self.state.current == PLAYER_X else self.mode_o

    def _maybe_ai_move(self) -> None:
        if self.state.winner is not None:
            return
        if self._current_mode() != AI:
            return

        ai_symbol = self.state.current
        move = best_move(self.state, ai_symbol)
        if move is not None:
            r, c = move
            self.state.make_move(r, c)

    def _draw(self) -> None:
        self.screen.fill(BG)
        self._draw_grid()
        self._draw_marks()
        self._draw_status()

    def _draw_grid(self) -> None:
        # Vertical lines
        for i in range(1, GRID_SIZE):
            x = i * CELL_SIZE
            pygame.draw.line(self.screen, GRID, (x, MARGIN), (x, WINDOW_SIZE - MARGIN), LINE_WIDTH)
        # Horizontal lines
        for i in range(1, GRID_SIZE):
            y = i * CELL_SIZE
            pygame.draw.line(self.screen, GRID, (MARGIN, y), (WINDOW_SIZE - MARGIN, y), LINE_WIDTH)

        # Border
        pygame.draw.rect(
            self.screen,
            GRID,
            pygame.Rect(MARGIN // 2, MARGIN // 2, WINDOW_SIZE - MARGIN, WINDOW_SIZE - MARGIN),
            2,
        )

        # Winning line (if any)
        if self.state.win_line:
            (r1, c1), (r2, c2) = self.state.win_line
            x1 = c1 * CELL_SIZE + CELL_SIZE // 2
            y1 = r1 * CELL_SIZE + CELL_SIZE // 2
            x2 = c2 * CELL_SIZE + CELL_SIZE // 2
            y2 = r2 * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.line(self.screen, WIN_COLOR, (x1, y1), (x2, y2), LINE_WIDTH + 4)

    def _draw_marks(self) -> None:
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                mark = self.state.board[r][c]
                cx = c * CELL_SIZE + CELL_SIZE // 2
                cy = r * CELL_SIZE + CELL_SIZE // 2
                size = CELL_SIZE // 3
                if mark == PLAYER_X:
                    # Draw X
                    pygame.draw.line(
                        self.screen,
                        X_COLOR,
                        (cx - size, cy - size),
                        (cx + size, cy + size),
                        LINE_WIDTH,
                    )
                    pygame.draw.line(
                        self.screen,
                        X_COLOR,
                        (cx + size, cy - size),
                        (cx - size, cy + size),
                        LINE_WIDTH,
                    )
                elif mark == PLAYER_O:
                    pygame.draw.circle(self.screen, O_COLOR, (cx, cy), size, LINE_WIDTH)

    def _draw_status(self) -> None:
        y_base = WINDOW_SIZE + 10
        info_rect = pygame.Rect(0, WINDOW_SIZE, WINDOW_SIZE, 80)
        pygame.draw.rect(self.screen, (24, 24, 30), info_rect)

        if self.state.winner is None:
            status = f"Turn: {self.state.current}"
        elif self.state.winner == "draw":
            status = "Draw!"
        else:
            status = f"Winner: {self.state.winner}"

        mode_str = f"Mode: X={self.mode_x.upper()}  O={self.mode_o.upper()}  [M] Toggle  [R] Restart"
        text1 = self.font_main.render(status, True, TEXT_COLOR)
        text2 = self.font_info.render(mode_str, True, INFO_COLOR)

        self.screen.blit(text1, (12, y_base))
        self.screen.blit(text2, (12, y_base + 38))
