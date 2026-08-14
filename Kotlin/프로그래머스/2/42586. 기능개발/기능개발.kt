class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = mutableListOf<Int>()

        val doneDay = IntArray(progresses.size){0}

        for (i in progresses.indices) {
            doneDay[i] = (100 - progresses[i]) / speeds[i] + if((100 - progresses[i]) % speeds[i] > 0) 1 else 0
        }

        var maxDay = doneDay[0]
        var cnt = 1

        for (i in 1 until doneDay.size) {
            if (doneDay[i] <= maxDay) {
                cnt++
            }else{
                answer.addLast(cnt)
                cnt = 1
                maxDay = doneDay[i]
            }
        }

        answer.addLast(cnt)

        return answer.toIntArray()
    }
}