package com.zer0rez.euler.problems

import com.google.common.math.LongMath
import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import com.zer0rez.euler.util.isDivisibleByAny

class Problem10 : Problem {
    override fun solve(): Solution {
        val primes = longArrayOf(2).toMutableList()
        val start = primes.max()!! + 2
        (start..2000000L).forEach { if (!it.isDivisibleByAny(primes)) primes.add(it) }
        val test = (start..2000000L step 2).filter {
            LongMath.isPrime(it)
        }.toList()
        println("test: ${test}")
        println("primes - test: ${(primes - test).slice(1..100)}")
        return Solution(10, primes.sum().toString(), "${primes}")
    }
}
// 	00:25:9C:57:F5:6D
// primes - test: [5, 7, 9, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]