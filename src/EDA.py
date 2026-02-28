import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # I. Software
    """)
    return


@app.cell
def _():
    import polars as pl
    import numpy as np

    return (pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #1. Data Loading
    """)
    return


@app.cell
def _(pl):
    df = pl.read_csv("dataset/diabetic_data.csv", null_values="?")
    df
    return


@app.cell
def _(pl):
    admision_type_id_mapping = pl.read_csv("dataset/admission_type_id_mapping.csv")
    admision_type_id_mapping
    return


@app.cell
def _(pl):
    admision_source_id_mapping = pl.read_csv("dataset/admission_source_id_mapping.csv")
    admision_source_id_mapping
    return


@app.cell
def _(pl):
    discharge_disposition_id_mapping = pl.read_csv("dataset/discharge_disposition_id_mapping.csv")
    discharge_disposition_id_mapping
    return


if __name__ == "__main__":
    app.run()
