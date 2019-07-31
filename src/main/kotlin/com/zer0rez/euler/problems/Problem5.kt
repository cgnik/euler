package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import com.zer0rez.euler.util.isDivisibleByAll

class Problem5 : Problem {
    private val target = 2520
    private val divisors = (1..20).toList().toIntArray()
    override fun solve(): Solution {
        var c = 20
        val answer = generateSequence { (c++) }.first { it.isDivisibleByAll(divisors) }
        return Solution(5, answer.toString(), "in ${c - 20} cycles")
    }
}