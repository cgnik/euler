package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import kotlin.math.roundToLong
import kotlin.math.sqrt

fun largestTerm(term: Long) = sqrt(term.toDouble()).roundToLong()
/**
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
 */

class Problem3 : Problem {
    private val term = 600851475143

    override fun solve(): Solution {
        val factors = generateSequence {
            factor(term)
        }.toList()
        val answer = 12
        return Solution(3, answer.toString(), factors.joinToString(", "))
    }

    fun factor(num: Long): Sequence<Long?> {
        var current = largestTerm(num)
        while (current % 2L == 0L) current /= 2
        return sequence {
            while (current > 1) {
                if (num % current == 0L) yield(current)
                current -= 2
            }
            yield(null)
        }
    }
}