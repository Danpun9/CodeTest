class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0

        for (i in s.indices) {
            val str = s.substring(i, s.length) + s.substring(0, i)

            if (check(str)) answer++
        }

        return answer
    }

    fun check(str: String): Boolean{
        var stack = ArrayDeque<Char>()

        for (i in str.indices){
            if(stack.isEmpty()) stack.addFirst(str[i])
            else if (stack[0] == '(' && str[i] == ')') stack.removeFirst()
            else if (stack[0] == '{' && str[i] == '}') stack.removeFirst()
            else if (stack[0] == '[' && str[i] == ']') stack.removeFirst()
            else stack.addFirst(str[i])
        }

        return stack.isEmpty()
    }
}

fun main(){
    println(Solution().solution("[](){}"))
}