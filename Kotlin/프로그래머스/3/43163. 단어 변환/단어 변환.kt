class Solution {
    fun solution(begin: String, target: String, words: Array<String>): Int {

        val wordsSet = HashSet<String>()
        for (word in words) wordsSet.add(word)

        if (!wordsSet.contains(target)) return 0

        val q = ArrayDeque<Pair<String, Int>>()
        q.addFirst(Pair(begin, 0))


        while (!q.isEmpty()) {
            val (curr, cnt) = q.removeLast()
            if (curr == target) return cnt
            
            for (letterIdx in curr.indices) {
                for (i in 'a'..'z') {
                    if (i == curr[letterIdx]) continue

                    val newWord = replaceChar(curr, letterIdx, i)

                    if (!wordsSet.contains(newWord)) continue

                    q.addFirst(Pair(newWord, cnt + 1))
                }
            }
        }
        
        return 404
    }

    fun replaceChar(str: String, idx: Int, newChar: Char): String {
        if (idx !in str.indices) return str
        return StringBuilder(str).apply {
            setCharAt(idx, newChar)
        }.toString()
    }
}