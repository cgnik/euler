package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import com.zer0rez.euler.util.isDivisibleByAny

class Problem7 : Problem {
    val firstPrime = 2
    val primeCount = 10001
    override fun solve(): Solution {
        var current = 2L
        var primes = ArrayList<Long>(2)
        while (primes.count() < primeCount) {
            if (!(++current).isDivisibleByAny(primes)) {
                primes.add(current)
            }
        }
        val answer = primes.last()
        return Solution(7, answer.toString(), "[${primes}]")
    }
}