r"""
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.
"""

import re

print("------字符串匹配------")
p = r'\w+@163.com'
email001 = '110@163.com'
email002 = '110@162.com'
# 匹配成功,返回一个对象
m = re.match(p, email001)
print(type(m))
# 匹配失败,返回none
m = re.match(p, email002)
print(type(m))

print("\r\n------字符串查找------")
text = 'Tmo`s email is 110@163.com'
m = re.search(p, text)
print("起始--结束索引:{0},匹配字符：{1}".format(list(m.span()), m.group()))

p = r'[J,j][A,a][v,V][a,A]'
text = 'i lile java Java and JAVA'
match_list = re.findall(p, text)
print(match_list)

print("\r\n------字符串替换------")
# 匹配数字出现一次或多次
p = r'\d+'
text = 'AB12CD34EF56'
repace_txet = re.sub(p, ' ', text)
print("替换全部匹配字符:", repace_txet)
repace_txet = re.sub(p, ' ', count=1)
print("替换规定数量的匹配字符:", repace_txet)
