package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import kotlin.math.roundToLong

/**
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
 */

class Problem3 : Problem {
    private val term = 600851475143
    private val half = (term.toDouble() / 2.0).roundToLong()
    override fun solve(): Solution {
        val answer = LongRange(half, 1).firstOrNull { term % it == 0L }
        return Solution(3, answer.toString(), "")
    }
}