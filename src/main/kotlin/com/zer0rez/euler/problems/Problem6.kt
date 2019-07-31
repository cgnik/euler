package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution

class Problem6 : Problem {
    override fun solve(): Solution {
        val r = (1..100)
        val s = r.sum()
        val squareOfSum = s * s
        val sumOfSquares = r.map { it * it }.sum()
        val answer = squareOfSum - sumOfSquares
        return Solution(6, answer.toString(), "sumOfSquares: $sumOfSquares, squareOfSums: $squareOfSum")
    }
}