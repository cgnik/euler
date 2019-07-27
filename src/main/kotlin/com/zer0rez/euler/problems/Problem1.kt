package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution

class Problem1 : Problem {
    // https://projecteuler.net/problem=1
    override fun solve() : Solution {
        var x = 0
        val r = generateSequence {
            (listOf(++x * 3, x * 5)).takeIf { x * 3 < 1000 }
        }.toList().flatten().filter { it < 1000 }.sorted().toSet().sum()
        return Solution(1, r.toString(), "")
    }
}
