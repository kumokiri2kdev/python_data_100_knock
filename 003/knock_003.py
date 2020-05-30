import pandas as pd

if __name__ == '__main__':
    transaction_1 = pd.read_csv('../csv/transaction_1.csv')
    transaction_2 = pd.read_csv('../csv/transaction_2.csv')

    transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)

    transaction_detail_1 = pd.read_csv('../csv/transaction_detail_1.csv')
    transaction_detail_2 = pd.read_csv('../csv/transaction_detail_2.csv')

    transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

    join_data = pd.merge(transaction_detail,
                         transaction[['transaction_id', 'payment_date', 'customer_id']],
                         on='transaction_id', how='left')


    print(join_data.head())