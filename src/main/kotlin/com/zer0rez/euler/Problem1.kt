package com.zer0rez.euler

import java.io.PrintStream

class Problem1 : Problem {
    // https://projecteuler.net/problem=1
    override fun solve(out: PrintStream) {
        var x = 0
        val r = generateSequence {
            (listOf(++x * 3, x * 5)).takeIf { x * 3 < 1000 }
        }.toList().flatten().filter { it < 1000 }.sorted().toSet().sum()
        out.println("Problem 1: $r")
    }
}
