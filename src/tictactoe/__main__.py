#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Tic Tac Toe (pygame)
File: __main__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-07
Updated: 2025-10-07
License: MIT License (see LICENSE file for details)
=========================================================================================================

Description:
CLI entry point. Launches the pygame UI.
Usage:
    python -m tictactoe
    tictactoe
"""
from __future__ import annotations

from .gui import TicTacToeUI


def main() -> None:
    ui = TicTacToeUI()
    ui.run()


if __name__ == "__main__":
    main()
