import pathlib
import pandas as pd
from sbireport.trades import extract_trades
from sbireport.calculators import calcposition, calcweight

rpt_path = (pathlib.Path.cwd() / ".." / "sbireport" / "data").resolve()
ex1_rpt_path = (
    pathlib.Path.cwd() / ".." / "sbireport" / "data" / "EX-1-REGULAR.html"
).resolve()


def test_trades_extractor_pass_0():
    trades = extract_trades(rpt_path)
    print(trades)
    assert isinstance(trades, pd.DataFrame)
    assert len(trades) == 11


def test_trades_extractor_pass_1():
    trades = extract_trades(ex1_rpt_path)
    print(trades)
    assert isinstance(trades, pd.DataFrame)
    assert len(trades) == 8


def test_position_calc_pass_0():
    trades = extract_trades(rpt_path)
    position = calcposition(trades)
    position = calcweight(position)
    print(position)
    assert isinstance(position, pd.DataFrame)
    assert len(position) == 6
