import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

example_input = '''
老师：这节课，我们就来一起认识一下Python最基础的3种数据类型。

没有很多，就3种，而且你基本都和他们打过照面了：

- 整数(int)
- 浮点数(float)
- 字符串(str)

<img src="https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230916111933.png"/>

### 整数int

<img src="https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230916221934.png"/>

整数(integer) 其实非常简单，就等同于我们小学数学里学到的“整数”概念。

我们上次让你print(42)，这个 42 就是整数类型的。

你可以对整数进行各种数学运算，就像我们试过的print(1+2) 一样。

Python中的运算符号如下
<img src="https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230915181353.png"/>

我们可以搞个稍微复杂点的式子让python算一下：

```python
print((4+2)*3-8)
```

你可以尝试运行一下，应该是秒出结果，结果是10

学生：没错。果然是数学学霸~

老师：哈哈哈，没错。我们继续。
'''

example_output = '''·
```cleword
- 发言:
    谁: 思远
    说:
    - 这节课，我们就来一起认识一下Python最基础的3种数据类型。
    - 没有很多，就3种，而且你基本都和他们打过照面了：

- 图片:
    地址: https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230916111933.png

- 大纲:
    标题: 整数int
    等级: 2

- 图片:
    地址: https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230916221934.png

- 发言:
    谁: 思远
    说:
    - 整数(integer) 其实非常简单，就等同于我们小学数学里学到的“整数”概念。
    - 我们上次让你print(42)，这个 42 就是整数类型的。
    - 你可以对整数进行各种数学运算，就像我们试过的print(1+2) 一样。
    - Python中的运算符号如下
- 图片:
    地址: https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20230915181353.png

- 发言:
    谁: 思远
    说:
    - 我们可以搞个稍微复杂点的式子让python算一下：
    - |
        ```python
        print((4+2)*3-8)
        ```
    - 你可以尝试运行一下，应该是秒出结果，结果是10

- 发言:
    谁: 学生
    说:
    - 没错。果然是数学学霸~

- 发言:
    谁: 思远
    说:
    - 哈哈哈，没错。我们继续。
```
'''

def get_completion_from_messages(messages, model="gpt-4-1106-preview", temperature=0):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
    #     print(str(response.choices[0].message))
        return response.choices[0].message["content"]

def generate_cleword(content):

    system_message = "你是一名优秀的课程文稿录入员，擅长把markdown格式的课程文稿，转化为一种叫做cleword的领域特定语言。"
    user_message = f"""
              你是一名优秀的课程文稿录入员。我将给你markdown格式的课程文稿，请你帮助我把这种文稿转化为一种叫做cleword的领域特定语言。下面是一些转化的基本规则：
              cleword是一种基于yaml的，缩进敏感的领域特定语言。它被专门用来创作课程。
              以下是某节课部分内容的cleword语法示例，这门课的内容演示了一个名叫思远的老师，教给名叫大乾的学生关于Python的变量的知识的场景。请注意其中出现的对于不同元素的语法规则和缩进，以及我给出的 “#” 号后面的语法注释：

              ```cleword
                - 发言:
                    谁: 思远
                    说:
                      - ok，那现在请你在自己的电脑中打开python，我们开始接下来的学习✊✊ #cleword语法注释：在一个”发言“下面，每一个短杠 “ - ” 就代表一条对话消息
                      - 前面，我们学习了Python的print()函数和3种基本数据类型。这能够让Python把一些东西“说”给我们听。

                - 图片: #cleword语法注释：请注意图片的语法。
                    地址: https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20231026105853.png

                - 问卷: #cleword语法注释：遇到选择题时，可以用这种语法。
                    类型: 单选    #cleword语法注释：类型可以是单选也可以是多选。
                    标题: 请对以下作出选择1
                    选项:
                      - 第一项A
                      - 第二项B
                      - 第三项C
                    答案:   #cleword语法注释：如果需要设置正确答案，则下面正确的答案要与上面的选项保持一致
                      - 第一项A
                    解析: |   #cleword语法注释：答案的具体解析
                      正确答案是第一项哦

                - 发言:
                    谁: 思远
                    说:
                      - 但是目前，我们所有的程序都只是运行一步，把一个值打印出来。
                      - |  #cleword语法注释：在“ - | ”的下面，可以在同一个对话消息内写符合markdown语法的内容
                        这对于更复杂的程序而言，肯定是不够用的。 
                        - 数据如何在程序中被传递？
                        - 如何实现多个步骤的程序？ 
                      - 这些都是问题。
                - 发言:
                    谁: 大乾
                    说:
                      - 复杂的程序？
                - 发言:
                    谁: 思远
                    说:
                      - 举个具体点例子来说，
                      - 比如我们想用Python写一个进制转换的小程序，它能够自动把你输入进去的十进制进制的数字，转化为二进制数字。
                      - 这个程序的构架会大概长下面这样：
                - 图片:
                    地址: https://siyuan-harry.oss-cn-beijing.aliyuncs.com/oss://siyuan-harry/20231013113342.png

                - 发言:
                    谁: 思远
                    说:
                      - 这里，我们需要 变量 来帮助这个程序做得更好。

                - 大纲: #cleword语法注释：markdown文稿中的一二三级标题，都应当转换为cleword里的对应等级大纲
                    标题: 1 什么是变量
                    等级: 1

                - 发言:
                    谁: 思远
                    说:
                      - |
                        虽然变量是个非常重要的东西，但其实它一点都不难，很容易理解。
                        > 只要你用心去做！
                      - | #cleword语法注释：在“ - | ”的下面，可以在同一个消息内写符合markdown语法的内容。比如这条消息中文字+Python代码块
                        多说无益，先来尝试运行一下下面这个代码：
                        ```python
                        weather = '今天的天气是多云转晴'
                        print(weather)
                        ```
                      - 还有下面这个:
                      - |
                        ```python
                        number = -4

                        if number > 0:
                            print("这是一个正数")

                        print('123')
                        ```

                - 旁白: 请自己在本地的编辑器里手打出来，不要复制粘贴哦 #cleword语法注释：“旁白”的语法就是这样的
              ```

              接下来，我将给你一个markdown版本的原始课程文稿。请你把它转化为cleword格式输出。
              原始文稿：「{content}」

              请你注意原始文稿里的markdown语法格式（如人物标记、图片、旁白标记、代码块等），并将原始文稿逐句地转化为符合cleword语法的格式。

            """
    messages =  [
                {'role':'system',
                'content': system_message},
                {'role':'user',
                'content': user_message},
            ]
    response = get_completion_from_messages(messages)
    return response

def app():
    
    st.title('''Markdown-to-Cleword v0.0.1 🎉''')

    col1, col2 = st.columns(2)
    
    with col1:
        script = st.text_area('请输入你想要转为cleword的markdown文稿：')
        btn = st.button('提交')

        with st.expander('输入示例'):
            st.text_area('', value = example_input, height=500)

        with st.expander('输出示例'):
             st.markdown(example_output)

    with col2:
        st.markdown('转化结果如下👇')
        if btn:
            cleword = generate_cleword(script)
            st.markdown(cleword)
    

if __name__ == '__main__':
    app()