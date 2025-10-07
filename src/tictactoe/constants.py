#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: constants.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
Centralized constants for dimensions, colors, and UI text.
"""
from __future__ import annotations

# Window / board
WINDOW_SIZE = 480
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 6
MARGIN = 12

# Colors (RGB)
BG = (30, 30, 38)
GRID = (200, 200, 210)
X_COLOR = (242, 95, 92)
O_COLOR = (36, 123, 160)
WIN_COLOR = (255, 200, 87)
TEXT_COLOR = (230, 230, 235)
INFO_COLOR = (160, 170, 180)

# Fonts
FONT_MAIN_SIZE = 36
FONT_INFO_SIZE = 20

# Gameplay
HUMAN = "human"
AI = "ai"
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = ""
