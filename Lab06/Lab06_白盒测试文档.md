## 白盒测试报告

1. 白盒测试流程图

   ```mermaid
   flowchart LR
   		A(开始) -->|1| B[/输入a, b, c/] -->|2| C{判断 a, b, c 是否\n都是 int 类型}
   		C -->|否 3| D[/输出'not a triangle!'/] -->|4| E(结束)
   		C -->|是 5| F{判断 a, b, c 是否都\n在 1 到 10000之间\n并且任意两边之和\n大于第三边} -->|否 6| D
   		F -->|是 7| G{a, b, c 是否\n两两相等} -->|是 8| H[/输出'equilateral triangle!'/] -->|9| E
   		G -->|否 10| I{a, b, c是否\n存在两个数相等} -->|是 11| J[/输出'isosceles triangle!'/] -->|12| E
   		I -->|否 13| K[/输出'regular triangle!'/] -->|14| E
   ```

2. 白盒测试分支覆盖表及用例表

   | 输入        | 执行路径         |
   | ----------- | ---------------- |
   | "3", 4, 5   | 1 2 3 4          |
   | 3.1, 4, 5   | 1 2 3 4          |
   | 0, 4, 5     | 1 2 5 6 4        |
   | 10001, 4, 5 | 1 2 5 6 4        |
   | 3, 3, 9     | 1 2 5 6 4        |
   | 3, 3, 3     | 1 2 5 7 8        |
   | 3, 3, 4     | 1 2 5 7 10 11 12 |
   | 3, 4, 4     | 1 2 5 7 10 11 12 |
   | 3, 4, 3     | 1 2 5 7 10 11 12 |
   | 3, 4, 5     | 1 2 5 7 10 13 14 |

3. 正确实现的白盒测试用例执行结果截图

   ![截屏2022-04-23 15.42.54](https://cdn.jsdelivr.net/gh/hjc-owo/allImgs/img/202204231543911.png)

   ```python
   import unittest
   
   from White import Triangle
   
   
   class MyTest(unittest.TestCase):
       # 编写测试用例，记得要以t开头，例：test
       def testTriangle(self):
           # 调用内部的测试方法，如：assertEqual,assertNotEqual 等
           self.assertEqual(Triangle.triangle("3", 4, 5), "not a triangle!")
           self.assertEqual(Triangle.triangle(3.1, 4, 5), "not a triangle!")
           self.assertEqual(Triangle.triangle(0, 4, 5), "not a triangle!")
           self.assertEqual(Triangle.triangle(10001, 4, 5), "not a triangle!")
           self.assertEqual(Triangle.triangle(3, 3, 9), "not a triangle!")
           self.assertEqual(Triangle.triangle(3, 3, 3), "equilateral triangle!")
           self.assertEqual(Triangle.triangle(3, 3, 4), "isosceles triangle!")
           self.assertEqual(Triangle.triangle(3, 4, 4), "isosceles triangle!")
           self.assertEqual(Triangle.triangle(3, 4, 3), "isosceles triangle!")
           self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")
   
       pass
   
   
   # 运行测试
   if __name__ == '__main__':
       unittest.main()
   
   ```

4. 带缺陷实现的白盒测试用例执行结果截图

   ![截屏2022-04-23 15.42.42](https://cdn.jsdelivr.net/gh/hjc-owo/allImgs/img/202204231543095.png)

   ```python
   def triangle(a, b, c):
       if a == int(a) and b == int(b) and c == int(c):
           if 1 <= a <= 10000 and 1 <= b <= 10000 and 1 <= c <= 10000 \
                   and a + b > c and a + c > b and b + c > a:
               if a == b and b == c:
                   return "equilateral triangle!"
               # elif a == b or b == c or a == c:
               #     return "isosceles triangle!"
               else:
                   return "regular triangle!"
           else:
               return "not a triangle!"
       else:
           return "not a triangle!"
   
   ```

   
