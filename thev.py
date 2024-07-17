import marimo

__generated_with = "0.7.4-dev2"
app = marimo.App()


@app.cell
async def __():
    import marimo as mo
    import pandas
    import seaborn
    import matplotlib as plt
    import micropip

    # await micropip.install("tornado", keep_going=True)
    import requests
    import fastparquet
    import zipfile
    import re
    import asyncio
    from inspect import getmembers, isfunction
    import importlib

    await micropip.install("openpyxl")
    import openpyxl
    import sys
    import lxml
    import html5lib
    import bs4
    return (
        asyncio,
        bs4,
        fastparquet,
        getmembers,
        html5lib,
        importlib,
        isfunction,
        lxml,
        micropip,
        mo,
        openpyxl,
        pandas,
        plt,
        re,
        requests,
        seaborn,
        sys,
        zipfile,
    )


@app.cell
def __(mo, pandas):
    list_folder = pandas.read_html(
        "https://corsproxy.marimo.app/https://github.com/Thevesh/charts/tree/main",
        extract_links="body",
    )

    folders = pandas.DataFrame(
        list_folder[0].Name.to_list(), index=list_folder[0].index
    )

    folders.columns = ["name", "href"]

    filtered_folder = folders[
        (
            ~folders.name.isin(
                [
                    ".gitignore",
                    ".github/workflows",
                    "LICENSE",
                    "README.md",
                    "requirements.txt",
                ]
            )
        )
        & (~folders.href.isin(["/Thevesh/charts/commits/main/", None]))
    ]

    dropdown2 = mo.ui.dropdown(
        options=filtered_folder.name, value=filtered_folder.name.iloc[0]
    )
    return dropdown2, filtered_folder, folders, list_folder


@app.cell
def __(pandas, re, requests):
    def initiate_folder(d_value):
        if (
            pandas.read_html(
                f"https://corsproxy.marimo.app/https://github.com/Thevesh/charts/tree/main/{d_value}"
            )[0]
            .Name.isin(["src.xlsx"])
            .any()
        ):
            url2 = f"https://raw.githubusercontent.com/Thevesh/charts/main/{d_value}/src.xlsx"
            output2 = "src.xlsx"
            r2 = requests.get(url2)
            with open(output2, "wb") as f2:
                f2.truncate(0)
                f2.write(r2.content)

        url = f"https://raw.githubusercontent.com/Thevesh/charts/main/{d_value}/script.py"
        output = "module_testingjk.py"
        r = requests.get(url)

        script = r.text

        script_proxy = re.sub(
            "os\.chdir\(.*\)",
            "",
            re.sub(
                "df = df\[df\.date >= date\(START_YEAR,1,1\)\]",
                "df.date = pd.to_datetime(df.date).dt.date\n    df = df[df.date >= date(START_YEAR,1,1)]",
                re.sub(
                    ",'TESLA',",
                    ",'Tesla',",
                    re.sub(
                        "plt.savefig\S*dpi=400\)\\n    plt\.close\(\)\\n",
                        "return plt.gcf()",
                        re.sub(
                            "https://storage.data.gov.my",
                            "https://corsproxy.marimo.app/https://storage.data.gov.my",
                            re.sub(
                                "https://storage.dosm.gov.my/",
                                "https://corsproxy.marimo.app/https://storage.dosm.gov.my/",
                                script,
                            ),
                        ),
                    ),
                ),
            ),
        )

        with open(output, "w") as f:
            f.truncate(0)
            f.write("import marimo as mo\n" + script_proxy)
        options = [
            re.sub("\(", "()", re.sub("def ", "", a))
            for a in re.findall("def \w*\(", requests.get(url).text)
        ]
        return True, options
    return initiate_folder,


@app.cell
def __(dropdown2, initiate_folder, mo, sys):
    dled, options = initiate_folder(dropdown2.value)
    # print(dled)
    if dled:
        if "module_testingjk" not in sys.modules:
            exec("import module_testingjk")
        else:
            exec("importlib.reload(sys.modules['module_testingjk'])")
        # options = list(zip(*getmembers(module_testingjk, isfunction)))[0]
        dropdown = mo.ui.dropdown(options=options, value=options[0])
    return dled, dropdown, options


@app.cell
def __(dropdown):
    fig2 = eval("module_testingjk." + dropdown.value)
    return fig2,


@app.cell
def __(mo):
    mo.md(f'# "Live" Thev Charts {mo.icon("flat-color-icons:line-chart")}')
    return


@app.cell
def __(mo):
    mo.center(
        mo.md(
            f"""## A WASM wrapper for charts by [@Thevesh](https://x.com/Thevesh)

    Note: 

    - all the functions are running on default paramters currently
    - some are still broken lmao 💀
    - fanmade 

    """
        )
    )
    return


@app.cell
def __(mo):
    mo.md(
        f"Source Code for Charts: [{mo.icon('ant-design:github-filled',size=25)}](https://github.com/Thevesh/charts)"
    ).callout()
    return


@app.cell
def __(mo):
    mo.md("Select a Project ⬇️:")
    return


@app.cell
def __(dropdown2):
    dropdown2
    return


@app.cell
def __(mo):
    mo.md("Select a function to run ⬇️:")
    return


@app.cell
def __(dropdown):
    dropdown
    return


@app.cell
def __(fig2):
    fig2
    return


if __name__ == "__main__":
    app.run()
