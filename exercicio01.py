import copy
import csv
from pathlib import Path
from pprint import pprint
from datetime import datetime


def check_transaction(t1, list_transactions):
    def set_found(transaction):
        transaction.append("FOUND")
        return transaction

    def set_missing(transaction):
        transaction.append("MISSING")
        return transaction

    return_transaction = [set_found(t1) for tran2 in list_transactions if t1[1:] == tran2[1:]]
    return_transaction = [set_missing(t1)] if len(return_transaction) == 0 else return_transaction
    return return_transaction[0]


def remove_duplicate(tran_idx, tran, list_tran):
    for idx, tran_ojb in enumerate(list_tran):
        if (tran[1:] == tran_ojb[1:]) and (tran != tran_ojb):
            d1 = datetime.strptime(tran[0], '%Y-%m-%d')
            d2 = datetime.strptime(tran_ojb[0], '%Y-%m-%d')
            if d1 <= d2 and d2 > d1:
                del list_tran[idx]
            elif d2 <= d1 and d1 > d2:
                del list_tran[tran_idx]
    return list_tran


def reconcile_accounts(transactions1, transactions2):
    transactions1 = sorted(transactions1, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
    transactions2 = sorted(transactions2, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
    copy_list2 = copy.deepcopy(transactions2)
    copy_list1 = copy.deepcopy(transactions1)

    list1 = [check_transaction(t1, copy_list2) for t1 in transactions1]
    list2 = [check_transaction(t2, copy_list1) for t2 in transactions2]

    list1 = [remove_duplicate(idx, t1, list1) for idx, t1 in enumerate(list1)][0]
    list2 = [remove_duplicate(idx, t2, list2) for idx, t2 in enumerate(list2)][0]

    return list1, list2


if __name__ == '__main__':
    transactions1 = list(csv.reader(Path('arquivos/01/transactions1.csv').open(encoding='utf-8')))
    transactions2 = list(csv.reader(Path('arquivos/01/transactions2.csv').open(encoding='utf-8')))
    out1, out2 = reconcile_accounts(transactions1, transactions2)
    pprint(out1)
    pprint(out2)