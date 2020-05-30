# ノック 002

csv データ（transaction_1.csv, transaction_2.csv) を 読み込み結合せよ。


```
  transaction_id   price         payment_date customer_id
0    T0000000113  210000  2019-02-01 01:36:57    PL563502
1    T0000000114   50000  2019-02-01 01:37:23    HD678019
2    T0000000115  120000  2019-02-01 02:34:19    HD298120
3    T0000000116  210000  2019-02-01 02:47:23    IK452215
4    T0000000117  170000  2019-02-01 04:33:46    PL542865

transaction_1 count : 5000
transaction_2 count : 1786
transaction count : 6786


```

```
   detail_id transaction_id item_id  quantity
0          0    T0000000113    S005         1
1          1    T0000000114    S001         1
2          2    T0000000115    S003         1
3          3    T0000000116    S005         1
4          4    T0000000117    S002         2

transaction_detail_1 count : 5000
transaction_detail_2 count : 2144
transaction_detail count : 7144
```