### 数据类型

~~~
基本数据类型：number、string、boolean、null、undefined

引用数据类型：object、function、array
~~~

### 存储位置的不同

- 基本数据类型:将值存储在栈中,栈中存放的是对应的值
- 引用数据类型:将对应的值存储在堆中,栈中存放的是指向堆内存的地址

基础数据类型 赋值 赋的是真正的值，引用数据类型 赋值 赋的是 引用地址

### 深浅拷贝是对引用数据类型来做探讨的

- 拷贝（简单来说就是只拷贝第一层）
- 深拷贝（完全独立的双胞胎,彼此之间不会影响）

### JS常见的浅拷贝方法

~~~
1. Object.assign()
2. 扩展运算符
3. Array.concat()
4. Array.slice()
~~~

### JS常见的深拷贝方法

1. JSON.parse(JSON.stringify(待拷贝对象))

   ```
   有弊端（JSON数据类型不能完全的支持JS数据类型，JS一部分转成JSON后无法再转回来，对于JSON语法不支持的属性，序列化后会将其省略）
       对于JavaScript中的五种原始类型，JSON语法支持数字、字符串、布尔值、null四种，不支持undefined；
       NaN、Infinity和-Infinity序列化的结果是null；
       JSON语法不支持函数；
       除了RegExp、Error对象，JSON语法支持其他所有对象；
       日期对象序列化的结果是ISO格式的字符串，但JSON.parse()依然保留它们字符串形态，并不会将其还原为日期对象；
       JSON.stringify()只能序列化对象的可枚举的自有属性；
   ```

2. jQuery 中的 $.extend (添加true就是深拷贝,不添加就是浅拷贝)

### 练习

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>

</head>
<body>


<script>
    let obj = {
        name: 'hkw',
        age: 18,
        inner: [
            666, 777, [9]
        ],
        deep() {
            console.log('deep')
        }
    }
    // 浅拷贝（简单来说就是值拷贝第一层）
    // 1.es6的展开语法
    // let obj2 = {...obj};
    // obj2.name = 'jon';  // 源对象不会改变
    // obj2.inner[0] = 888;  // 源对象跟着改变
    // obj2.inner[2][0] = 999;  // 源对象跟着改变
    // console.log(obj);
    // console.log(obj2);

    // 2.Object.assign()
    // let obj2 = Object.assign({}, obj);
    // obj2.name = 'jon';  // 源对象不会改变
    // obj2.inner[0] = 888;  // 源对象跟着改变
    // obj2.inner[2][0] = 999;  // 源对象跟着改变
    // console.log(obj);
    // console.log(obj2);

    // 3.Array的slice和concat方法（针对数组）
    // let origin = [1, 2, 3, 4, [111, 222]];
    // let new_data = origin.slice();
    // new_data.push(5);
    // new_data[4].push(333);
    // console.log('origin：', origin);
    // console.log('new_data：', new_data);
    // contact操作类似

    // 深拷贝
    // 1.JSON.parse(JSON.stringify(待拷贝对象))
    // let obj2 = JSON.parse(JSON.stringify(obj));
    // console.log(obj, obj2);  // 弊端：不会拷贝内部函数（即obj2没有deep函数）

    // 2.jQuery 中的 $.extend (添加true就是深拷贝,不添加就是浅拷贝)
    // let origin = [1, 2, 3, 4, [111, 222]];
    // let new_data = [];
    // $.extend(true, new_data, origin);
    // // $.extend(new_data, origin);
    // new_data[4].push(666);
    // // origin[4].push(666);
    // // origin.push(666);
    // // new_data.push(666);
    // console.log('origin：', origin);
    // console.log('new_data：', new_data);


</script>


</body>
</html>

~~~

