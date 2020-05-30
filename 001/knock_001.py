import pandas as pd


if __name__ == '__main__':
    customer_master = pd.read_csv('../csv/customer_master.csv')
    print(customer_master.head())

    item_master = pd.read_csv('../csv/item_master.csv')
    print(item_master.head())

    transaction_1 = pd.read_csv('../csv/transaction_1.csv')
    print(transaction_1.head())

    transaction_detail_1 = pd.read_csv('../csv/transaction_detail_1.csv')
    print(transaction_detail_1.head())