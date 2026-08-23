class Solution {
    lateinit var connect: Array<MutableList<Int>>
    lateinit var visited: BooleanArray
    
    fun solution(n: Int, computers: Array<IntArray>): Int {
        visited = BooleanArray(n)
        connect = Array(n) { mutableListOf() }

        for (i in 0 until n) {
            for (j in 0 until n) {
                if (computers[i][j] == 0) continue

                connect[i].add(j)
                connect[j].add(i)
            }
        }

        var answer = 0

        for (i in 0 until n) {
            if (bfs(i)) continue
            answer++
        }

        return answer
    }

    fun bfs(idx: Int): Boolean {
        if (visited[idx]) return true

        val q = ArrayDeque<Int>()
        q.addFirst(idx)

        while (q.isNotEmpty()) {
            val curr = q.removeLast()
            visited[curr] = true

            for (next in connect[curr]) {
                if (visited[next]) continue

                q.addFirst(next)
            }
        }

        return false
    }
}