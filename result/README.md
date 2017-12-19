### My Running Result

> Last Update Time: 2017-12-19 3:11:20

> 最后更新时间: 2017-12-19 3:11:20


1. Read
```python
import pickle
all_cates = pickle.load(open('all', 'rb'))
```

2. Struct
```
{
    cate_name:
    {
        cate_name:
        {
            ...
            cate_name:
            {
                text: 'spu name'
                attr:
                [
                    'text':
                    [
                        'value1',
                        'value2',
                        ...
                    ]
                ]
                prors:
                [
                    'value1',
                    'value2',
                    ...
                ]
            }
        }
    }
}
```