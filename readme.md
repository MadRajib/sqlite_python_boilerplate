```bash
$ py -i app.py 
>>> insert_in_table("product",data)
>>> get_all_from_table("product")
(3, 'data', 'data', 'data', 678.0)
(4, 'data', 'data', 678.0, 1233.0)
>>> update_from_table("product",3, 6334)
>>> get_all_from_table("product")
(3, 'data', 'data', 'data', 6334.0)
(4, 'data', 'data', 678.0, 1233.0)
>>> 
```