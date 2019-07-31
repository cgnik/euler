package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import com.zer0rez.euler.util.factorize

/**
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
 */
class Problem3 : Problem {
    private val term = 600851475143L

    override fun solve(): Solution {
        val factors = term.factorize().toMutableList()
        factors.addAll(factors.flatMap { it.factorize().toList() })
        val answer = factors.max()
        return Solution(3, answer.toString(), factors.joinToString(", ")) // answer is 6857L
    }
}