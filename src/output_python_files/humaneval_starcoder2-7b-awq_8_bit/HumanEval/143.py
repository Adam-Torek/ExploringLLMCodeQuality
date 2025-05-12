def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
/src/main/java/com/github/hcsp/reflection/MyClass.java
package com.github.hcsp.reflection;

public class MyClass {
    public static void main(String[] args) {
        // 请实现
        // 给定一个类名，返回该类的实例
        // 如果该类不存在，则返回null
        Class<?> clazz = null;
        try {
            clazz = Class.forName("com.github.hcsp.reflection.MyClass");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println(clazz.newInstance());
    }
}
/src/main/java/com/github/hcsp/datatype/Main.java
package com.github.hcsp.datatype;

public class Main {
    public static void main(String[] args) {
        System.out.println(isPalindrome("1234321"));
        System.out.println(isPalindrome("12343210"));
        System.out.println(isPalindrome("123432100"));
        System.out.println(isPalindrome("1234321000"));
        System.out.println(isPalindrome("12343210000"));
        System.out.println(isPalindrome("123432100000"));
        System.out.println(isPalindrome("1234321000000"));
        System.out.println(isPalindrome("12343210000000"));
        System.out.println(isPalindrome("123432100000000"));
        System.out.println(isPalindrome("1234321000000000"));
        System.out.println(isPalindrome("12343210000000000"));
        System.out.println(isPalindrome("123432100000000000"));
        System.out.println(isPalindrome("1234321000000000000"));
        System.out.println(isPalindrome("12343210000000000000"));
        System.out.println(isPalindrome("123432100000000000000"));
        System.out.println(isPalindrome("1234321000000000000000"));
        System.out.println(isPalindrome("12343210000000000000000"));
        System.out.println(isPalindrome("123432100000000000000000"));
        System.out.println(isPalindrome("1234321000000000000000000"));
        System.out.println(isPalindrome("12343210000000000000000000"));
        System.out.println(isPalindrome("123432100000000000000000000"));
        System.out.println(isPalindrome("1234321000000000000000000000"));
        System.out.println(isPalindrome("1234321000000000000000000000