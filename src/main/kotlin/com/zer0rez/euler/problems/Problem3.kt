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
//    private val term = 1234141233L
    private val term = 6857L //71L //104441L //600851475143L

    override fun solve(): Solution {
        val factors = sequence {
            var target = term
            var current = sqrt(target.toDouble()).toLong()
            while (current % 2 == 0L) {
                current /= 2
            }
            while (current < target) {
                print(" $current::$target")
                if (target % current == 0L) {
                    yield(current)
                    target = (target / current).toLong()
                }
                current -= 2
            }
        }
        val answer = 12
        return Solution(3, answer.toString(), factors.joinToString(", "))
    }
}