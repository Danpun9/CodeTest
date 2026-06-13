class Solution {
    fun solution(angle: Int): Int {
        return if(angle in 1..89) 1 else if(angle == 90) 2 else if (angle in 91..179) 3 else 4
    }
}