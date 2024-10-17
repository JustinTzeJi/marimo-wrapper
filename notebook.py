import marimo

__generated_with = "0.8.13"
app = marimo.App()


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

    - fanmade 
    - some may still be broken lmao 💀 
    - report issues at: [{mo.icon("ant-design:github-filled")}](https://github.com/JustinTzeJi/marimo-wrapper/issues)

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
def __(dropdown2):
    dropdown2
    return


@app.cell
def __(dr3_4, dr4_4, dropdown, dropdown3, dropdown4, mo):
    mo.hstack(
        [
            dropdown,
            dropdown3 if dr3_4 else mo.Html(""),
            dropdown4 if dr4_4 else mo.Html(""),
        ]
    )
    return


@app.cell
def __(fig2):
    fig2
    return


@app.cell
async def __():
    import marimo as mo
    import pandas
    import seaborn
    import matplotlib.pyplot as plt
    import micropip

    # await micropip.install("tornado", keep_going=True)
    import requests
    import fastparquet
    import zipfile
    import re
    import asyncio
    from inspect import getmembers, isfunction
    import importlib
    from time import sleep

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
        sleep,
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

    folder_dict = {}

    for fold_ in filtered_folder.name:
        folder_dict[fold_.split("_", 1)[1].replace("_", " ")] = fold_

    default_folder = (
        filtered_folder.name.iloc[0].split("_", 1)[1].replace("_", " ")
    )

    dropdown2 = mo.ui.dropdown(
        options=folder_dict,
        value=default_folder,
        label="Select a Project:",
    )
    return (
        default_folder,
        dropdown2,
        filtered_folder,
        fold_,
        folder_dict,
        folders,
        list_folder,
    )


@app.cell
def __():
    re_dict = {
        "os\.chdir\(.*\)": "",
        "df = df\[df\.date >= date\(START_YEAR,1,1\)\]": "df.date = pd.to_datetime(df.date).dt.date\n    df = df[df.date >= date(START_YEAR,1,1)]",
        ",'TESLA',": ",'Tesla',",
        "plt.savefig\S*dpi=400\)\\n    plt\.close\(\)\\n": "return plt.gcf()",
        "https://storage.data.gov.my": "https://corsproxy.marimo.app/https://storage.data.gov.my",
        "https://storage.dosm.gov.my/": "https://corsproxy.marimo.app/https://storage.dosm.gov.my/",
        "http://storage.dosm.gov.my/": "https://storage.dosm.gov.my/",
    }

    replace_dict = {
        "pyperclip.copy(ALT)": "",
        "import pyperclip": "",
        "len(tf[tf.maker == 'PROTON'])": "len(tf[tf.maker == 'Proton'])",
        "len(tf[tf.maker == 'PERODUA'])": "len(tf[tf.maker == 'Perodua'])",
        "https://storage.data.gov.my/catalogue/": "https://storage.data.gov.my/transportation/",
        "ncols=": "ncol=",
    }
    return re_dict, replace_dict


@app.cell
def __(pandas, re, requests, sleep):
    def initiate_folder(d_value, re_dict, replace_dict):
        while True:
            try:
                df_files = pandas.read_html(
                    f"https://corsproxy.marimo.app/https://github.com/Thevesh/charts/tree/main/{d_value}"
                )[0]
                break
            except Exception as ee:
                sleep(2)
                print("Connection issues. Retrying ...")

        if df_files.Name.str[-4:].isin([".csv", "xlsx", "quet"]).any():
            for files_ in df_files.Name:
                if files_[-4:] in [".csv", "xlsx", "quet"]:
                    r2 = requests.get(
                        f"https://raw.githubusercontent.com/Thevesh/charts/main/{d_value}/{files_}"
                    )
                    with open(files_, "wb") as f2:
                        f2.truncate(0)
                        f2.write(r2.content)

        url = f"https://raw.githubusercontent.com/Thevesh/charts/main/{d_value}/script.py"
        output = "module_thevcharts.py"
        r = requests.get(url)

        script_proxy = r.text

        for k, v in re_dict.items():
            script_proxy = re.sub(k, v, script_proxy)

        for kr, vr in replace_dict.items():
            script_proxy = script_proxy.replace(kr, vr)

        if d_value == "2024-02-14_valentines":
            script_proxy = script_proxy.replace(
                """df = df[pd.to_datetime(df.date).dt.year >= 2000]""",
                """df["date"] = pd.to_datetime(df.date).dt.date \n    df = df[pd.to_datetime(df.date).dt.year >= 2000]""",
            )

        if d_value == "2024-03-03_mmr":
            #     script_proxy = script_proxy.replace(
            #         """# ALT-text
            # ALT = 1
            # if ALT == 1:
            #     print(ax.get_title())
            #     for i in range(len(df)): print(f'{df.index[i]:%Y}: {df["rate"].iloc[i]:,.1f}')""",
            #         """print(df)""",
            #     )
            script_proxy = script_proxy.replace(
                """df = pd.read_parquet(URL).set_index('date')""",
                """df = pd.read_parquet(URL)\n    df['date'] = pd.to_datetime(df['date'])\n    df = df.set_index('date')""",
            )

        if d_value == "2024-03-22_lfpr":
            url_lfpr = f"https://raw.githubusercontent.com/Thevesh/charts/main/{d_value}/lfpr.xlsx"
            output_lfpr = "lfpr.xlsx"
            r_lfpr = requests.get(url_lfpr)
            with open(output_lfpr, "wb") as f_lfpr:
                f_lfpr.truncate(0)
                f_lfpr.write(r_lfpr.content)

            script_proxy = script_proxy.replace(
                """plt.savefig(f'heatmap.png',dpi=400, bbox_inches = 'tight')
        plt.close()""",
                "return plt.gcf()",
            )

        if d_value == "2024-05-01_income_distributions":
            script_proxy = script_proxy.replace(
                """if __name__ == '__main__':""", ""
            )
            script_proxy = script_proxy.replace(
                """    # ----- Household Income (DOSM) -----""",
                "def household_income():",
            )
            script_proxy = script_proxy.replace(
                """# ----- Income Declarations (LHDN) -----""",
                "return plt.gcf() \ndef incomme_declaration():",
            )
            script_proxy = script_proxy.replace(
                """# ----- Formal Sector Wages (DOSM) -----""",
                "return plt.gcf() \ndef formal_sctor_wage():",
            )
            script_proxy += "    return plt.gcf()"

        if d_value == "2024-05-12_byelection":
            script_proxy = script_proxy.replace(
                "ncols=len(order)", "ncol=len(order)"
            )
        if d_value == "2024-06-10_diesel":
            script_proxy = script_proxy.replace(
                "df['proportion'] = (df.diesel / df.total) * 100",
                "df['proportion'] = (df.diesel / df.total) * 100\n    df = df.set_index('year')",
            )

        with open(output, "w") as f:
            f.truncate(0)
            f.write("import marimo as mo\n" + script_proxy)
        options = [
            re.sub("\(", "()", re.sub("def ", "", a))
            for a in re.findall("def \w*\(", script_proxy)
        ]

        if d_value == "2024-05-01_income_distributions":
            options = [filt for filt in options if filt != "plot_distribution()"]
        # print(options)

        return True, options
    return initiate_folder,


@app.cell
def __(dropdown2, initiate_folder, mo, re_dict, replace_dict, sys):
    dled, options = initiate_folder(dropdown2.value, re_dict, replace_dict)

    if dled:

        if "module_thevcharts" not in sys.modules:
            exec("import module_thevcharts")
        else:
            exec("importlib.reload(sys.modules['module_thevcharts'])")

        options_dict = {}
        for opt_ in options:
            options_dict[opt_.replace("()", "").replace("_", " ")] = opt_

        default_opt = options[0].replace("()", "").replace("_", " ")

        dropdown = mo.ui.dropdown(
            options=options_dict,
            value=default_opt,
            label="Select a function to run :",
        )
    return default_opt, dled, dropdown, opt_, options, options_dict


@app.cell
def __(dropdown, dropdown2, mo):
    if dropdown2.value == "2024-05-26_ev":
        if dropdown.value == "top3()":
            drop3_list = ["cumulative", "monthly"]
            drop3_label = "CHART_TYPE"
            dropdown3 = mo.ui.dropdown(
                options=drop3_list, value=drop3_list[0], label=drop3_label
            )
            dr4_4 = False
        if dropdown.value == "bar_fueltype()":
            drop3_list = {"2024": 2024, "2023": 2023, "2022": 2022}
            drop3_label = "START_YEAR"
            dropdown3 = mo.ui.dropdown(
                options=drop3_list, value="2022", label=drop3_label
            )
            dr4_4 = False
        if dropdown.value == "bar_fueltype_top15()":
            drop3_list = ["Hybrid", "Electric"]
            drop3_label = "FUEL_TYPE"
            drop4_list = ["Blues", "Greens"]
            drop4_label = "COLOUR"
            dropdown3 = mo.ui.dropdown(
                options=drop3_list, value=drop3_list[0], label=drop3_label
            )
            dropdown4 = mo.ui.dropdown(
                options=drop4_list, value=drop4_list[0], label=drop4_label
            )
            dr4_4 = True
        dr3_4 = True
    else:
        dr3_4 = False
        dr4_4 = False
    return (
        dr3_4,
        dr4_4,
        drop3_label,
        drop3_list,
        drop4_label,
        drop4_list,
        dropdown3,
        dropdown4,
    )


@app.cell
def __(
    drop3_label,
    drop4_label,
    dropdown,
    dropdown2,
    dropdown3,
    dropdown4,
    mo,
):
    with mo.redirect_stdout():
        if dropdown2.value == "ev":
            if dropdown.value == "bar fueltype top15":
                func_out = f'{dropdown.value.replace(")","")}{drop3_label}="{dropdown3.value}", {drop4_label}="{dropdown4.value}")'
            elif dropdown.value == "bar fueltype":
                func_out = f'{dropdown.value.replace(")","")}{drop3_label}={dropdown3.value})'
            else:
                func_out = f'{dropdown.value.replace(")","")}{drop3_label}="{dropdown3.value}")'
            fig2 = eval("module_thevcharts." + func_out)
        else:
            fig2 = eval("module_thevcharts." + dropdown.value)
    return fig2, func_out


if __name__ == "__main__":
    app.run()
