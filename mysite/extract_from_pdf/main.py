import pandas as pd
import sys

from extract import *
from analysis import *


def main():
    start = time.time()
    pdf_path = "yes1.pdf"

    print("[INFO] Starting extraction...")
    name, acc_no, bank, ifsc = extract_data(pdf_path)

    data = pd.read_excel(pdf_path[:pdf_path.find(".")] + ".xlsx")

    total_trans, length = summary(data)
    info = {"name": name, "bank": bank, "account_no": acc_no, "ifsc": ifsc, "total_months_statement": length,
            "total_transactions": total_trans}

    print("[INFO] Classifying Transactions...")
    data = classify_trans(data)
    
    data = money(data)
    
    processed_path = pdf_path[:pdf_path.find(".")] + "_processed" + ".xlsx"
    data.to_excel(processed_path, index=False)

    salary = redundant_trans(processed_path, length)
    info["salary"] = salary
    print("[INFO] Running balances...")

    bal_data = calculate_balances(data, pdf_path)

    # print(bal_data)

    print("[INFO] Analysing Cash Inflow and Outflow")
    

if __name__ == '__main__':
    # path = sys.argv[1]
    print("[INFO] Initializing...")
    res = main()
    print(res)
    print(type(res))
