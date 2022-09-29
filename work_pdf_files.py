#%%
import os
import pandas as pd
from PyPDF2 import PdfReader
from datetime import datetime
import random as rnd

#%%
# VARIABLES
target_dir = r"C:\Users\iurkl\OneDrive\Private\Accountability\Credit_Card_to_Check"

os.chdir(target_dir)

sum_head_foot = {
    "HEADER": ["•Détail devosopérations", "•Detail vanuwverrichtingen"],
    "FOOTER": ["€ Nouveau solde", "€ Nieuw saldo"],
}

detail_head_foot = {
    "HEADER": ["ANCIEN SOLDE"],
    "FOOTER": ["NOUVEAU SOLDE"],
    "PAYABLE": ["DOMICILIATION"],
}

# %%
# MAIN
file1 = target_dir + "\\" + os.listdir()[0]

files = []
for i, j in enumerate(os.listdir()):
    files.append(target_dir + "\\" + j)


# %%
def fetch_file(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def fetch_summary(text):
    for i, j in enumerate(text.splitlines()):
        if any(item in j for item in sum_head_foot["HEADER"]):
            sum_start_index = i
        elif any(item in j for item in sum_head_foot["FOOTER"]):
            sum_end_index = i
    sum_final = text.splitlines()[sum_start_index:sum_end_index]
    expense_summary = {
        "DESCRIPTION": [],
        "DATE": [],
        "AMOUNT": [],
    }
    # It was found that the first 3 lines of the summary have no use and the 4th line is different from the other lines
    for i, j in enumerate(sum_final):
        if i == 3:
            l = j.split()
            expense_summary["DATE"].append(l[1])
            if any(sign in l for sign in ["-", "+"]):
                expense_summary["AMOUNT"].append(l[2] + l[3])
                expense_summary["DESCRIPTION"].append(" ".join(l[4:]))
            else:
                expense_summary["AMOUNT"].append(l[2])
                expense_summary["DESCRIPTION"].append(" ".join(l[3:]))
        elif i > 3 and len(j.split()) > 2:
            l = j.split()
            expense_summary["DATE"].append(l[0])
            if any(sign in l for sign in ["-", "+"]):
                expense_summary["AMOUNT"].append(l[1] + l[2])
            else:
                expense_summary["AMOUNT"].append(l[2])
            expense_summary["DESCRIPTION"].append(" ".join(l[3:]))
    return pd.DataFrame(expense_summary)


def fetch_expenses(text):

    for i, j in enumerate(text.splitlines()):
        if "DETAIL DES OPERATIONS DU" in j:
            period_line = text.splitlines()[i]
    edited_txt = text[
        text.index("ANCIEN SOLDE") : text.index("NOUVEAU SOLDE")
        + text[text.index("NOUVEAU SOLDE") :].index("\n")
    ]
    return edited_txt, period_line


#%%
print("Fetching the Summary Expense", flush=True)

df_summary = pd.DataFrame({"DESCRIPTION": [], "DATE": [], "AMOUNT": [], "PERIOD": []})
df_detailed = pd.DataFrame(
    {
        "DESCRIPTION": [],
        "COUNTRY": [],
        "DATE_SPENT": [],
        "DATE_EFFECTIVE": [],
        "AMOUNT": [],
    }
)

for f in files:
    # It is very important that the file name follows the same structure

    date = f[-10:-6] + "/" + f[-6:-4] + "/01"
    date = datetime.strptime(date, "%Y/%m/%d")
    t = fetch_file(f)
    df_sum_k = fetch_summary(t)
    df_sum_k["PERIOD"] = date
    df_summary = pd.concat([df_summary, df_sum_k])

df_summary = df_summary.reset_index(drop=True)


#%%

print("Fetching the Detailed Expense", flush=True)


def fetch_expenses(text):
    first_period = ["01/10/2021", "19/11/2021"]  # The very period of the card

    for i, j in enumerate(text.splitlines()):
        if "DETAIL DES OPERATIONS DU" in j:
            period_line = text.splitlines()[i]
    edited_txt = text[
        text.index("ANCIEN SOLDE") : text.index("NOUVEAU SOLDE")
        + text[text.index("NOUVEAU SOLDE") :].index("\n")
    ]

    period_start = period_line[
        period_line.index("DU") + 2 : period_line.index("AU")
    ].strip()
    period_end = period_line[period_line.index("AU") + 2 : period_line.index("AU") + 12]

    try:
        period_start = datetime.strptime(period_start, "%d/%m/%Y")
    except:
        period_start = datetime.strptime(first_period[0], "%d/%m/%Y")
    try:
        period_end = datetime.strptime(period_end, "%d/%m/%Y")
    except:
        period_end = datetime.strptime(first_period[1], "%d/%m/%Y")

    p_month_year = {
        "YEARS": [period_start.year, period_end.year],
        "MONTHS": [period_start.month, period_end.month],
    }

    expense_details = {
        "DESCRIPTION": [],
        "COUNTRY": [],
        "DATE_SPENT": [],
        "DATE_EFFECTIVE": [],
        "AMOUNT": [],
    }
    for i, j in enumerate(edited_txt.splitlines()):
        if any(sign in j for sign in ["-", "+"]):
            if any(item in j for item in detail_head_foot["FOOTER"]):
                amount = j.split()[-1] + j.split()[-2]
                if "00" in j.split()[0]:
                    spe = period_end.strftime("%d/%m/%Y")
                else:
                    spe = (
                        j.split()[0]
                        + "/"
                        + str(
                            p_month_year["YEARS"][
                                p_month_year["MONTHS"].index(int(j.split()[0][-2:]))
                            ]
                        )
                    )
                eff = spe
                ctr = "BE"
                desc = " ".join(j.split()[1:-2])

            else:
                amount = j.split()[-1] + j.split()[-2]

                eff = (
                    j.split()[-3]
                    + "/"
                    + str(
                        p_month_year["YEARS"][
                            p_month_year["MONTHS"].index(int(j.split()[-3][-2:]))
                        ]
                    )
                )
                spe = (
                    j.split()[-4]
                    + "/"
                    + str(
                        p_month_year["YEARS"][
                            p_month_year["MONTHS"].index(int(j.split()[-4][-2:]))
                        ]
                    )
                )
                ctr = j.split()[-5]
                desc = " ".join(j.split()[:-5])
            expense_details["DESCRIPTION"].append(desc)
            expense_details["COUNTRY"].append(ctr)
            expense_details["DATE_SPENT"].append(spe)
            expense_details["DATE_EFFECTIVE"].append(eff)
            expense_details["AMOUNT"].append(amount)

    return expense_details


rand_file = fetch_file(files[rnd.randint(0, len(files) - 1)])

expenses = fetch_expenses(fetch_file(files[rnd.randint(0, len(files) - 1)]))
