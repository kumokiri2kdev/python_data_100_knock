import pandas as pd

if __name__ == '__main__':
    transaction_1 = pd.read_csv('../csv/transaction_1.csv')
    transaction_2 = pd.read_csv('../csv/transaction_2.csv')

    transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)

    print(transaction.head())

    print('transaction_1 count : {}'.format(len(transaction_1)))
    print('transaction_2 count : {}'.format(len(transaction_2)))
    print('transaction count : {}'.format(len(transaction)))

    transaction_detail_1 = pd.read_csv('../csv/transaction_detail_1.csv')
    transaction_detail_2 = pd.read_csv('../csv/transaction_detail_2.csv')

    transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

    print(transaction_detail.head())

    print('transaction_detail_1 count : {}'.format(len(transaction_detail_1)))
    print('transaction_detail_2 count : {}'.format(len(transaction_detail_2)))
    print('transaction_detail count : {}'.format(len(transaction_detail)))